# rfind
def string_rfind():
    str1 = "12||"
    ret = str1.rfind("|")
    print(ret)
    str2 = str1[str1.rfind("|"):]
    print(str2)
    split_list = str1.split("|")
    print(split_list)

def string_replace():
    str1 = "9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||"
    print("str1=",str1)



