from otree.api import *
import random
import itertools

class C(BaseConstants):
    NAME_IN_URL = 'public_goods'
    PLAYERS_PER_GROUP = None  # Single player
    NUM_ROUNDS = 5
    TIMEOUT_SECONDS = 10
    TREATMENTS = ['control', 'choice_blindness', 'choice_overload', 'both']
    ENDOWMENT = cu(100)          # Initial endowment for each player
    MULTIPLIER = 1.6             # Multiplier for total contributions

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass  

class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT,
        label="How much of your endowment ({} points) would you like to contribute to the public good?".format(C.ENDOWMENT)
    )
    outcome = models.CurrencyField()  
    game_payoff = models.CurrencyField()
    comment_result = models.LongStringField(blank=True, label="What do you think about the results of the game you played?")
    comment_optional = models.LongStringField(blank=True, label="Is there anything in particular you want to comment on? (optional)")


# Pages

class Decision(Page):
    form_model = 'player'
    form_fields = ['contribution']
    timeout_seconds = C.TIMEOUT_SECONDS

    @staticmethod
    def vars_for_template(player: Player):
        return {'treatment': player.participant.vars['treatment']}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        treatment = player.participant.vars.get('treatment', 'control')  # Default to 'control' if not found

        # Apply treatments
        if treatment == 'choice_overload' or treatment == 'both':
            if timeout_happened:
                player.contribution = random.randint(0, C.ENDOWMENT)
        if treatment == 'choice_blindness' or treatment == 'both':
            player.contribution = random.randint(0, C.ENDOWMENT)
        
        # Simulate other players' contributions and calculate payoff
        # In this single-player case, we'll just assume zero contribution from others
        total_contribution = player.contribution 
        player.outcome = total_contribution * C.MULTIPLIER
        player.game_payoff = C.ENDOWMENT - player.contribution + (player.outcome / 1)  # Divide by 1 since there's only one player

        # Outcome for feedback (may be different from actual decision due to treatments)
        if treatment == 'choice_blindness' or treatment == 'both':
            player.outcome = random.randint(0, C.ENDOWMENT) * C.MULTIPLIER
        else:
            player.outcome = player.contribution * C.MULTIPLIER


class Results(Page):
    form_model = 'player'
    form_fields = ['comment_result', 'comment_optional']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'contribution': player.contribution,
            'outcome': player.outcome,
            'game_payoff': player.game_payoff
        }

    @staticmethod
    def error_message(player: Player, values):
        if not values['comment_result']:
            return 'Please provide your thoughts on the results.'

page_sequence = [Decision, Results]
