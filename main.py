import requests # 訪問
import jieba
from collections import Counter # 次數統計
import re
from tkinter import font
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib import colors
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  
import numpy as np
from PIL import Image # 圖片轉array陣列
import pandas as pd
import seaborn as sns
import os
import csv
from bs4 import BeautifulSoup
from openpyxl import Workbook
import parsel #數據解析模組
import requests #數據請求模組
import csv
import json
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
import re
import pandas as pd
from json.decoder import JSONDecodeError
import os
import numpy as np

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
