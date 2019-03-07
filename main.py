import math

from flask import Flask, request, render_template, flash

import pyodbc
from time import time
import csv
import hashlib
import redis
import pickle as cPickle
from random import *
import random

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'Secret'

server = 'assignm3.database.windows.net'
database = 'earthquake'
username = 'satya973@assignm3'
password = 'Satya@973'
driver= '{ODBC Driver 17 for SQL Server}'
connection = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
# connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=swethacloudserver.database.windows.net;Database=Sapp1;Uid=svrswetha@swethacloudserver;Pwd=Swetha123")
# connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=assignm3.database.windows.net;Database=earthquake;Uid=satya973@assignm3;Pwd=Satya@973") #;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;

cursor = connection.cursor()
print(cursor)
myhost="satya.redis.cache.windows.net"
myapsswrd="9FZFgFbbUr0A63Bm2dW63jQKYvXOiGkWa5454bRQhgM="
r = redis.StrictRedis(host=myhost,port=6380,password=myapsswrd,ssl=True)
#satya.redis.cache.windows.net:6380,password=9FZFgFbbUr0A63Bm2dW63jQKYvXOiGkWa5454bRQhgM=,ssl=True,abortConnect=False

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/Limit', methods=['get', 'post'])
def limit():
    year=request.form['Year']
    ra1 = int(request.form['ra1'])
    ra1=str(ra1*100000)
    print(ra1)
    ra11 = int(request.form['ra11'])
    ra11 = str(ra11*100000)
    print(ra11)
    ra2 = int(request.form['ra2'])
    ra2 = str(ra2*1000000)
    ra21 = int(request.form['ra21'])
    ra21 = str(ra21*1000000)
    ra3= int(request.form['ra3'])
    ra3 = str(ra3*1000000)
    ra31 = int(request.form['ra31'])
    ra31 = str(ra31*100000)
    query1 = "Select count(*) from dbo.population where Y"+year+">"+ra1+" and Y"+year+"<"+ra11+";"
    query4 = "Select Year,BLPErcent from dbo.educationshare;"
    query2 = "Select count(*) from dbo.population where Y"+year+">"+ra2+" and Y"+year+"<"+ra21+";"
    query3 = "Select count(*) from dbo.population where Y"+year+">"+ra2+" and Y"+year+"<"+ra21+";"
    print(query1)
    cur = connection.cursor()
    cur.execute(query1)

    print(cur.execute(query1))
    val1 = cur.fetchall()
    cur.execute(query2)
    val2 = cur.fetchall()
    cur.execute(query3)
    val3 = cur.fetchall()
    cur.execute(query4)
    val4= cur.fetchall()
    print(val4)
    x=[]
    y=[]

    for i in range(len(val4)):
        x.append(list(val4[i]))
        # x.append(val4[i][0])
        # y.append(val4[i][1])
    print(x)
    # print(y)
    dct1=dict()
    dct2 = dict()
    dct3 = dict()

    dct1["label"]="ra1"
    dct1["value"]=val1[0][0]
    dct2["label"] = "ra2"
    dct2["value"] = val2[0][0]
    dct3["label"] = "ra3"
    dct3["value"] = val3[0][0]
    d=[]
    d.append(dct1)
    d.append(dct2)
    d.append(dct3)
    print(val1)
    print(d)
    leng=len(d)
    connection.commit()
    cursor.close()
    return render_template('range.html', ra1=val1, ra2=val2,ra3=val3,d=d,xaxis=x,yaxis=y,data=val4,length=leng)

@app.route('/Limit2', methods=['get', 'post'])
def limit2():
    year=request.form['Year']
    ra1 = int(request.form['ra1'])
    ra1=str(ra1*0)
    print(ra1)
    ra11 = int(request.form['ra1'])
    ra11 = str(ra11*100000)
    print(ra11)
    ra2 = int(request.form['ra1'])
    ra2 = str(ra2*1000000)
    ra21 = int(request.form['ra1'])+int(request.form['ra1'])
    ra21 = str(ra21*1000000)
    ra3= int(request.form['ra1'])+int(request.form['ra1'])
    ra3 = str(ra3*1000000)
    ra31 = int(request.form['ra1'])+int(request.form['ra1'])+int(request.form['ra1'])
    ra31 = str(ra31*100000)
    query1 = "Select count(*) from dbo.population where Y"+year+">"+ra1+" and Y"+year+"<"+ra11+";"
    # query4 = "Select Year,BLPErcent from dbo.educationshare;"
    query2 = "Select count(*) from dbo.population where Y"+year+">"+ra2+" and Y"+year+"<"+ra21+";"
    query3 = "Select count(*) from dbo.population where Y"+year+">"+ra2+" and Y"+year+"<"+ra21+";"
    print(query1)
    cur = connection.cursor()
    cur.execute(query1)

    print(cur.execute(query1))
    val1 = cur.fetchall()
    cur.execute(query2)
    val2 = cur.fetchall()
    cur.execute(query3)
    val3 = cur.fetchall()
    # cur.execute(query4)
    # val4= cur.fetchall()
    # print(val4)
    # x=[]
    # y=[]
    #
    # for i in range(len(val4)):
    #     x.append(list(val4[i]))
    #     # x.append(val4[i][0])
    #     # y.append(val4[i][1])
    # print(x)
    # print(y)
    dct1=dict()
    dct2 = dict()
    dct3 = dict()

    dct1["label"]="ra1"
    dct1["value"]=val1[0][0]
    dct2["label"] = "ra2"
    dct2["value"] = val2[0][0]
    dct3["label"] = "ra3"
    dct3["value"] = val3[0][0]
    d=[]
    d.append(dct1)
    d.append(dct2)
    d.append(dct3)
    print(val1)
    print(d)
    leng=len(d)
    connection.commit()
    cursor.close()
    return render_template('range2.html', ra1=val1, ra2=val2,ra3=val3)


if __name__ == '__main__':
  app.run()
