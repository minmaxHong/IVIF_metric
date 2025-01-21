import numpy as np

def AG(fusion):
    if fusion.ndim == 2:
        fusion = fusion[:, :, np.newaxis]
    
    fusion = fusion.astype(np.float64)
    h, w, c = fusion.shape
    
    gradients = []
    for k in range(c):
        band = fusion[:, :, k]
        
        dzdx = np.gradient(band, axis=1)
        dzdy = np.gradient(band, axis=0)
        
        magnitude = np.sqrt((dzdx**2 + dzdy ** 2) / 2)
        gradients.append(np.sum(magnitude) / ((h - 1) * (w - 1)))
    
    output = np.mean(gradients)    
    return output