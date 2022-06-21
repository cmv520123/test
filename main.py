from flask import Flask, request, jsonify,render_template,url_for
from flask_cors import CORS
import numpy as np
import requests as req
import pandas as pd
from requests_html import HTML
import re
import random
import time
import json
from bs4 import BeautifulSoup
from openpyxl import Workbook
import jieba
from collections import Counter # 次數統計
from tkinter import font
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib import colors
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  
from PIL import Image # 圖片轉array陣列
import pandas as pd
import seaborn as sns
import os
import csv
import parsel #數據解析模組
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from json.decoder import JSONDecodeError

app = Flask(__name__)
CORS(app)
# app.config["DEBUG"]=True
@app.route('/',methods=['POST','GET'])
def index():
    if request.method =='POST':
        if request.values['send']=='送出':
      
            keyword=request.values['user']
          
            return render_template('index.html',name="不給你看!!",keyword=keyword)    
    return render_template("index.html",name="")

@app.route('/data',methods=['POST','GET'])
def DATA():
    if request.method =='POST':
        if request.values['send']=='送出':
      
            keyword=request.values['user']
            from crawler_total import crawler_all
            crawler_all(keyword=keyword)
            
            return render_template('data.html',name="下載成功自己去找!!")
    return render_template('data.html',name="")
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
