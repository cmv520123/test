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
    app.run(debug=True, use_reloader=False)