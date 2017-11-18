import numpy as np
import skfuzzy

# speed_range = np.arange(0, 3.05, 0.01)
# speed_high_fx = skfuzzy.trapmf(speed_range, [1, 2, 3, 3])
# slice_value = 1
# speed_high_active_slice = np.fmin(slice_value, speed_high_fx)
# check_point = skfuzzy.interp_membership(speed_range, speed_high_active_slice, 1.375)
# defuzz_value = skfuzzy.defuzz(speed_range, speed_high_active_slice, 'centroid')
speed_range = np.arange(0, 2.01, 0.01)
speed_high_fx = skfuzzy.trimf(speed_range, [1, 2, 2])
slice_value = 1
speed_high_active_slice = np.fmin(slice_value, speed_high_fx)
check_point = skfuzzy.interp_membership(speed_range, speed_high_active_slice, 1.375)
defuzz_value = skfuzzy.defuzz(speed_range, speed_high_active_slice, 'centroid')
pass
