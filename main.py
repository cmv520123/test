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
import parsel #數據解析模組
import csv
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from json.decoder import JSONDecodeError
import os

from rq import Queue
from worker import conn

q = Queue(connection=conn)


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
            result = q.enqueue(crawler_all,keyword)
            
            return render_template('data.html',name="下載成功自己去找!!",result=result,crawler_all=crawler_all)
    return render_template('data.html',name="")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1314)
