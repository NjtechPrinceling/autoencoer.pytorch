from torch.utils.tensorboard import SummaryWriter
from torchvision.utils import make_grid
import torch
import numpy as np


class Writer():
    def __init__(self, log_dir='./runs/mnist'):
        self.writer = SummaryWriter(log_dir=log_dir)

    def add_images(self, tag, images, logits, nums=10):
        assert len(images) == len(logits)
        length = len(images)
        assert length >= nums
        imglist = []
        for i in range(nums):
            imglist.append(images[i])
            imglist.append(logits[i])
        img_grid = make_grid(imglist)
        self.writer.add_image(tag=tag, img_tensor=img_grid)

    def close(self):
        self.writer.close()