from otree.api import *


# Models

class Constants(BaseConstants):
    name_in_url = 'post_game_questions'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    age = models.StringField(
        choices=[
            'Under 18', '18 - 24', '25 - 34', '35 - 44', '45 - 54',
            '55 - 64', '65 - 74', '75 - 84', '85 or older'
        ],
        widget=widgets.RadioSelect,
        label="What is your age?"
    )
    gender = models.StringField(
        choices=[
            'Male', 'Female', 'Non-binary / third gender', 'Prefer not to say'
        ],
        widget=widgets.RadioSelect,
        label="To which gender do you identify?"
    )
    education = models.StringField(
        choices=[
            'Less than high school', 'High school graduate', 'Some college',
            '2 year degree', '4 year degree', 'Professional degree', 'Doctorate'
        ],
        widget=widgets.RadioSelect,
        label="What is your education level?"
    )
    employment = models.StringField(
        choices=[
            'Employed full time', 'Employed part time', 'Unemployed looking for work',
            'Unemployed not looking for work', 'Retired', 'Student', 'Disabled'
        ],
        widget=widgets.RadioSelect,
        label="What is your employment situation?"
    )
    feelings_towards_algorithms = models.IntegerField(
        label="I trust algorithms to make fair decisions.",
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5]
    )
    alg_unbiased = models.IntegerField(
        label="I believe algorithms can perform better than humans in making unbiased decisions.",
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5]
    )
    alg_comfort = models.IntegerField(
        label="I feel comfortable relying on algorithms for important decisions.",
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5]
    )
    time_well = models.IntegerField(
        label="I perform well when making decisions under time pressure.",
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5]
    )
    time_improve = models.IntegerField(
        label="Time constraints improve my decision-making efficiency.",
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5]
    )
    time_stress = models.IntegerField(
        label="I feel stressed when I have to make decisions quickly.",
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5]
    )
    fair_fair = models.IntegerField(
        label="I believe that decisions made by algorithms are fair.",
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5]
    )
    fair_transparency = models.IntegerField(
        label="I am confident in the transparency of algorithmic decisions.",
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5]
    )
    fair_bias = models.IntegerField(
        label="Algorithms are less likely to be biased compared to human decision-makers.",
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5]
    )

    
# Pages

class GeneralQuestions(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'employment']

    def get_template_name(self):
        return 'GeneralQuestions.html'


class SpecificQuestions(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = [
        'feelings_towards_algorithms', 'alg_unbiased', 'alg_comfort',
        'time_well', 'time_improve', 'time_stress',
        'fair_fair', 'fair_transparency', 'fair_bias'
    ]

    def get_template_name(self):
        return 'SpecificQuestions.html'


page_sequence = [GeneralQuestions, SpecificQuestions]
