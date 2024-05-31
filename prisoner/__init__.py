from otree.api import *
import random
from .payoff_tables import round_1, round_2, round_3, round_4, round_5  # Import from payoff_tables.py

class C(BaseConstants):
    NAME_IN_URL = 'prisoners_dilemma'
    PLAYERS_PER_GROUP = None 
    NUM_ROUNDS = 5
    TIMEOUT_SECONDS = 10
    TREATMENTS = ['control', 'choice_blindness', 'choice_overload', 'both'] 

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
    outcome = models.StringField(choices=['cooperate', 'defect'], blank=True, initial=None) 
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
    def get_context_data(player: Player, **kwargs):
        context = super().get_context_data(**kwargs)
        context['player'] = player
        from . import payoff_tables
        payoff_table = getattr(payoff_tables, f'round_{self.player.round_number}', {}) 

        # If not found, use default payoffs
        if not payoff_table:
            payoff_table = {'CC': (0, 0), 'CD': (0, 0), 'DC': (0, 0), 'DD': (0, 0)}
        
        context.update({
            'payoff_cc': payoff_table.get('CC'),
            'payoff_cd_you': payoff_table.get('CD', [0, 0])[0],
            'payoff_cd_computer': payoff_table.get('CD', [0, 0])[1],
            'payoff_dc_you': payoff_table.get('DC', [0, 0])[0],
            'payoff_dc_computer': payoff_table.get('DC', [0, 0])[1],
            'payoff_dd': payoff_table.get('DD'),
        })
        return context

    @staticmethod
    def vars_for_template(player: Player):
        # Get the treatment from participant variables
        treatment = player.participant.vars.get('treatment', 'control')  
        return {'treatment': treatment} 

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        """Handle player decisions, computer choices, and payoff calculations."""
        treatment = player.participant.vars.get('treatment', 'control')
        from . import payoff_tables #Import here

        if treatment in ['choice_overload', 'both']:
            if timeout_happened:
                player.decision = random.choice(['cooperate', 'defect'])
        if treatment in ['choice_blindness', 'both']:
            player.decision = random.choice(['cooperate', 'defect'])

        player.computer_decision = random.choice(['C', 'D'])
        
        outcome_key = player.decision[0].upper() + player.computer_decision
        payoff_table = getattr(payoff_tables, f'round_{player.round_number}', {}) 

        if not payoff_table:  # Check if a valid payoff table was found
            payoff_table = {'CC': (0, 0), 'CD': (0, 0), 'DC': (0, 0), 'DD': (0, 0)} # Default values

        payoff_range = payoff_table[outcome_key]
        player.game_payoff = cu(random.randint(*payoff_range))

class Results(Page):
    form_model = 'player'
    form_fields = ['comment_result', 'comment_optional']

    def get_context_data(self, **kwargs):
        """Add round_number to context."""
        context = super().get_context_data(**kwargs)
        context['round_number'] = self.round_number
        return context

    @staticmethod
    def vars_for_template(player: Player):
        """Provide template variables, handling potential missing payoffs gracefully."""
        payoff_table = getattr(payoff_tables, f'round_{player.round_number}', None)

        # Handle the case where payoff_table is not found
        if payoff_table is None:
            payoff_table = {'CC': (0, 0), 'CD': (0, 0), 'DC': (0, 0), 'DD': (0, 0)}

        same_choice = player.decision[0].upper() == player.computer_decision

        return {
            'decision': player.decision,
            'outcome': player.field_maybe_none('outcome'),
            'computer_decision': player.computer_decision,
            'game_payoff': player.game_payoff,
            'same_choice': same_choice,
            'payoff_cc': payoff_table['CC'],
            'payoff_cd_you': payoff_table['CD'][0],
            'payoff_cd_computer': payoff_table['CD'][1],
            'payoff_dc_you': payoff_table['DC'][0],
            'payoff_dc_computer': payoff_table['DC'][1],
            'payoff_dd': payoff_table['DD'],
        }


    def error_message(player: Player, values):
        if not values['comment_result']:
            return 'Please provide your thoughts on the results.'

page_sequence = [Decision, Results]
