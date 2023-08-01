# from PIL import Image
# import os
# import cv2
# import numpy as np
# '''
# 函 数 名：gaussian_noise(img, mean, sigma)
# 函数功能：添加高斯噪声
# 入口参数：
#         img ：原图
#         mean ：均值
#         sigma ：标准差
# 返 回 值：
#         噪声处理后的图片
# '''
# def gaussian_noise(img, mean, sigma):
#     # 将图片灰度标准化
#     img = (img / 255)
#     # 产生高斯 noise
#     noise = np.random.normal(mean, sigma, img.shape)
#     # 将噪声和图片叠加
#     gaussian_out = img + noise
#     # 将超过 1 的置 1，低于 0 的置 0
#     gaussian_out = np.clip(gaussian_out, 0, 1)
#     # 将图片灰度范围的恢复为 0-255
#     gaussian_out = np.uint8(gaussian_out*255)
#     # 这里也会返回噪声，注意返回值
#     return gaussian_out
# '''
# 函 数 名：motion_blur(image)
# 函数功能：运动模糊化处理
# 入口参数：
#         image ：原图
# 返 回 值：
#         模糊化处理后的图片
# '''
# def motion_blur(image):
#     degree = 15   # 破损，闪络30；掉片15
#     angle = 35
#     image = np.array(image)
#
#     # 这里生成任意角度的运动模糊kernel的矩阵， degree越大，模糊程度越高
#     M = cv2.getRotationMatrix2D((degree / 2, degree / 2), angle, 1)
#     motion_blur_kernel = np.diag(np.ones(degree))
#     motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))
#
#     motion_blur_kernel = motion_blur_kernel / degree
#     blurred = cv2.filter2D(image, -1, motion_blur_kernel)
#
#     # convert to uint8
#     cv2.normalize(blurred, blurred, 0, 255, cv2.NORM_MINMAX)
#     blurred = np.array(blurred, dtype=np.uint8)
#     return blurred
#
#
# '''
# 函 数 名：gauss_fuzzy_convert(input_dir, output_dir)
# 函数功能：将原图进行高斯和模糊化变换
# 入口参数：
#         input_dir ：原图路径
#         output_dir ：变换后路径
# 返 回 值：
#         无
# '''
# def gauss_fuzzy_convert(input_dir, output_dir):
#     for filename in os.listdir(input_dir):
#         path = input_dir + "/" + filename# 获取文件路径
#         fuzzy_image = cv2.imread(path)#读取图片
#         noise_img = cv2.imread(path)#读取图片
#         fuzzy_image_1 = motion_blur(fuzzy_image)
#         noise_img_1 = gaussian_noise(noise_img, 0.1, 0.08) #高斯噪声
#         #cv2.imwrite(output_dir+'/'+filename[:-4] + "noise" + ".jpg",noise_img_1)
#         #cv2.imwrite(output_dir+'/'+filename[:-4] + "fuzzy" + ".jpg",fuzzy_image_1)
#         cv2.imwrite(output_dir + '/' + filename[:-4]  + ".jpg", fuzzy_image_1)
#
#
# Input_dir = r"/workspace/zhaoxyu/yolov7-main/runs/detect/exp52"  # 要改变的图片的路径文件夹
# Output_dir = r"/workspace/zhaoxyu/yolov7-main/runs/detect/exp52"  # 要保存的图片的路径文件夹
#
# for name in os.listdir(Input_dir):
#     saveName= name[:-4]+"original.png"
#     image = Image.open(os.path.join(Input_dir, name))
#     image.save(os.path.join(Output_dir,saveName))#保存原图
#
# ########################添加高斯噪声、运动模糊处理#######################
#     gauss_fuzzy_convert(Input_dir, Output_dir)
from PIL import Image
from PIL import ImageEnhance
import os

from PIL import Image
from PIL import ImageEnhance
import os
import cv2
import numpy as np
'''
函 数 名：brightnessEnhancement(root_path,img_name,brightness)
函数功能：亮度增强
入口参数：
        root_path ：图片根目录
        img_name ：图片名称
        brightness ：亮度
返 回 值：
        亮度增强后的图片
'''
def brightnessEnhancement(root_path,img_name,brightness):
    image = Image.open(os.path.join(root_path, img_name))
    enh_bri = ImageEnhance.Brightness(image)
    image_brightened = enh_bri.enhance(brightness)
    return image_brightened


Input_dir = r"/workspace/sxk/yolov5-master/my_yolo_dataset2/val/images"  # 要改变的图片的路径文件夹
Output_dir = r"/workspace/sxk/yolov5-master/my_yolo_dataset2/val/imagesjialiang/"  # 要保存的图片的路径文件夹

for name in os.listdir(Input_dir):
    saveName= name[:-4]+"original.png"
    image = Image.open(os.path.join(Input_dir, name))
    #image.save(os.path.join(Output_dir,saveName))#保存原图

######################亮度增强#######################
    for i in range(5, 16, 10):
        i_int = i / 10# range()的传入参数只能是int类型，使用i与i_int做转换
        #saveName= name[:-4]+"bright" + str(i_int) + ".jpg"
        saveName = name[:-4] + ".jpg"
        saveImage=brightnessEnhancement(Input_dir,name,i_int)
        saveImage.save(os.path.join(Output_dir,saveName))
