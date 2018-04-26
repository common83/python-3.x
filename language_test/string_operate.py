# rfind
def string_rfind():
    str1 = "12||"
    ret = str1.rfind("|")
    print(ret)
    str2 = str1[str1.rfind("|"):]
    print(str2)
    split_list = str1.split("|")
    print(split_list)
    print(str1.find("/"))

def string_replace():
    str1 = "9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||"
    print("str1=",str1)
    str2 = str1.replace("-","0")
    print("str1=", str2)
    print("str1=", str1)

def string_clear():
    str1 = "test"
    print(str1)
    str1 = ""
    print(str1)
    str1 = "new"
    print(str1)
# string_replace()
# string_rfind()
string_clear()




