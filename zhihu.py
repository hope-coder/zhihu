#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 11:22
# @Author  : ZWP
# @File    : zhihu.py

from bs4 import BeautifulSoup
import requests
from skimage import io
import os


def getZhiHuImg(question_url, file_dir='./pic/', show=False):
    """
       question_url: 想要爬取的url地址
       file_dir: 图片的保存路径
       show：是否在爬取过程中显示图片

    """
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)

    url = question_url

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'
    }

    response = requests.get(url=url, headers=headers)

    question = BeautifulSoup(response.text, "html.parser")

    img_list = question.select("figure > img")

    for index, img in enumerate(img_list):
        if img.has_attr('data-original'):
            print(img['data-original'])
            image = requests.get(img['data-original'])
            with open(file_dir + str(index) + '.jpg', "wb") as f:  # 保存的文件名 保存的方式（wb 二进制  w 字符串）
                f.write(image.content)
                if show:
                    image = io.imread(file_dir + str(index) + '.jpg')
                    io.imshow(image)
                    io.show()


if __name__ == '__main__':
    getZhiHuImg("https://www.zhihu.com/question/351508369", file_dir="./pic/", show=True)
