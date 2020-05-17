# -*- coding: utf-8 -*-
"""
# @file name  : resnet_inference.py
# @author     : TingsongYu https://github.com/TingsongYu
# @date       : 2019-11-16
# @brief      : inference demo
"""

import os
import time
import torch.nn as nn
import torch
import torchvision.transforms as transforms
from PIL import Image
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import torchvision.models as models

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

norm_mean = [0.485, 0.456, 0.406]
norm_std = [0.229, 0.224, 0.225]

inference_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(norm_mean, norm_std),
])

classes = ["ants", "bees"]


def img_transform(img_rgb, transform=None):
    """
    将数据转换为模型读取的形式
    :param img_rgb: PIL Image
    :param transform: torchvision.transform
    :return: tensor
    """

    if transform is None:
        raise ValueError("找不到transform！必须有transform对img进行处理")

    img_t = transform(img_rgb)
    return img_t


def get_img_name(img_dir, format="jpg"):
    """
    获取文件夹下format格式的文件名
    :param img_dir: str
    :param format: str
    :return: list
    """
    file_names = os.listdir(img_dir)
    img_names = list(filter(lambda x: x.endswith(format), file_names))

    if len(img_names) < 1:
        raise ValueError("{}下找不到{}格式数据".format(img_dir, format))
    return img_names


def get_model(m_path, vis_model=False):
    resnet18 = models.resnet18()
    num_ftrs = resnet18.fc.in_features
    resnet18.fc = nn.Linear(num_ftrs, 2)

    checkpoint = torch.load(m_path)
    resnet18.load_state_dict(checkpoint['model_state_dict'])

    if vis_model:
        from torchsummary import summary
        summary(resnet18, input_size=(3, 224, 224), device="cpu")

    return resnet18


if __name__ == "__main__":
    # 1. data
    img = "bee5.jpg"
    model_path = "checkpoint_14_epoch.pkl"
    time_tic = time.time()

    # 2. model
    resnet18 = get_model(model_path, False)
    resnet18.to(device)
    resnet18.eval()

    with torch.no_grad():
        # step 1/4 : path --> img
        img_rgb = Image.open(img).convert('RGB')

        # step 2/4 : img --> tensor
        img_tensor = img_transform(img_rgb, inference_transform)
        img_tensor.unsqueeze_(0)
        img_tensor = img_tensor.to(device)

        # step 3/4 : tensor --> vector
        outputs = resnet18(img_tensor)

        # step 4/4 : visualization
        _, pred_int = torch.max(outputs.data, 1)
        pred_str = classes[int(pred_int)]

        plt.imshow(img_rgb)
        plt.title("predict:{}".format(pred_str))
        # plt.show()
        plt.savefig("../../../../font/media/inference_img/"+img)
        plt.close()

        time_s = time.time() - time_tic

        print("input shape:{}\ntime:{:.3f}s".
              format(img_rgb.size, time_s))


def inference(pic_name,pkl_path):
    # 1. data
    img = pic_name
    print(os.path)
    model_path = pkl_path + "checkpoint_14_epoch.pkl"
    time_tic = time.time()

    # 2. model
    resnet18 = get_model(model_path, False)
    resnet18.to(device)
    resnet18.eval()

    with torch.no_grad():
        # step 1/4 : path --> img
        img_rgb = Image.open(img).convert('RGB')

        # step 2/4 : img --> tensor
        img_tensor = img_transform(img_rgb, inference_transform)
        img_tensor.unsqueeze_(0)
        img_tensor = img_tensor.to(device)

        # step 3/4 : tensor --> vector
        outputs = resnet18(img_tensor)

        # step 4/4 : visualization
        _, pred_int = torch.max(outputs.data, 1)
        pred_str = classes[int(pred_int)]

        plt.imshow(img_rgb)
        plt.title("predict:{}".format(pred_str))
        # plt.show()
        plt.savefig(pic_name)

        plt.close()

        time_s = time.time() - time_tic

        return {"addr":pic_name,"input_shape":img_rgb.size,"time": round(time_s,2)}
