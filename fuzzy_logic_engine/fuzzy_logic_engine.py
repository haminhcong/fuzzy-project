from . import data_input

from fuzzy_logic_engine.rule import rule_processing
from fuzzy_logic_engine.defuzzification.speed_calculator import defuzz_speed
from fuzzy_logic_engine.fuzzification import \
    angle as angle_fuzzification, \
    distance as distance_fuzzification, \
    lamp_state as lamp_state_fuzzification


def set_speed(ahead_thing=None, distance=None, angle=None,
              lamp_state=None, lamp_time_remaining=None):
    print('')
    print('----:start fuzzy logic engine:----')
    print('data input:----')
    print("ahead_thing: " + ahead_thing)
    print("distance: " + str(distance))
    print("angle: " + str(angle))
    print("lamp_state: " + str(lamp_state))
    print("lamp_time_remaining: " + str(lamp_time_remaining))
    print('//data input:----')
    if ahead_thing == data_input.TRAFFIC_LAMP:
        return traffic_lamp_fuzzy_engine(lamp_state, lamp_time_remaining, distance, angle)
    elif ahead_thing == data_input.BARRIER:
        return barrier_fuzzy_engine(distance, angle)


def traffic_lamp_fuzzy_engine(
        lamp_state=None, lamp_time_remaining=None, distance=None, angle=None):
    lamp_state_fuzzy_value_list = \
        lamp_state_fuzzification.fuzzify_lamp_state_value(lamp_state, lamp_time_remaining)
    distance_fuzzy_value_list = \
        distance_fuzzification.fuzzify_distance_value(distance)
    angle_fuzzy_value_list = \
        angle_fuzzification.fuzzify_angle_value(angle)

    print('----:start fuzzy set lamp engine input:----')
    print("lamp_state: ")
    print(lamp_state_fuzzy_value_list)
    print("distance: ")
    print(distance_fuzzy_value_list)
    print("angle: ")
    print(angle_fuzzy_value_list)

    speed_total = 0
    weight_total = 0
    for distance_fuzzy_value in distance_fuzzy_value_list:
        for lamp_state_fuzzy_value in lamp_state_fuzzy_value_list:
            for angle_fuzzy_value in angle_fuzzy_value_list:
                speed_fuzzy_set_name, slice_value = rule_processing.resolver_lamp_rule(
                    distance_fuzzy_value, lamp_state_fuzzy_value, angle_fuzzy_value)
                defuzz_speed_arg = defuzz_speed(speed_fuzzy_set_name, slice_value)
                print('active fuzzy functions:' +
                      'distance: ' + str(distance_fuzzy_value) + '-' +
                      'lamp: ' + str(lamp_state_fuzzy_value) + ' - ' +
                      'angle: ' + str(angle_fuzzy_value))
                print('speed rule mean: ' + str(speed_fuzzy_set_name) + '-' + str(slice_value))
                print('defuzz speed: ' + str(defuzz_speed_arg) + ' - factor: ' + str(slice_value))
                speed_total += defuzz_speed_arg * slice_value
                weight_total += slice_value
                print()
    print("Total: ", speed_total, weight_total)
    speed_average = round(speed_total / weight_total, 2)
    print('output speed: ' + str(speed_average))
    print('!!=-- end fuzzy set lamp engine process:----')
    print('----:end fuzzy logic engine:----')
    print('')
    return speed_average


def barrier_fuzzy_engine(distance=None, angle=None):
    distance_fuzzy_value_list = \
        distance_fuzzification.fuzzify_distance_value(distance)
    angle_fuzzy_value_list = \
        angle_fuzzification.fuzzify_angle_value(angle)

    print('----:start fuzzy set barrier engine input:----')
    print("distance: ")
    print(distance_fuzzy_value_list)
    print("angle: ")
    print(angle_fuzzy_value_list)

    speed_total = 0
    weight_total = 0
    for distance_fuzzy_value in distance_fuzzy_value_list:
        for angle_fuzzy_value in angle_fuzzy_value_list:
            speed_fuzzy_set_name, slice_value = rule_processing.resolver_barrier_rule(
                distance_fuzzy_value, angle_fuzzy_value)
            defuzz_speed_arg = defuzz_speed(speed_fuzzy_set_name, slice_value)
            print('active fuzzy functions:' +
                  'distance: ' + str(distance_fuzzy_value) + '-' +
                  'angle: ' + str(angle_fuzzy_value))
            print('speed rule mean: ' + str(speed_fuzzy_set_name) + '-' + str(slice_value))
            print('defuzz speed: ' + str(defuzz_speed_arg) + ' - factor: ' + str(slice_value))
            speed_total += defuzz_speed_arg * slice_value
            weight_total += slice_value
            print()
    print("Total: ", speed_total, weight_total)
    speed_average = round(speed_total / weight_total, 2)
    print('output speed: ' + str(speed_average))
    print('!!=-- end fuzzy set lamp engine process:----')
    print('----:end fuzzy logic engine:----')
    print('')
    return speed_average
