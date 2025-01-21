import numpy as np

def MSE(vis, ir, fusion):
    h, w = vis.shape
    scale = h * w
    
    MSE_VF = np.sum((fusion - vis) ** 2) / scale
    MSE_IF = np.sum((fusion - ir) ** 2) / scale
    
    MSE = 0.5 * MSE_VF + 0.5 * MSE_IF
    
    return MSE