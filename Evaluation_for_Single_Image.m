clc;
clear all;

easy = 0; % easy=1: EN, SF, SD, PSNR, MSE, MI, VIF, AG, CC, SCD, Qabf 등의 지표 계산
          % easy=0: Nabf, SSIM, MS_SSIM, FMI_pixel, FMI_dct, FMI_w 등의 지표 계산


source_folder_ir = '..\Image\Source-Image\TNO\ir\';
source_folder_vi = '..\Image\Source-Image\TNO\vi\'; 
fused_folder = 'C:/Users/USER/Desktop/IVIF_model_fusion_output/CMTFusion/TNO_42/';

ir_files = dir(fullfile(source_folder_ir, '*.png'));
vi_files = dir(fullfile(source_folder_vi, '*.png'));
fused_files = dir(fullfile(fused_folder, '*.png'));


num_images = min([length(ir_files), length(vi_files), length(fused_files)]);


EN_all = []; SF_all = []; SD_all = []; PSNR_all = []; MSE_all = [];
MI_all = []; VIF_all = []; AG_all = []; CC_all = []; SCD_all = [];
Qabf_all = []; Nabf_all = []; SSIM_all = []; MS_SSIM_all = [];
FMI_pixel_all = []; FMI_dct_all = []; FMI_w_all = [];


for i = 1:num_images
    ir_image_path = fullfile(source_folder_ir, ir_files(i).name);
    vi_image_path = fullfile(source_folder_vi, vi_files(i).name);
    fused_image_path = fullfile(fused_folder, fused_files(i).name);

    ir_image = imread(ir_image_path);
    vi_image = imread(vi_image_path);
    fused_image = imread(fused_image_path);
    
    fprintf('%s\n', repmat('-', 1, 20));
    fprintf('Processing Index: %d\n', i);
    fprintf('IR: %s\n', ir_files(i).name);
    fprintf('VI: %s\n', vi_files(i).name);
    fprintf('Fused: %s\n', fused_files(i).name);
    fprintf('%s\n', repmat('-', 1, 20));

    if size(ir_image, 3) > 2
        ir_image = rgb2gray(ir_image);
    end
    if size(vi_image, 3) > 2
        vi_image = rgb2gray(vi_image);
    end
    if size(fused_image, 3) > 2
        fused_image = rgb2gray(fused_image);
    end
    
    ir_size = size(ir_image);
    vi_size = size(vi_image);
    fusion_size = size(fused_image);
    
    if length(ir_size) < 3 && length(vi_size) < 3
        [EN, SF, SD, PSNR, MSE, MI, VIF, AG, CC, SCD, Qabf, Nabf, SSIM, MS_SSIM, FMI_pixel, FMI_dct, FMI_w] = ...
            analysis_Reference(fused_image, ir_image, vi_image, easy);
        
        EN_all = [EN_all, EN]; SF_all = [SF_all, SF]; SD_all = [SD_all, SD];
        PSNR_all = [PSNR_all, PSNR]; MSE_all = [MSE_all, MSE];
        MI_all = [MI_all, MI]; VIF_all = [VIF_all, VIF];
        AG_all = [AG_all, AG]; CC_all = [CC_all, CC];
        SCD_all = [SCD_all, SCD]; Qabf_all = [Qabf_all, Qabf];
        Nabf_all = [Nabf_all, Nabf]; SSIM_all = [SSIM_all, SSIM];
        MS_SSIM_all = [MS_SSIM_all, MS_SSIM];
        FMI_pixel_all = [FMI_pixel_all, FMI_pixel];
        FMI_dct_all = [FMI_dct_all, FMI_dct];
        FMI_w_all = [FMI_w_all, FMI_w];

    else
        fprintf('Image size mismatch at index %d!\n', i);
    end
end

if easy == 1
    fprintf('Average Results for Easy = 1:\n');
    fprintf('EN = %.4f\n', mean(EN_all));
    fprintf('MI = %.4f\n', mean(MI_all));
    fprintf('SD = %.4f\n', mean(SD_all));
    fprintf('SF = %.4f\n', mean(SF_all));
    fprintf('MSE = %.4f\n', mean(MSE_all));
    fprintf('PSNR = %.4f\n', mean(PSNR_all));
    fprintf('VIF = %.4f\n', mean(VIF_all));
    fprintf('AG = %.4f\n', mean(AG_all));
    fprintf('SCD = %.4f\n', mean(SCD_all));
    fprintf('CC = %.4f\n', mean(CC_all));
    fprintf('Qabf = %.4f\n', mean(Qabf_all));
else
    fprintf('Average Results for Easy = 0:\n');
    fprintf('Nabf = %.4f\n', mean(Nabf_all));
    fprintf('SSIM = %.4f\n', mean(SSIM_all));
    fprintf('MS_SSIM = %.4f\n', mean(MS_SSIM_all));
    fprintf('FMI_pixel = %.4f\n', mean(FMI_pixel_all));
    fprintf('FMI_dct = %.4f\n', mean(FMI_dct_all));
    fprintf('FMI_w = %.4f\n', mean(FMI_w_all));
end
