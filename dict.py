#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import requests,re

word=input("Input the word, ENTER for exit: ")

while(word!=''):
    url="http://dict.youdao.com/w/"+word+"/"
    html=requests.get(url).content.decode('utf-8')
    print("Result is : ")
    # the word is English word
    if ord(word[0].lower()) in range(97,123):   
        result=re.findall(r'<li>(.*?)</li>',html)  
        for i in result:
            if i[0]=='<':
                break
            print(i)
    # the word is Chinese word
    else:
        result=re.findall(r"(?<=                )[a-zA-Z ]+(?=</span>)",html) 
        #上一步提取到的信息列表中有无用项
        for i in result:
            if ord(i[0].lower()) in range(97,123):   
                print(i,end=';')
    word=input("\nInput the word, ENTER for exit: ")
    
