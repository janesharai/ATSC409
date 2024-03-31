import numpy as np

def temp_ave(T,lat):
    """
    input: temperature distribution array in Kelvin from previous timestep and latitude array in degrees      (both of length 91)
    output: average temperature accross the globe in Kelvin (float)
    """
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
    