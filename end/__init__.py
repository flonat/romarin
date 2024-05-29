from otree.api import *
import random
c = cu
doc = ''

# Models

class Constants(BaseConstants):
    name_in_url = 'end'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass


# Pages
class EndPage(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        # Determine if the participant is a Prolific user
        is_prolific_user = self.participant.vars.get('participant_type') == 'prolific'
        return {
            'is_prolific_user': is_prolific_user,
            'prolific_completion_code': 'XXXXXX'  # Replace with your actual completion code
        }


page_sequence = [EndPage]