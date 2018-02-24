#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import requests,re

def analysis():
    word=input("请输入您要翻译的内容： ")
    url="http://dict.youdao.com/w/eng/"+word+"/#keyfrom=dict2.index"
    html=requests.get(url).content.decode('utf-8')
    print("翻译结果：")
    if ord(word[0].lower()) in range(97,123):   #将输入的第一个字节转换为数字，如果数字的值在97到123之间输入的一定是英语，否则输入的是汉语
        result=re.findall(r"(?<=                )\w+(?=</span>)",html)  #匹配翻译后的汉语
        for i in result:
                print(i)        
    else:
        result=re.findall(r"(?<=                )[a-zA-Z ]+(?=</span>)",html) #匹配翻译后的英语
        for i in result:
            if ord(i[0].lower()) in range(97,123):   #上一步提取到的信息列表中有无用项（正则表达式中的空格造成的），这里过滤一下
                print(i)
if __name__ == '__main__':
    while(1):
        analysis()
