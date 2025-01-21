import cv2
import numpy as np
import os
import pandas as pd

from PSNR import PSNR
from MSE import MSE
from EN import EN
from SF import SF
from SD import SD
from CC import CC
from AG import AG

def evaluation(vis, ir, fusion):
    _PSNR = PSNR(vis, ir, fusion)
    _MSE = MSE(vis, ir, fusion)
    _CC = CC(vis, ir, fusion)
    _SF = SF(fusion)
    _SD = SD(fusion)
    _EN = EN(fusion)
    _AG = AG(fusion)
    return _PSNR, _MSE, _SF, _SD, _EN, _CC, _AG


def load_images(vis_path, ir_path, fusion_path):
    vis_images = sorted(os.listdir(vis_path))
    ir_images = sorted(os.listdir(ir_path))
    fusion_images = sorted(os.listdir(fusion_path))

    columns = ["PSNR", "MSE", "SF", "SD", "EN", "CC", "AG"]
    
    _PSNR_SUM = 0
    _MSE_SUM = 0
    _SF_SUM = 0
    _SD_SUM = 0
    _EN_SUM = 0
    _CC_SUM = 0
    _AG_SUM = 0
    for i in range(len(vis_images)):
        vis_image = cv2.imread(os.path.join(vis_path, vis_images[i]))
        ir_image = cv2.imread(os.path.join(ir_path, ir_images[i]))
        fusion_image = cv2.imread(os.path.join(fusion_path, fusion_images[i]))
        
        # print(vis_image.shape, ir_image.shape, fusion_image.shape)
        
        gray_vis_image = cv2.cvtColor(vis_image, cv2.COLOR_BGR2GRAY)
        gray_ir_image = cv2.cvtColor(ir_image, cv2.COLOR_BGR2GRAY)
        gray_fusion_image = cv2.cvtColor(fusion_image, cv2.COLOR_BGR2GRAY)
        
        # cv2.imshow("fusion_image", gray_fusion_image)
        # cv2.waitKey(0)
        
        _PSNR, _MSE, _SF, _SD, _EN, _CC, _AG = evaluation(gray_vis_image, gray_ir_image, gray_fusion_image)
        _PSNR_SUM += _PSNR
        _MSE_SUM += _MSE
        _SF_SUM += _SF
        _SD_SUM += _SD
        _EN_SUM += _EN
        _CC_SUM += _CC
        _AG_SUM += _AG
    
    avg_PSNR = _PSNR_SUM / len(vis_images)
    avg_MSE = _MSE_SUM / len(vis_images)
    avg_SF = _SF_SUM / len(vis_images)
    avg_SD = _SD_SUM / len(vis_images)
    avg_EN = _EN_SUM / len(vis_images)
    avg_CC = _CC_SUM / len(vis_images)
    avg_AG = _AG_SUM / len(vis_images)
    
    print("-"*20)
    print("PSNR: ", avg_PSNR)
    print("MSE: ", avg_MSE)
    print("SF: ", avg_SF)
    print("SD: ", avg_SD)
    print("EN: ", avg_EN)
    print("CC: ", avg_CC)
    print("AG: ", avg_AG)
    print("-"*20)
    
    avg_values = pd.DataFrame([[avg_PSNR, avg_MSE, avg_SF, avg_SD, avg_EN, avg_CC, avg_AG]], columns=columns)
    # avg_values.to_csv("model_second_try.csv", index=False)

vis_path = r'C:\Users\USER\Desktop\code\IVIF_metric\TNO_42\vi'
ir_path = r'C:\Users\USER\Desktop\code\IVIF_metric\TNO_42\ir'
fusion_path = r'C:\Users\USER\Desktop\second_model_outputs'

load_images(vis_path, ir_path, fusion_path)