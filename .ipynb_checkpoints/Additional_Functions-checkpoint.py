import numpy as np

def temp_ave(T,lat):
    """
    input: temperature distribution array in Kelvin from previous timestep and latitude array in degrees (both of length 91)
    output: average temperature accross the globe in Kelvin (float)
    """
    deg2rad = np.pi/180
    
    denominator = np.sum(np.cos(lat*deg2rad))
    numerator = np.sum(T * np.cos(lat*deg2rad))
    
    Tave = numerator / denominator
    
    return Tave