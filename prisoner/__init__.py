from otree.api import *
import random
import itertools

class C(BaseConstants):
    NAME_IN_URL = 'prisoners_dilemma'
    PLAYERS_PER_GROUP = None 
    NUM_ROUNDS = 5
    TIMEOUT_SECONDS = 10
    TREATMENTS = ['control', 'choice_blindness', 'choice_overload', 'both'] 
    PAYOFF_RANGES = {
        'CC': (8, 12), 
        'CD': (-2, 2), 
        'DC': (18, 22),
        'DD': (3, 7)
    }

class Subsession(BaseSubsession):
    pass  # No need for creating_session as treatment is assigned in another app

class Group(BaseGroup):
    pass  

class Player(BasePlayer):
    decision = models.StringField(
        choices=[('cooperate', 'Cooperate'), ('defect', 'Defect')],
        widget=widgets.RadioSelect,
        label='What is your decision?'
    )
    outcome = models.StringField(choices=['cooperate', 'defect'])
    computer_decision = models.StringField(choices=['cooperate', 'defect'])
    game_payoff = models.CurrencyField()
    comment_result = models.LongStringField(
        label="What do you think about the results of the game you played?"
    )
    comment_optional = models.LongStringField(
        blank=True, label="Is there anything in particular you want to comment on? (optional)"
    )
    


# Pages

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
    timeout_seconds = C.TIMEOUT_SECONDS

    @staticmethod
    def vars_for_template(player: Player):
        treatment = player.participant.vars.get('treatment', 'control')  # Get treatment with default
        return {'treatment': treatment}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):            
        treatment = player.participant.vars.get('treatment', 'control')  # Default to 'control' if not found

        if treatment in ['choice_overload', 'both']:
            if timeout_happened:
                player.decision = random.choice(['cooperate', 'defect'])
        if treatment in ['choice_blindness', 'both']:
            player.decision = random.choice(['cooperate', 'defect'])

        player.computer_decision = random.choice(['C', 'D'])  # Use 'C' and 'D' instead of 'cooperate' and 'defect'
        
        # Create the outcome key as a 2-character string representing both decisions
        outcome_key = player.decision[0].upper() + player.computer_decision  
        
        payoff_range = C.PAYOFF_RANGES[outcome_key]
        player.game_payoff = cu(random.randint(*payoff_range))


class Results(Page):
    form_model = 'player'
    form_fields = ['comment_result', 'comment_optional']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'decision': player.decision,
            'outcome': player.outcome,
            'computer_decision': player.computer_decision,  # Add this line
            'game_payoff': player.game_payoff
        }
    def error_message(player: Player, values):
        if not values['comment_result']:
            return 'Please provide your thoughts on the results.'

page_sequence = [Decision, Results]
