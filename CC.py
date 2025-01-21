import numpy as np

def CC(vis, ir, fusion):
    vis_mean = np.mean(vis)
    ir_mean = np.mean(ir)
    fusion_mean = np.mean(fusion)
    
    rAF = np.sum((vis-vis_mean) * (fusion-fusion_mean)) / np.sqrt(np.sum((vis-vis_mean)**2) * np.sum((fusion-fusion_mean)**2))
    rBF = np.sum((ir-ir_mean) * (fusion-fusion_mean)) / np.sqrt(np.sum((ir-ir_mean)**2) * np.sum((fusion-fusion_mean)**2))
    
    return (rAF + rBF) / 2    
