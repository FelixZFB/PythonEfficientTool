# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2021/1/5 10:39
Desc:
'''

# 文件夹中文件名批量重命名，保留原始文件名部分内容，删除文件名开头部分广告内容
# 比如 [押题微信：1151346968]第7讲-城镇道路路基施工1
# 类似文件，删除]前面的广告部分，重命名后为 第7讲-城镇道路路基施工1

import os

def rename():
    # path为批量文件的文件夹的路径,直接电脑右键复制路径
    path = input("请输入路径(例如D:\\图片\\)：")
    # 文件夹中所有文件的文件名,获取结果是所有文件名的一个列表
    file_names = os.listdir(path)
    # 即文件统一的开头部分，也可以空白
    name = input("请输入文件开头名:")
    # 循环遍历所有文件名，内循环遍历每个文件名的每个字符
    for name in file_names:
        # name是一个字符串，可以遍历，找到]符号的位置
        for s in name:
            if s == ']':
                index_num = name.index(s)  # index_num 为要删除的位置索引
                # 采用字符串的切片方式删除]及其之前的部分，后面部分作为文件名称
                # 索引位置+1以及后面的内容切片取出作为文件新的名词
                os.renames(os.path.join(path, name), os.path.join(path, name[index_num + 1:]))

                break  # 重命名成功，跳出内循环

rename()