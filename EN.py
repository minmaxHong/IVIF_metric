import numpy as np

def EN(fusion):
    fusion = fusion.astype(np.uint8)
    
    hist, _ = np.histogram(fusion.flatten(), bins=256, range=(0, 256), density=True)
    hist = hist[hist>0]
    
    E = -np.sum(hist * np.log2(hist))
    return E
        