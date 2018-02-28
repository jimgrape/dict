#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import requests,re,sys

def trans(word):
    url="http://dict.youdao.com/w/"+word+"/"
    html=requests.get(url).content.decode('utf-8')
    print("%s : \n" % word)
    # the word is English word
    if ord(word[0].lower()) in range(97,123):   
        result=re.findall(r'<li>(.*?)</li>',html)  
        pron=re.findall(r'class="phonetic">(.*?)</span>',html)
        if pron!=[]:
            print("英%s   美%s" % (pron[0],pron[1]))
        for i in result:
            if i=='' or i[0]=='<':
                break
            print(i)
    # the word is Chinese word
    else:
        result=re.findall(r"(?<=                )[a-zA-Z ]+(?=</span>)",html) 
        #上一步提取到的信息列表中有无用项
        for i in result:
            if ord(i[0].lower()) in range(97,123):   
                print(i,end=';')

if len(sys.argv)==2:
    trans(sys.argv[1])
else:
    word=input("Input the word, ENTER for exit: ")
    while(word!=''):
        trans(word)
        word=input("\nInput the word, ENTER for exit: ")
