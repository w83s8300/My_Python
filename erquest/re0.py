import re
"""
patten=r"ac*"#找c[a-z]t包含[a-z的字]  []<要找[]的字 [\d]<全部的數字 [^]<不包含[]的字 [\w] <包含[]的任何字母与数字 \s <包含[]的任何空白 * 找*前面的1個字 後面的字
patten1=r"ac*"#  * 找*前面的1個字 後面的字

text="dog runsacat ac1t1o cat"#

x =re.search(patten,text)#用patten找text裏的字 
y =re.findall(patten,text)#用patten找所有包含text裏的字 
print(x)
print(y)

patten1 =r"(^.*)號"
text1 = '''台中市太平區還中東路132號 台中市東區中三路999號 台中市南區東中三路9459號'''
x =re.findall(patten1,text1,flags=re.M)#用geoup找text裏的字
import re
"""

text='''台中市南屯區五權西路3段24號 黃小芳 04123456789\n
台中市北屯區崇德路28號 陳小華 03456789789\n
台北市中正區中正路170巷28號 陳小明 87435983749\n
彰化縣埤頭鄉文化路369號 林大力 053445637\n
''' #CSV格式
# x=re.search(patten1,text1,flags=re.M)
addr=r"(^.*號|^.*鄉)"#找號以前的字 (^不包含.*號之後的字)
name=r"號\s(.*) "#找號以後的字到空格之前的字
tel=r"(\d+)$"#找全部空格之後的數字
addr=re.findall(addr,text,flags=re.M)#地址
name=re.findall(name,text,flags=re.M)# 人名
tel=re.findall(tel,text,flags=re.M)# 人名
allData=r"(^.*號) (\w+) (\d+)$"#簡化
allData=re.findall(allData,text,flags=re.M)# 人名

