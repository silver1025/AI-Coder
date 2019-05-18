import os
import re
filePath='D:\\nlp\\codeCom\\datagit\\'
savePath='D:\\nlp\\codeCom\\datagit\\'
isExists=os.path.exists(savePath)
if not isExists:
    os.makedirs(savePath)
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

def merge_data(filePath,saveFile):
    mergeStr = ""
    for filename in os.listdir(filePath):
        with open(filePath + filename, 'r', encoding="utf-8") as file:
            str = file.read()
            mergeStr = mergeStr + str
    with open(saveFile, 'w', encoding="utf-8") as f:
        f.write(mergeStr)
    return

def onlyASCII(data,model='string',outputName='result.txt'):
    if model=='file':
        if not (isinstance(data, str) and '.txt' in data):
            return "请输入.txt文件或字符串或列表"
        with open(data, 'r', encoding="utf-8") as f:
            str = f.read().encode("utf-8").decode("ascii", 'ignore')
        with open(outputName, 'w', encoding="utf-8") as f:
            f.write(str)
        return
    elif model=='string':
        data_str = data.encode("utf-8").decode("ascii", 'ignore')
        return data_str
    elif model=='list':
        data_list=[]
        for item in data:
            data_str = item.encode("utf-8").decode("ascii", 'ignore')
            data_list.extend(data_str)
        return data_list
    else:
        return "请输入.txt文件或字符串或列表"

def onlyASCII_generator(data_list):
    for data in data_list:
        data_str=data.encode("utf-8").decode("ascii", 'ignore')
        yield data_str

def deleteComment(data,model='file'):
    p0=re.compile(u"#.*", re.M)
    data=re.sub(p0, "",data)
    p1=re.compile(u"\\'''.*?'''", re.S)
    data=re.sub(p1, "",data)
    print(data)

def deletePrint(data):
    p0=re.compile(u"print\(.*?\)", re.M)
    data=re.sub(p0, "",data)
    print(data)

def mult2one(data):
    p0=re.compile(u"\\\n", re.M)
    data=re.sub(p0, "",data)
    print(data)

def deleteParement(data):
    p0=re.compile(u"\((.*)=(.*)?\)", re.S)
    string=re.search(p0,data).group()
    print(string)
    str_list=string.split(',')
    result=''
    for itrm in str_list:
        p1 = re.compile(u"=(.*)", re.S)
        data = re.sub(p1, "= ", itrm)
        result=result+data+','
    result=result[:-1]+' )'
    print(result)




def matchIdentation(data):
    p0=re.compile(u"\(.*?\)", re.M)
    data=re.sub(p0, " IDT ",data)
    print(data)



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

if __name__ == '__main__':
    pass
    str1="def onlyASCII(data,model='string',outputName='result.txt'):"
    deleteParement(str1)
