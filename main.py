# -*- coding: utf-8 -*-
# @Time    : 2022/5/26 19:09
# @Author   my friend
# @File    : main.py
# @Software: PyCharm

# 这是一个简单的背词器脚本，用来迎接十八周的词根词缀考试.
# 欢迎大家进一步修改同步到github上
# Prof.He给的复习资料的第二第三部分对应项目中的part2.txt和part3.txt
# 请确保它们和main.py在同一文件夹下


import os
import random
import time
# 选择工作模式
while(1):
    print("请输入学习内容：1=100词, 2=词缀，3=词根")
    part_code = input()
    if(part_code=='1'):
        file= open("part1.txt", "r",encoding= "utf-8")
        break
    elif(part_code=='2'):
        file = open("part2.txt", "r", encoding="utf-8")
        break
    elif(part_code=='3'):
        file = open("part3.txt", "r", encoding="utf-8")
        break
    else:
        print("输入无效")
        pass


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
    for i in range(len(list_pre)-1,0, -1):
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
    print("第【"+str(i)+"】号词")
    print("\n————————————\n")
    print("请输入\'"+list_pre[i]+"\'的含义")
    print("\n————————————\n")
    you_ans= input()
    print("\n————————————\n")
    print("答案："+ list_forget[i].replace('\n', ' '))# 去掉换行符
    print("\n————————————\n")
    print("请选择操作：1=收藏该词并继续，2=不收藏并继续，3=结束并导出收藏词")
    save_code=input()
    if(save_code== '1'):
        save_list.append(list_pre[i]+":"+list_forget[i]+" 你的答案："+ you_ans)
    if(save_code== '3'):
        print("已收藏，退出中")
        save_list.append(list_pre[i] + ":" + list_forget[i] + " 你的答案：" + you_ans)
        output_save()
        return 1
    return 0

# 预处理
for line in file:
    # 按照冒号切割
    line_l= line.split(":")
    list_pre.append(line_l[0])
    list_forget.append(":".join(line_l[1:]))

# 选择记词顺序：正序，倒序，乱序
print("请输入学习模式：1=正序，2=倒序，3=乱序")
seq_code= input()
if(seq_code=='1'):
    az()
if(seq_code=='2'):
    za()
if(seq_code=='3'):
    rand()

clr = os.system("cls") # 清屏
print("\n————————————\n")
print("感谢使用 good luck")
print("\n————————————\n")
print("请备份mysave.txt(不然下一次会被清空)")
print("\n————————————\n")

time.sleep(2)



