# -*- coding: utf-8 -*-
"""
# @file name  : seg_demo.py
# @author     : TingsongYu https://github.com/TingsongYu
# @date       : 2019-11-22
# @brief      : torch.hub调用deeplab-V3进行图像分割
"""

import os
import time
import torch.nn as nn
import torch
import numpy as np
import torchvision
import torchvision.transforms as transforms
from PIL import Image
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# appendix
classes = ['__background__',
           'aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor']


def resnet101(pic_name, pkl_path):
    # config
    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # 1. load data & model
    tic = time.time()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    input_image = Image.open(pic_name).convert("RGB")
    model = torch.hub.load('pytorch/vision', 'deeplabv3_resnet101', pretrained=False)
    dict_ = torch.load(pkl_path + 'deeplabv3_resnet101_coco-586e9e4e.pth')
    list_ = []
    for t in dict_.keys():
        if t[:4] == 'aux_':
            list_.append(t)
    for t in list_:
        dict_.pop(t)
    model.load_state_dict(dict_)
    model.eval()

    # 2. preprocess
    input_tensor = preprocess(input_image)
    input_bchw = input_tensor.unsqueeze(0)

    # 3. to device
    if torch.cuda.is_available():
        input_bchw = input_bchw.to('cuda')
        model.to('cuda')

    # 4. forward
    with torch.no_grad():
        output_4d = model(input_bchw)['out']
        output = output_4d[0]
    output_predictions = output.argmax(0)

    # 5. visualization
    palette = torch.tensor([2 ** 25 - 1, 2 ** 15 - 1, 2 ** 21 - 1])
    colors = torch.as_tensor([i for i in range(21)])[:, None] * palette
    colors = (colors % 255).numpy().astype("uint8")

    # plot the semantic segmentation predictions of 21 classes in each color
    r = Image.fromarray(output_predictions.byte().cpu().numpy()).resize(input_image.size)
    r.putpalette(colors)
    plt.imshow(r)
    pic_out = pic_name[:-4] + '_out.jpg'
    plt.savefig(pic_out)

    plt.close()

    return {"addr": pic_out, "input_shape": str(input_bchw.shape)[11:-1],
            "output_shape": str(output.shape)[11:-1], "time": round(time.time() - tic, 2)}


if __name__ == "__main__":
    print(resnet101('demo_img1.png', './'))