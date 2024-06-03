# payoff_tables.py

round_1 = {
    'CC': (12, 12),     # Both Cooperate (Increased reward)
    'CD': (-2, 10),     # You Cooperate, Computer Defects
    'DC': (10, -2),     # You Defect, Computer Cooperates
    'DD': (0, 0)        # Both Defect
}

round_2 = {
    'CC': (10, 10),     # Both Cooperate (Increased reward)
    'CD': (-4, 9),      # You Cooperate, Computer Defects
    'DC': (9, -4),      # You Defect, Computer Cooperates
    'DD': (-1, -1)      # Both Defect
}

round_3 = {
    'CC': (7, 7), 
    'CD': (-3, 11),
    'DC': (11, -3),
    'DD': (-2, -2)
}

round_4 = {
    'CC': (5, 5), 
    'CD': (-5, 8), 
    'DC': (8, -5),
    'DD': (-3, -3)
}

round_5 = {
    'CC': (9, 9), 
    'CD': (-1, 12),
    'DC': (12, -1),
    'DD': (1, 1)
}
