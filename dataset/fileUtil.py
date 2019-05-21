# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 23:34
# @Author  : zhangyx
# @FileName: fileUtil.py
# @Software: PyCharm

'''
fileUtil.py用于清洗数据，输入格式可以是字符串、字符串列表、文件。其对应的model参数分别�?string','list','file�?
'''

import os
import re
import astor
#数据文件夹路�?
filePath='dataset\\preprocessed\\'
#合并后的数据文件保存路径
savePath='D:\\nlp\\codeCom\\datagit\\'
#合并后的数据文件名称
saveFile='merge.txt'
isExists=os.path.exists(savePath)
if not isExists:
    os.makedirs(savePath)
'''
将文件夹内的文件合并成一个文�?
'''
def merge_data(filePath,saveFile):
    for filename in os.listdir(filePath):
        with open(filePath + filename, 'r', encoding="utf-8") as file:
            data = file.read()
            with open(saveFile, 'a', encoding="utf-8") as f:
                f.write(data)
    return

'''
去除输入中的非ASCII字符（可以去掉中文等非英文字符）
'''
def onlyASCII(data,model='string'):
    def innerOnlyASCII(data_str):
        # 用utf-8解码再用ascii编码，设置模式为'ignore'，即忽略不能转换的字�?
        return data_str.encode("utf-8").decode("ascii", 'ignore')
    if model=='file':
        if not (isinstance(data, str) and '.txt' in data):
            #抛出异常
            raise Exception("请输�?txt文件或字符串或列�?)
        with open(data, 'r', encoding="utf-8") as f:
            data_str=innerOnlyASCII(f.read())
        return data_str
    elif model=='string':
        data_str=innerOnlyASCII(data)
        return data_str
    elif model=='list':
        data_list=[]
        for item in data:
            data_str = innerOnlyASCII(item)
            data_list.extend(data_str)
        return data_list
    else:
        raise Exception("请输�?txt文件或字符串或列�?)

'''
删除注释
'''
def deleteComment(data,model='string'):
    def innerDelCom(data):
        p0 = re.compile(u"(#.*)?", re.M)
        data1 = re.sub(p0, "", data)
        p1 = re.compile(u"('''.*?''')", re.S)
        data1 = re.sub(p1, "", data1)
        p2 = re.compile(u'(""".*?""")', re.S)
        return re.sub(p2, "", data1)
        # return data

    if model=='file':
        if not (isinstance(data, str) and '.txt' in data):
            raise Exception("请输�?txt文件或字符串或列�?)
        with open(data, 'r', encoding="utf-8") as f:
            dataStr = f.read()
            dataStr=innerDelCom(dataStr)
            # print(dataStr)
        return dataStr
    elif model=='string':
        innerDelCom(data)
        data=innerDelCom(data)
        # print(data)
        return data
    elif model=='list':
        data_list=[]
        for item in data:
            data_list.extend(innerDelCom(item))
        # print(data_list)
        return data_list
    else:
        raise Exception("model值错�?)

'''
删除Print语句，适用于python3
'''
def deletePrint(data,model='string'):
    def innerDelPrt(data):
        p0 = re.compile(u"print\(.*?\)", re.M)
        return re.sub(p0, "", data)
    if model=='file':
        if not (isinstance(data, str) and '.txt' in data):
            raise Exception("请输�?txt文件或字符串或列�?)
        with open(data, 'r', encoding="utf-8") as f:
            dataStr = f.read()
            new=innerDelPrt(dataStr)
            # print(new)
        return new
    elif model=='string':
        data_str=innerDelPrt(data)
        return data_str
    elif model=='list':
        data_list=[]
        for item in data:
            data_str = innerDelPrt(item)
            data_list.extend(data_str)
        return data_list
    else:
        raise Exception("model参数错误")

'''
多行转一�?
'''
def mult2one(data,model='string'):
    def innerMlt(data):
        p0 = re.compile(".(?<=[(])[^)]\n", re.M)
        data = re.sub(p0, "", data)
        p1=re.compile("[([{](.*\r\n.*)", re.S)
        temp=re.findall(p1,data)
        for item in temp:
            s1=item.replace('\r\n','')
            data=data.replace(item,s1)
        return data
    if model=='file':
        if not (isinstance(data, str) and '.txt' in data):
            raise Exception("请输�?txt文件或字符串或列�?)
        with open(data, 'r', encoding="utf-8") as f:
            dataStr = f.read()
            new=innerMlt(dataStr)
        return new
    elif model=='string':
        data_str=innerMlt(data)
        return data_str
    elif model=='list':
        data_list=[]
        for item in data:
            data_str = innerMlt(item)
            data_list.extend(data_str)
        return data_list
    else:
        raise Exception("model参数错误")

'''
删除参数
'''
def deleteParement(data,model='string'):
    def innerDelPmt(data):
        p0 = re.compile(u".*\((.*)=(.*)?\)", re.S)
        string = re.search(p0, data)
        if string == None:
            return data
        print(string)
        str_list = string.group().split(',')
        result = ''
        for item in str_list:
            p1 = re.compile(u"=(.*)", re.S)
            data = re.sub(p1, "= ", item)
            result = result + data + ','
        result = result[:-1] + ' )'
        print(result)
        return result
    if model=='file':
        if not (isinstance(data, str) and '.txt' in data):
            raise Exception("请输�?txt文件或字符串或列�?)
        with open(data, 'r', encoding="utf-8") as f:
            dataStr = f.read()
            new=innerDelPmt(dataStr)
            print(new)
        return new
    elif model=='string':
        data_str=innerDelPmt(data)
        return data_str
    elif model=='list':
        data_list=[]
        for item in data:
            data_str = innerDelPmt(item)
            data_list.extend(data_str)
        return data_list
    else:
        raise Exception("model参数错误")

'''
标记缩进，标记符为IDT
'''
def matchIdentation(data,model='string'):
    def innerIdt(data):
        p0 = re.compile(u" {4}", re.M)
        return  re.sub(p0, " IDT ",data)
    if model=='file':
        if not (isinstance(data, str) and '.txt' in data):
            raise Exception("请输�?txt文件或字符串或列�?)
        with open(data, 'r', encoding="utf-8") as f:
            dataStr = f.read()
            new=innerIdt(dataStr)
            print(new)
        return new
    elif model=='string':
        return innerIdt(data)
    elif model=='list':
        data_list=[]
        for item in data:
            data_str = innerIdt(item)
            data_list.extend(data_str)
        return data_list
    else:
        raise Exception("model参数错误")
# def onlyASCII_generator(data_list):
#     for data in data_list:
#         data_str=data.encode("utf-8").decode("ascii", 'ignore')
#         yield data_str

# p0=re.compile(u"\\[.*?]", re.M)
# p1 = re.compile(r"\([^()]*\)", re.M)
# p2=re.compile('[\'\"](.*?)[\'\"]', re.M)
# rep2=" QUOTMARK "
# p3='('
# rep3=" PARELEFT "
# p4=')'
# rep4=" PARERIGHT "
# p5='.'
# rep5=" DOT "
# p6=','
# rep6=" COMMA "
# p7='='
# rep7=' EQUAL '
# p8=':'
# rep8=' COLON '

# temp1 = re.sub(p2, rep2, re.sub(p0, "[]", re.sub(p1, "()", str, count=0, flags=0),
#                                         count=0, flags=0), count=0, flags=0)
# temp2 = temp1.replace(p3, rep3).replace(p4, rep4).replace(p5, rep5).replace(p6, rep6).replace(p7, rep7)\
#     .replace(p8,rep8).replace('\n', ' DOM\n')
# print(temp2)

# #测试代码
# with open(filePath+'0.txt','r',encoding="utf-8") as file:
#     str = file.read()
#     temp1 = re.sub(p2, rep2, re.sub(p0, "[]", re.sub(p1, "()", str, count=0, flags=0),
#                                              count=0, flags=0), count=0, flags=0)
#     temp2=temp1.replace(p4, rep4).replace(p5,rep5).replace(p6,rep6).replace(p7,rep7).replace('\n',' DOM\n')
#     print(temp2)
# data
# str.replace(p2, " quotMark ")
# temp1 =          re.sub(p2, " quotMark ", re.sub(p0, "[]", re.sub(p1, "()", str, count=0, flags=0),
#                                          count=0, flags=0), count=0, flags=0)
# temp2 = re.sub(p6, rep6,
#                re.sub(p5, rep5, re.sub(p4, rep4, re.sub(p3, rep3, temp1, count=0, flags=0),
#                                        count=0, flags=0), count=0, flags=0), count=0, flags=0)
# temp3 = re.sub(p7, rep7, temp2, count=0, flags=0)
# print(re.sub('\n', ' DOM\n',temp3, count=0, flags=0))
# print(str.replace('\n',' DOM\n'))
# mydata='datagit.txt'
if __name__ == '__main__':
    # temp=deletePrint(deleteComment(onlyASCII('datagit.txt',model='file')))
    # temp1=mult2one(temp)
    # temp2=matchIdentation(temp1)
    # with open('train.txt','w',encoding='utf-8') as f:
    #     f.write(temp2)
    # print(mult2one('test.txt','file'))
    with open(saveFile, 'a', encoding="utf-8") as f:
        for filename in os.listdir(filePath):
            with open(filePath + filename, 'r', encoding="utf-8") as file:
                for line in file:
                    temp=deletePrint(onlyASCII(line))
                    temp1=deleteParement(deleteComment(temp))
                    temp2=matchIdentation(temp1)
                    f.write(temp2)


