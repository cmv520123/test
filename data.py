import requests # 訪問
import jieba
from collections import Counter # 次數統計
import re
from tkinter import font
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy
from PIL import Image # 圖片轉array陣列
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
#設定圖表顯示中文
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False


    h=[]
    b=[]
    #設定各品牌關鍵字關鍵字
    keywords = ['老協珍','田原香','農純鄉','芳茲','娘家','純煉']
    #讀取檔案
    for keyword in keywords:
        df = pd.read_excel(keyword + '.xlsx')
    #     print(df)
        a = keyword + '.txt'
        df.to_csv(a,header=None,sep=',',index=False)
        with open(a, encoding="utf-8", errors='ignore') as f:
            text_s = f.read()

        # 設定分詞資料庫
        # https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big 右鍵另存放目錄下
        jieba.set_dictionary('dict.txt.big.txt')

        # 將自己常用的詞加入字典
        jieba.load_userdict('C:/Users/User/T大使培訓/userDict.txt')

    #-------------------------------------------------------------------------------設定詞彙

        #帶入正向詞彙
        import sys
        res=[]
        text_god=[]
        with open('好.txt',encoding="utf-8") as f:
            for i in f:
                res.append(list(i.strip('\n').split(',')))      
        for j in res:
            text_god.append(j[0])
        res=[]
        text_bad=[]


        #帶入負向詞彙
        with open('壞.txt',encoding="utf-8") as f:
            for i in f:
                res.append(list(i.strip('\n').split(',')))      
        for j in res:
            text_bad.append(j[0])


        text_x = text_god+text_bad

        for usual_word in text_x:
            jieba.add_word(usual_word)
        jieba.del_word('不') # 刪除不單詞

    #---------------------------------------------------------------------切開文章

        seg_list = jieba.lcut(text_s, cut_all=False) # lcut直接返回list
        words = " ".join(seg_list)
        asd = []
        zxc = []
        for g in seg_list:
            if g in text_x:
                asd.append(g)
                zxc = Counter(asd)
        xcv = dict(zxc)
        print(keyword)
    #--------------------------------------------計算正負向比例
        x=0
        for i in text_god:
            if i in xcv:
                x +=xcv[i]
        print('好的',x)


        y=0
        for i in text_bad:
            if i in xcv:
                y +=xcv[i]
        print('壞的',y)

        if x != 0 and y != 0:
            s =float(x/(x+y)*100)
            boos = int('%.0f' %s)
            h.append(boos)
            print('%.2f' %s)
            u =float(y/(x+y)*100)
            yes = int('%.0f' %u)
            b.append(yes)
            print('%.2f' %u)

        else:
            s = 100
            h.append(s)
            u = 0
            b.append(u)
    #-----------------------------------------畫出圖表

    img = plt.imread('背景圖.jpg')

    plt.figure(figsize=(10,10))#設定圖表大小
    fig,ax = plt.subplots()
    # ax.imshow(img,extent=[0,6,0,100])
    # plt.xticks(x,x)
    ax.bar(keywords, h,color='limegreen',label='正向',linewidth=10)#長條圖數值顏色設定
    ax.bar(keywords, b,color='royalblue',label='負向' ,bottom=h,linewidth=10)#長條圖數值顏色設定
    #長條圖顯示文字
    for i in range(6):
        ax.text(i,
            h[i]/2 - 0.5,                 # 計算垂直高度
            h[i],
            fontsize=14,
            horizontalalignment='center')  # 設定 horizontalalignment 屬性水平置中
        ax.text(i,
            b[i]/2 + h[i] - 0.5,
            b[i],
            fontsize=14,
            horizontalalignment='center')
    plt.title('滴雞精各品牌正負評價比')
    ax.legend(bbox_to_anchor=(1,1), loc='upper left')
    fig.set_size_inches(10, 10)
    ax.spines['top'].set_visible(False)#取消上框
    ax.spines['right'].set_visible(False)#取消右框
    ax.spines['left'].set_visible(False)#取消左框
    ax.get_yaxis().set_visible(False)#取消y軸數值
    plt.show()
    fig.savefig('滴雞精各品牌正負評價比.png')