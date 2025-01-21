import numpy as np

def SF(fusion):
    rf = np.diff(fusion, axis=0)
    rf1 = np.sqrt(np.mean(rf**2))
    
    cf = np.diff(fusion, axis=1)
    cf1 = np.sqrt(np.mean(cf**2))
    
    sf = np.sqrt(rf1**2 + cf1**2)
    return sf

