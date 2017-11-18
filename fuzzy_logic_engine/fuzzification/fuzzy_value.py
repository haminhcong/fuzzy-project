RED_FUZZY_SET = 'Red'
LESS_RED_FUZZY_SET = 'Less_red'
YELLOW_FUZZY_SET = 'Yellow'
LESS_GREEN_FUZZY_SET = 'Less_green'
GREEN_FUZZY_SET = 'Green'

DISTANCE_NEAR = 'Near'
DISTANCE_MEDIUM = 'Medium'
DISTANCE_FAR = 'Far'

ANGLE_SMALL = 'Small'
ANGLE_MEDIUM = 'Medium'
ANGLE_BIG = 'Big'

SPEED_FAST = 'Fast'
SPEED_SLOWER = 'Slower'
SPEED_SLOW = 'Slow'
SPEED_STOP = 'Stop'


class FuzzyValue:
    def __init__(self, fuzzy_set_name, truth_value):
        self.fuzzy_set_name = fuzzy_set_name
        self.truth_value = truth_value

    def __repr__(self):
        return '<FuzzyValue:' + str(self.fuzzy_set_name) + ' - ' + \
               str(self.truth_value) + '> '

# x = FuzzyValue(SPEED_FAST,0.75)
