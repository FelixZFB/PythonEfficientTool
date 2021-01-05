# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2021/1/5 10:57
Desc:
'''
# 批量自定义重命名文件,按数字编号增加重命名

import os
def rename():
    # path为批量文件的文件夹的路径,直接电脑右键复制路径
    path = input("请输入路径(例如D:\\图片\\)：")
    name=input("请输入开头名:")
    startNumber=input("请输入开始数:")
    fileType=input("请输入后缀名（如 .jpg、.txt等等）:")
    print("正在生成以"+name+startNumber+fileType+"迭代的文件名")
    count=0
    file_names=os.listdir(path)
    for files in file_names:
        Olddir=os.path.join(path,files)
        if os.path.isdir(Olddir):
            continue
        Newdir=os.path.join(path,name+str(count+int(startNumber))+fileType)
        os.rename(Olddir,Newdir)
        count+=1
    print("一共修改了"+str(count)+"个文件")

rename()