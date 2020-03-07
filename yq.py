# coding=utf-8
# 读文件
def readFile():
    file = open("yq_in.txt", "r")
    fileList = list(file)            # 将文件转化为列表
    file.close()
    dict = {}
    for i in fileList:             # 遍历列表转化为字典
        List = i.split('\t')
        province = List[0]
        city = List[1]
        number = List[2]
        if province in dict:
            dict[province][city] = number
        else:
            dict[province] = {}
            dict[province][city] = number
    return dict

# 写文件
def writeFile(dict):
    file = open("yq_out.txt", 'w')
    str = ""
    for i in dict:             # 遍历字典转化为字符串
        province = i
        str += province + '\n'

        for j in dict[province]:
            city = j
            number = dict[province][city]
            str += city + '\t' + number
        str += "\n"
    file.write(str)              # 转换为文档形式写出


def Main():
    d = readFile()
    writeFile(d)


if __name__ == "__main__":         # 直接运行模块，执行代码块
    Main()
