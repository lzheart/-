# coding=utf-8
# 读文件
def readFile():
    filename = l[0]
    file = open(filename, "r")
    fileList = list(file)            # 将文件转化为列表
    file.close()
    dict = {}
    for i in fileList:             # 遍历列表转化为字典
        List = i.split('\t')
        province = List[0]
        city = List[1]
        number = int(List[2])
        if province in dict:
            dict[province][city] = number
        else:
            dict[province] = {}
            dict[province][city] = number
    return dict

# 写文件
def writeFile(d):
    filename = l[1]
    file = open(filename, 'w')
    count = len(l)
    if (count <= 2):
        s = ""
        province_count = pList(d)
        for i in province_count:
            s += "{} {}\n".format(i[0], i[1])
            city = cList(d[i[0]])
            for j in city:
                s += "{} {}\n".format(j[0], j[1])
            s += "\n"
        file.write(s)
    else:
        s = ""
        province = l[2]
        province_count = pList(d)
        for i in province_count:
            if i[0] == province:
                s += "{} {}\n".format(province, i[1])
                city = cList(d[i[0]])
                for j in city:
                    s += "{} {}\n".format(j[0], j[1])
                s += "\n"
        file.write(s)

# 返回排序列表
def pList(dic):
    list = []
    for i in dic:
        count = provinceCount(dic[i])
        list.append((i, count))
    sort_list = listsort(list)
    return sort_list

# 输出省总数
def provinceCount(city):
    count = 0
    for i in city:
        count += int(city[i])
    return count

# 输入参数列表并进行大小排序
def listsort(list):
    list1 = list.copy()
    sort_list = []
    while list1 != []:
        max = list1[0]
        for i in list1:
            city = i[0]
            number = i[1]
            if number < max[1]:
                max = i
            elif number == max[1]:
                if city.encode('gb2312') > max[0].encode('gb2312'):
                    max = i
        sort_list.insert(0, max)
        list1.remove(max)
    return sort_list

# 城市 数目进行大小排序
def cList(province):
    list = []
    for i in province:
        count = province[i]
        list.append((i, count))
    sort_list = listsort(list)
    return sort_list

def Main():
    global l  # 定义全局变量
    l = input().split(' ')
    d = readFile()
    writeFile(d)


if __name__ == "__main__":         # 直接运行模块，执行代码块
    Main()
