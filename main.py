# -*- coding: utf-8 -*-
# @Time    : 2022/5/26 19:09
# @Author   Zhou Yiqun,CS,CQU
# @File    : main.py
# @Software: PyCharm
import os
import random

# 选择工作模式
while(1):
    print("请输入学习内容：1=词缀，2=词根")
    part_code = input()
    if(part_code=='1'):
        file= open("part2.txt", "r",encoding= "utf-8")
        break
    elif(part_code=='2'):
        file = open("part3.txt", "r", encoding="utf-8")
        break
    else:
        print("输入无效")
        pass

# TODO 顺序出现左边的词。 下面一行用来输入。输入完之后可以对比。 也可以直接对比. 支持导出不熟悉的词。
# 读取前缀和含义，分别保存，以i作为下标
list_pre=[] # 前缀
list_forget=[] # 含义和例子
save_list=[] # 收藏词

# 输出收藏词到文档
def output_save():
    savefile= open("mysave.txt", 'w',encoding="utf-8")
    for item in save_list:
        item= item.replace("\n", " ")
        item= item+ "\n"
        savefile.write(item)

# 顺序记词
def az():
    for i in range(len(list_pre)):
        exit_code= user_inter(i)
        if(exit_code):
            break

# 倒序记词
def za():
    for i in range(len(list_pre),0, -1):
        exit_code= user_inter(i)
        if(exit_code):
            break

# 乱序记词
def rand():
    randlist=random.sample(range(0, len(list_pre)), len(list_pre))
    for i in randlist:
        exit_code= user_inter(i)
        if(exit_code):
            break

# 每一个词的用户交互
def user_inter(i):
    clr = os.system("cls") # 清屏
    print("请输入\'"+list_pre[i]+"\'的含义")
    you_ans= input()
    print("你的答案："+you_ans)
    print("Prof.He的答案："+ list_forget[i])
    print("按1收藏该词并继续，按2不收藏并继续，按3结束并导出收藏词")
    save_code=input()
    if(save_code== '1'):
        save_list.append(list_pre[i]+":"+list_forget[i]+" 你的答案："+ you_ans)
    if(save_code== '3'):
        save_list.append(list_pre[i] + ":" + list_forget[i] + " 你的答案：" + you_ans)
        output_save()
        return 1
    return 0

# 预处理
for line in file:
    # 按照冒号切割
    line_l= line.split(":")
    list_pre.append(line_l[0])
    list_forget.append(line_l[1])

# 选择记词顺序：正序，倒序，乱序
print("请输入学习模式：1=正序，2=倒序，3=乱序")
seq_code= input()
if(seq_code=='1'):
    az()
if(seq_code=='2'):
    za()
if(seq_code=='3'):
    rand()
print("感谢使用 考试加油 请备份mysave.txt(不然下一次会被清空)")






