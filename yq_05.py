class Yiqing:
    def readFile(self):
        filename = line[1]
        file = open(filename, "r")
        fileList = list(file)
        file.close()
        total = {}
        for i in fileList:
            List = i.split('\t')
            shengshi = List[0]
            place = List[1]
            number = int(List[2][0:-1])
            if shengshi in total:
                total[shengshi][place] = number
            else:
                total[shengshi] = {}
                total[shengshi][place] = number
        return total

    def listWork(list):
        list1 = list.copy()
        result = []
        while list1 != []:
            max = list1[0]
            for i in list1:
                place = i[0]
                count = i[1]
                if count < max[1]:
                    max = i
                elif count == max[1]:
                    if place.encode('gb2312') > max[0].encode('gb2312'):
                        max = i
            result.insert(0, max)
            list1.remove(max)
        return result

    def shengshiCount(shengshi):
        count = 0
        for i in shengshi:
            count += int(shengshi[i])
        return count

    def shengshiList(dic):
        list = []
        for i in dic:
            count = shengshiCount(dic[i])
            list.append((i, count))
        result = listWork(list)
        return result

    def placeList(province):
        list = []
        for i in province:
            count = province[i]
            list.append((i, count))
        result = listWork(list)
        return result

    def writeFile(x):
        filename = line[2]
        file = open(filename, 'w')
        count = len(line)
        if (count <= 3):
            s = ""
            province = shengshiList(x)
            for i in province:
                s += "{} {}\n".format(i[0], i[1])
                place = placeList(x[i[0]])
                for j in place:
                    s += "{} {}\n".format(j[0], j[1])
                s += "\n"
            file.write(s)
        else:
            s = ""
            condition = line[3]
            shengshi = condition
            province = shengshiList(x)
            for i in province:
                if i[0] == shengshi:
                    s += "{} {}\n".format(shengshi, i[1])
                    place = placeList(x[i[0]])
                    for j in place:
                        s += "{} {}\n".format(j[0], j[1])
                    s += "\n"
            file.write(s)

def Main():
    x = Yiqing
    global line
    line = input().split(' ')
    name = x.readFile(line)
    x.writeFile(name)

if __name__ == "__main__":
    Main()