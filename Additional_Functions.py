import numpy as np

def temp_ave(T):
    """
    input: temperature distribution array in Kelvin from previous timestep and latitude array in degrees      (both of length 91)
    output: average temperature accross the globe in Kelvin (float)
    """
    lat = np.arange(0, 91, 1)
    deg2rad = np.pi/180
    
    denominator = np.sum(np.cos(lat*deg2rad))
    numerator = np.sum(T * np.cos(lat*deg2rad))
    
    Tave = numerator / denominator
    
    return Tave


def create_interp_T(lat):
    """
    Input: takes in the lat array.
    Output: spits out the interpolated temperature array
    """
    table_Ti = np.array([26.4, 26.1, 22.9, 16.2, 8.8, 2.2, -5.1, -12.3, -16.9])
    table_lats = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    return np.interp(lat, table_lats, table_Ti)


def create_interp_solar(lat):
    """
    Input: takes in the lat array.
    Output: spits out the interpolated solar insolation array
    """
    deg2rad = np.pi/180
    s_i = 1366

    table_solar_fractions = np.array([1.219, 1.189, 1.120, 1.021, 0.892, 0.770, 0.624, 0.531, 0.500])
    table_lats = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    interp_solar_fractions = np.interp(lat, table_lats, table_solar_fractions)

    interp_solar_insolation = (s_i/4)*interp_solar_fractions

    return interp_solar_insolation

def create_interp_albedo(lat):
    """
    Input: takes in the lat array.
    Output: spits out the interpolated solar insolation array
    """
    table_albedo = np.array([0.254, 0.248, 0.272, 0.309, 0.357, 0.407,0.452, 0.544, 0.589])
    table_lats = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    return np.interp(lat, table_lats, table_albedo)
    