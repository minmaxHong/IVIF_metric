import numpy as np

def SD(fusion):
    h, w = fusion.shape
    scale = h * w
    u = np.mean(fusion)
    
    SD = np.sqrt(np.sum((fusion - u) ** 2) / scale)
    return SD  