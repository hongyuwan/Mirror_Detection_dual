"""
  @Time    : 2021-1-17 23:46
  @Author  : Why
  @Email   : hongyuwan@hotmail.com

  @Project : final
 @File    : compute_size.py
 @Function: compute mirror area distribution.
 
"""
import os
import numpy as np
import skimage.io
from misc import data_write

image_path = '/Users/wanhongyu/Documents/Mirror_Detection_infer/MSD/all_images/'
mask_path = '/Users/wanhongyu/Documents/Mirror_Detection_infer/MSD/all_masks/'

imglist = os.listdir(image_path)
print(len(imglist))

output = []

for i, imgname in enumerate(imglist):
    print(i, imgname)
    name = imgname.split('.')[0]

    mask = skimage.io.imread(mask_path + name + '.png')
    mask = np.where(mask != 0, 1, 0).astype(np.uint8)

    height = mask.shape[0]
    width = mask.shape[1]
    total_area = height * width
    if total_area != 640*512:
        print('size error!')

    mirror_area = np.sum(mask)
    proportion = mirror_area / total_area
    output.append(proportion)
data_write(os.path.join(os.getcwd(), 'msd_size.xlsx'), [output])