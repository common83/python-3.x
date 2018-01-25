# __*__encoding=utf-8 __*__


class HuffmanItem:
    item = ""
    value = 0
    marked = False
    code = ""
    left = -1
    right = -1

    def __init__(self,item="", value=0):
        self.item = item
        self.value = value

class Huffman:
    arr = []
    result = []

    def addItem(self,item,value):
        if item and value > 0:
            self.arr.append(HuffmanItem(item,value))

    def initResult(self):
        for i in self.arr:
            self.result.append(i)
        for i in range(len(self.arr),2*len(self.arr)-1):
            self.result.append(HuffmanItem())

    def clearItem(self):
        if self.arr:
            self.arr.clear()
        if self.result:
            self.result.clear()

    def getMinItem(self):
        index = 0
        value = 0
        item = ""
        for i in range(len(self.result)):
            if not self.result[i].marked and self.result[i].value > 0:
                if value == 0 or self.result[i].value < value:
                    index = i
                    value = self.result[i].value
                    item = self.result[i].item
        self.result[index].marked = True
        # print([index,value,item])
        return [index,value,item]

    def calcHuffman(self):
        index = len(self.arr)
        self.initResult()
        while index < len(self.result):
            ret1 = self.getMinItem()
            left = ret1[0]
            value1 = ret1[1]
            item1 = ret1[2]
            ret2 = self.getMinItem()
            right = ret2[0]
            value2 = ret2[1]
            item2 = ret2[2]
            self.result[index].item = item1+item2
            self.result[index].value = value1+value2
            self.result[index].left = left
            self.result[index].right = right
            index += 1

    def huffmanCodingFlag(self, index, code):
        self.result[index].code += code
        left = self.result[index].left
        right = self.result[index].right
        if left >= 0:
            self.huffmanCodingFlag(left, self.result[index].code+"0")
        if right >= 0:
            self.huffmanCodingFlag(right, self.result[index].code+"1")

    def huffmanCodingTree(self):
        self.calcHuffman()
        index = len(self.result)
        self.huffmanCodingFlag(index - 1, "")

    def printResult(self):
        info = ""
        for i in range(len(self.arr)):
            item =self.result[i]
            info += "{%s,%d,huffmanCode:%s} " \
                    %(item.item,item.value,item.code)+"\r\n"
        print(info)

    def encode_length(self):
        count = 0
        if len(self.arr) == 1:
            return self.result[0].value

        for i in range(len(self.arr)):
            item = self.result[i]
            count += item.value * len(item.code)
        ret = count
        return ret

class kevindi(object):

    def result_function(self, para_str_list):
        if not para_str_list:
            return 0
        if len(para_str_list) == 1:
            return 1

        alpha_count = {}
        hufman = Huffman()
        for i in range(len(para_str_list)):
            if para_str_list[i] in alpha_count:
                alpha_count[para_str_list[i]] += 1
            else:
                alpha_count[para_str_list[i]] = 1
        for item, value in alpha_count.items():
            hufman.addItem(item,value)

        hufman.huffmanCodingTree()
        # hufman.printResult()
        ret = hufman.encode_length()
        hufman.clearItem()
        return ret;

if __name__ == '__main__':
    tmp_prime = kevindi()

    value = "abc"
    print(tmp_prime.result_function(value))


