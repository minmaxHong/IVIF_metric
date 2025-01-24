import numpy as np
from EN import EN

def hab(grey_matrix1, grey_matrix2, grey_level):
    joint_hist, _, _ = np.histogram2d(
        grey_matrix1.ravel(), grey_matrix2.ravel(), bins=grey_level, range=[[0, grey_level], [0, grey_level]]
    )
    joint_prob = joint_hist / np.sum(joint_hist)  
    joint_prob = joint_prob[joint_prob > 0]  
    return -np.sum(joint_prob * np.log2(joint_prob))

def MI(vis, ir, fusion, grey_level=256):
    HA = EN(vis)
    HB = EN(ir)
    HF = EN(fusion)
    HFA = hab(fusion, vis, grey_level)
    HFB = hab(fusion, ir, grey_level)
    MIFA = HA + HF - HFA
    MIFB = HB + HF - HFB
    return MIFA + MIFB