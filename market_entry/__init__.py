from otree.api import *
import random
import itertools

class C(BaseConstants):
    NAME_IN_URL = 'market_entry'
    PLAYERS_PER_GROUP = None  
    NUM_ROUNDS = 5
    TIMEOUT_SECONDS = 10
    TREATMENTS = ['control', 'choice_blindness', 'choice_overload', 'both']
    MAX_FIRMS = 4         
    PROFIT_IF_MONOPOLY_RANGE = (90, 110)  # Range for monopoly profit
    PROFIT_IF_COMPETITION_RANGE = (-15, -5)  # Range for competition profit

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass  # Not used in single-player

class Player(BasePlayer):
    decision = models.StringField(
        choices=[('enter', 'Enter the Market'), ('stay_out', 'Stay Out')],
        widget=widgets.RadioSelect,
        label='What is your decision?'
    )
    outcome = models.StringField()
    game_payoff = models.CurrencyField()
    comment_result = models.LongStringField(blank=True, label="What do you think about the results of the game you played?")
    comment_optional = models.LongStringField(blank=True, label="Is there anything in particular you want to comment on? (optional)")


# Pages

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
    timeout_seconds = C.TIMEOUT_SECONDS

    def vars_for_template(player: Player):
        return {'treatment': player.participant.vars['treatment']}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        treatment = player.participant.vars.get('treatment', 'control')  # Default to 'control' if not found

        # Apply treatments (same as before)
        if treatment == 'choice_overload' or treatment == 'both':
            if timeout_happened:
                player.decision = random.choice(['enter', 'stay_out'])

        if treatment == 'choice_blindness' or treatment == 'both':
            player.decision = random.choice(['enter', 'stay_out'])

        # Simulate market outcomes
        num_entering = random.randint(0, C.MAX_FIRMS)  

        if player.decision == 'enter':
            if num_entering == 0:
                player.game_payoff = cu(random.randint(*C.PROFIT_IF_MONOPOLY_RANGE))
            else:
                player.game_payoff = cu(random.randint(*C.PROFIT_IF_COMPETITION_RANGE))
        else:
            player.game_payoff = cu(0)

        # Outcome for feedback (may be different from actual decision due to treatments)
        if treatment == 'choice_blindness' or treatment == 'both':
            player.outcome = random.choice(['enter', 'stay_out'])
        else:
            player.outcome = player.decision 

class Results(Page):
    form_model = 'player'
    form_fields = ['comment_result', 'comment_optional']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'decision': player.decision,
            'outcome': player.outcome,  
            'game_payoff': player.game_payoff,
            'num_entering': 1 if player.outcome == 'enter' else 0 + (0 if player.decision == 'enter' and player.outcome == 'stay_out' else random.randint(0, C.MAX_FIRMS - 1))
        }

    @staticmethod
    def error_message(player: Player, values):
        if not values['comment_result']:
            return 'Please provide your thoughts on the results.'

page_sequence = [Decision, Results]
