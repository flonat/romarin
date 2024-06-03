from otree.api import *
import random
import itertools
c = cu
doc = ''

# Models
class C(BaseConstants):
    NAME_IN_URL = 'introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1       
    TREATMENTS = ['control', 'choice_blindness', 'choice_overload', 'both'] 

    
class Subsession(BaseSubsession):
    def creating_session(self):
        """Assign treatments to participants."""
        players = self.get_players()
        random.shuffle(players) 
        treatments = itertools.cycle(C.TREATMENTS)
        for player in self.get_players():
            treatment = next(treatments)  # Get the next treatment from the cycle
            player.participant.vars['treatment'] = treatment
                
                
class Group(BaseGroup):
    pass

class Player(BasePlayer):
    intro_start_time = models.FloatField()
    intro_end_time = models.FloatField()    
    participant_type = models.StringField(
        choices=[
            ('student', 'A student in Professor Nagel\'s class'),
            ('random', 'A person who just received the link to participate'),
            ('prolific', 'A Prolific user')
        ],
        widget=widgets.RadioSelect,
        label='What kind of participant are you?'
    )
    fictitious_name = models.StringField(blank=True)
    prolific_id = models.StringField(blank=True)
    time_spent_games_intro = models.FloatField(initial=0)
    time_spent_pg_intro = models.FloatField(initial=0)
    time_spent_pd_intro = models.FloatField(initial=0)
    time_spent_me_intro = models.FloatField(initial=0)
    
    
# Pages
class intro1(Page):
    pass

class infoSheet2(Page):
    pass

class consentForm3(Page):
    def vars_for_template(self):
        return {
            'next': 'I Give My Consent'
        }

class participantType4(Page):
    form_model = 'player'
    form_fields = ['participant_type', 'fictitious_name', 'prolific_id']

    def before_next_page(self, timeout_happened=False):
        redirect_url = 'GamesIntro'
        self.participant.vars['redirect_url'] = redirect_url

    def vars_for_template(self):
        return {
            'next': 'Next'
        }

    def error_message(self, values):
        if values['participant_type'] == 'student' and not values['fictitious_name']:
            return 'Please enter your fictitious name.'
        if values['participant_type'] == 'prolific' and not values['prolific_id']:
            return 'Please enter your Prolific ID.'


class gamesIntro5(Page):
    def vars_for_template(self):
        return {}

    # def before_next_page(self, timeout_happened=False):
    #     # Retrieve the 'time_spent' value from the POST data
    #     time_spent = float(self.participant.vars.get('time_spent_games_intro', 0))
    #     self.player.time_spent_games_intro = time_spent
    #     self.player.save()

# class PGIntro(Page):
#     def vars_for_template(self):
#         return {}

#     # def before_next_page(self, timeout_happened=False):
#     #     # Retrieve the 'time_spent' value from the participant's vars
#     #     time_spent = float(self.participant.vars.get('time_spent_pg_intro', 0))
#     #     self.player.time_spent_pg_intro = time_spent
#     #     self.player.save()

# class PDIntro(Page):
#     def is_displayed(self):
#         return self.round_number == 1

#     def vars_for_template(self):
#         return {}

    # def before_next_page(self, timeout_happened=False):
    #     # Retrieve the 'time_spent' value from the participant's vars
    #     time_spent = float(self.participant.vars.get('time_spent_pd_intro', 0))
    #     self.player.time_spent_pd_intro = time_spent
    #     self.player.save()

# class MEIntro(Page):
#     def is_displayed(self):
#         return self.round_number == 1

#     def vars_for_template(self):
#         return {}

    # def before_next_page(self, timeout_happened=False):
    #     # Retrieve the 'time_spent' value from the participant's vars
    #     time_spent = float(self.participant.vars.get('time_spent_me_intro', 0))
    #     self.player.time_spent_me_intro = time_spent
    #     self.player.save()



page_sequence = [
    intro1, 
    infoSheet2, 
    consentForm3, 
    participantType4, 
    gamesIntro5
    ]
