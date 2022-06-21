from flask import Flask, request, jsonify,render_template,url_for
from flask_cors import CORS
import numpy as np
import requests as req
import pandas as pd

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
            from crawler_all import crawler_all
            crawler_all(keyword=keyword)
            return render_template('data.html',name="下載成功自己去找!!")
        return render_template('data.html',name="")
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
