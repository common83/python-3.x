# rfind
import re
import timeit
import operator as op


def string_copy():
    '''复制'''
    name = 'tomcat'
    print('name=',name)
    logo = name
    print('logo=',logo)
    slogn = 'apache is useful'
    logo = slogn
    print('logo = slogn =',logo)
    logo = name
    print('logo = name=',name)
    triger = 'apache found is good'
    logo = triger
    print('logo=triger = ',logo)


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

def killAnUnseen(s):
    try:
        s.encode('gbk')
    except UnicodeEncodeError as err:
        info = str(err)
        st = re.search('\\\\u[a-f0-9]{4}|\\\\x[a-f0-9]{2}', info).group()[2:]
        x = int(st, 16)
        return s.replace(chr(x), "")
    return s

def string_strip():
  str1 = '迪巴拉  的中文名是什么'
  print(str1.strip(' '))
  print(str1.expandtabs())
  print(str1.split(' '))
  print(str1.split('\xa0'))
  print(killAnUnseen(str1))

def string_replace2():
    s = '*ST爱富第八届第九次（临时）监事会决议公告'
    name = '*ST爱富'
    n = re.sub('^\*','\*',name)
    pdf_title = re.sub(('\A' + n), 'ss', s)
    print(pdf_title)


def string_replace3():
    s = '*ST爱富第八届第九次（临时）监事会决议公告'
    s1 = '三六零第八届第九次（临时）监事会决议公告'
    s2 = 'S*ST天颐第八届第九次（临时）监事会决议公告'
    s3 = '东电B股第八届第九次（临时）监事会决议公告'
    name = 'S*ST爱富'
    n = re.sub('\*', '\*', name)
    s_list = ['三六零', '小米集团-M', '*ST爱富','S*ST天颐','东电B股']
    s_str = '|'.join(s_list)
    print('s_str= ', s_str)
    s_str = re.sub('\*', '\*', s_str)
    print('new s_str= ', s_str)
    r_str = re.compile('\A(?P<c_name>' + s_str + ')' + '(：?)' + '(?P<c_title>.*)')
    print("r_str=", r_str)
    if isinstance(r_str, re._pattern_type):
        print('true')
    p1 = r_str.sub('ss', s1)
    # p2 = re.sub(('\A' + '(' + s_str + ')'), 'ss', s2)
    t3 = r_str.match(s3)
    m_t = r_str.match(s2)
    print('type=', m_t)
    print('type=', type(m_t))
    if m_t:
        a_g = m_t.groups()
        print('test=', a_g)
        print('name=', m_t.group('c_name'))
        print('title=', m_t.group('c_title'))

    m_t = re.match(r_str, s3)
    if m_t:
        a_g = m_t.groups()
        print('test=', a_g)
        print('name=', m_t.group('c_name'))
        print('title=', m_t.group('c_title'))


def string_none_blank():
    s = None
    if not s:
        print('not true')
        print('type=',type(s))
    a = ''
    if not a:
        print('not true')
        print('type=', type(a))
    else:
        print('true')
        print('type=', type(a))

def str_count():
    sStr1 = '1345678'
    sStr2 = '456'
    print(sStr1.count(sStr2))

def str_upper_and_lower():
    sStr1 = 'JCstrlwr'
    sStr = sStr1.upper()
    sStr2 = sStr1.lower()
    print(sStr, sStr2)

def str_cat():
    sStr1 = '1345'
    sStr2 = 'abcdef'
    n = 10
    sStr1 += sStr2[0:n]
    print(sStr1)

def str_cmp():
    sStr1 = '1345'
    sStr2 = '13bc'
    n = 5
    print(op.eq(sStr1[0:n],sStr2[0:n]))

def str_copy():
    sStr = '1345'
    n = 3
    str2 = sStr[0:n]
    print(str2)


if __name__ == '__main__':
    # string_replace()
    # string_rfind()
    # string_clear()
    # string_strip()
    # string_replace2()
    # string_none_blank()
    # string_replace3()
    # string_copy()
    # str_count()
    # str_cat()
    str_cmp()





