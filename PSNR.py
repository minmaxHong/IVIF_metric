import numpy as np

def PSNR(vis, ir, fusion):
    h, w = vis.shape
    scale = h * w
    
    MSE_VF = np.sum((fusion - vis) ** 2) / scale # MSE(Vis, Fusion)
    MSE_IF = np.sum((fusion - ir) ** 2) / scale # MSE(Ir, Fusion)
    
    MSE = 0.5 * MSE_VF + 0.5 * MSE_IF
    
    _PSNR = 20 * np.log10(255 / np.sqrt(MSE))
    return _PSNR