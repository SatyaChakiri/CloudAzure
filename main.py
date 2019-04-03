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
# app.config['SESSION_TYPE'] = 'memcached'
# app.config['SECRET_KEY'] = 'Secret'

server = 'clouddbaseserver.database.windows.net'
database = 'clouddb'
username = 'satya973@clouddbaseserver'
password = 'Satya@973'
driver= '{ODBC Driver 17 for SQL Server}'
connection = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
# connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=swethacloudserver.database.windows.net;Database=Sapp1;Uid=svrswetha@swethacloudserver;Pwd=Swetha123")
# connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=assignm3.database.windows.net;Database=earthquake;Uid=satya973@assignm3;Pwd=Satya@973") #;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;

cursor = connection.cursor()
# print(cursor)
# myhost="satya.redis.cache.windows.net"
# myapsswrd="9FZFgFbbUr0A63Bm2dW63jQKYvXOiGkWa5454bRQhgM="
# r = redis.StrictRedis(host=myhost,port=6380,password=myapsswrd,ssl=True)
#satya.redis.cache.windows.net:6380,password=9FZFgFbbUr0A63Bm2dW63jQKYvXOiGkWa5454bRQhgM=,ssl=True,abortConnect=False

@app.route('/')
def my_form():
    return render_template('my-form.html')
    # connection.commit()
    # clusters=request.form['Year']
    # query1="Select fare,age from dbo.titanic"  #where "++">"+ra1+" and Y"+year+"<"+ra11+";"
    # cur = connection.cursor()
    # cur.execute(query1)
    # val1 = cur.fetchall()
    # import random
    # centroid=[]
    # centroidval=[]
    # # clusters = 5
    # i=0
    # while i<clusters:
    #   value=random.randint(0,len(val1)-1)
    #   if value not in centroid:
    #    centroidval.append([val1[int(value)]])
    #    centroid.append(value)
    #    i+=1
    # centroidvalues=centroidval
    # centroidvaldist = []
    # for i in range(len(centroidvalues)):
    #     distval=[]
    #     for j in range(len(centroidvalues)):
    #         dist = math.sqrt((centroidvalues[j][0][0] - centroidvalues[i][0][0]) ** 2 + (
    #                     centroidvalues[j][0][1] - centroidvalues[i][0][1]) ** 2)
    #         distval.append(dist)
    #     centroidvaldist.append(distval)
    # # print(centroidval)
    # # print(centroidvaldist)
    # run=0
    # run2=0
    # while(True):
    #     for i in range(len(val1)):
    #         centroiddist=[]
    #         for j in range(len(centroidvalues)):
    #             dist=math.sqrt((centroidvalues[j][0][0]-val1[i][0])**2+(centroidvalues[j][0][1]-val1[i][1])**2)
    #             centroiddist.append(dist)
    #         centroidvalues[centroiddist.index(min(centroiddist))].append(val1[i])
    #     centroidvalues2=[]
    #     for i in range(len(centroidvalues)):
    #         xavg = 0
    #         yavg = 0
    #         for j in range(len(centroidvalues[i])):
    #             xavg+=centroidvalues[i][j][0]
    #             yavg+=centroidvalues[i][j][1]
    #         centroidpoint=(xavg/len(centroidvalues[i]),yavg/len(centroidvalues[i]))
    #         centroidvalues2.append([centroidpoint])
    #     centroidvalues3=centroidvalues
    #     centroidvalues=centroidvalues2
    #     # print(centroidvalues)
    #     centroidvaldist2=centroidvaldist
    #     run=0
    #     # print(centroidvalues)
    #     for i in range(len(centroidvalues)):
    #         for j in range(len(centroidvalues)):
    #             dist=math.sqrt((centroidvalues[j][0][0]-centroidvalues[i][0][0])**2+(centroidvalues[j][0][1]-centroidvalues[i][0][1])**2)
    #             if (centroidvaldist2[i][j]-dist)<-1 or (centroidvaldist2[i][j]-dist)>1:
    #                 run += 1
    #             centroidvaldist[i][j]=dist
    #     # print(centroidvaldist)
    #     run2+=1
    #     print(run)
    #     print(run2)
    #     if run==0:
    #         break
    # # print(run2)
    # return render_template('kmeans.html',values=centroidvaldist2,len=clusters)

@app.route('/Limit2', methods=['get', 'post'])
def limit2():
    strat = time()
    clusters=int(request.form['clusters'])
    att1=request.form['att1']
    att2=request.form['att2']
    point1 = request.form['poi1']
    point2 = request.form['poi2']
    if(att1=="decklevel"):
        query1 = "Select cabinnum/100," + att2 + " from dbo.minnow;"  # where "++">"+ra1+" and Y"+year+"<"+ra11+";"
    elif(att2=="decklevel"):
      query1 = "Select "+ att1 +",cabinnum/100 from dbo.minnow;"  # where "++">"+ra1+" and Y"+year+"<"+ra11+";"
    else:
     query1="Select "+ att1+","+att2+" from dbo.minnow"  #where "++">"+ra1+" and Y"+year+"<"+ra11+";"
    cur = connection.cursor()
    cur.execute(query1)
    val1 = cur.fetchall()
    import random
    centroid=[]
    centroidval=[]
    # clusters = 5
    i=0
    while i<clusters:
      value=random.randint(0,len(val1)-1)
      if value not in centroid:
       centroidval.append([val1[int(value)]])
       centroid.append(value)
       i+=1
    centroidvalues=centroidval
    centroidvaldist = []
    for i in range(len(centroidvalues)):
        distval=[]
        for j in range(len(centroidvalues)):
            dist = math.sqrt((centroidvalues[j][0][0] - centroidvalues[i][0][0]) ** 2 + (
                        centroidvalues[j][0][1] - centroidvalues[i][0][1]) ** 2)
            distval.append(dist)
        centroidvaldist.append(distval)
    # print(centroidval)
    # print(centroidvaldist)
    run=0
    run2=0
    while(True):
        centroidvaluesnew=centroidvalues
        print(centroidvaluesnew)
        for i in range(len(val1)):
            centroiddist=[]
            for j in range(len(centroidvalues)):
                dist=math.sqrt((centroidvalues[j][0][0]-val1[i][0])**2+(centroidvalues[j][0][1]-val1[i][1])**2)
                centroiddist.append(dist)
            centroidvalues[centroiddist.index(min(centroiddist))].append(val1[i])
        centroidvalues2=[]
        for i in range(len(centroidvalues)):
            xavg = 0
            yavg = 0
            for j in range(len(centroidvalues[i])):
                xavg+=centroidvalues[i][j][0]
                yavg+=centroidvalues[i][j][1]
            centroidpoint=(xavg/len(centroidvalues[i]),yavg/len(centroidvalues[i]))
            centroidvalues2.append([centroidpoint])
        centroidvalues3=centroidvalues
        pointcount=[]
        for i in range(clusters):
            pointcount.append(len(centroidvalues3[i]))
        print(pointcount)
        centroidvalues=centroidvalues2
        # print(centroidvalues)
        centroidvaldist2=centroidvaldist
        run=0
        # print(centroidvalues)
        for i in range(len(centroidvalues)):
            for j in range(len(centroidvalues)):
                dist=math.sqrt((centroidvalues[j][0][0]-centroidvalues[i][0][0])**2+(centroidvalues[j][0][1]-centroidvalues[i][0][1])**2)
                if (centroidvaldist2[i][j]-dist)<-1 or (centroidvaldist2[i][j]-dist)>1:
                    run += 1
                centroidvaldist[i][j]=dist
        # print(centroidvaldist)
        run2+=1
        print(run)
        print(run2)
        if run==0:
            break
        endtime=time()
        time_taken=endtime-strat
    point=(point1,point2)
    pointdis=[]
    for i in range(clusters):
        dist=math.sqrt((centroidvaluesnew[i][0][0]-point1)**2+(centroidvaluesnew[i][0][1]-point2)**2)
        pointdis.append(dist)
    pointcluster1=centroidvaluesnew[pointdis.index(min(pointdis))][6][0]
    pointcluster2 = centroidvaluesnew[pointdis.index(min(pointdis))][6][1]
    query1 = "Select * from dbo.minnow where "+att1+"=="+ pointcluster1 + "and "+att2+"=="+pointcluster2+";"  # where "++">"+ra1+" and Y"+year+"<"+ra11+";"
    # print(run2)
    return render_template('kmeans.html',points=pointcount,time=time_taken,centroids=centroidvaluesnew,values=centroidvaldist2,len=clusters)


@app.route('/Limit', methods=['get', 'post'])
def limit():
    strat = time()
    clusters=int(request.form['clusters'])
    att1=request.form['att1']
    att2=request.form['att2']
    point1 = request.form['poi1']
    point2 = request.form['poi2']
    if(att1=="decklevel"):
        query1 = "Select cabinnum/100," + att2 + " from dbo.minnow;"  # where "++">"+ra1+" and Y"+year+"<"+ra11+";"
    elif(att2=="decklevel"):
      query1 = "Select "+ att1 +",cabinnum/100 from dbo.minnow;"  # where "++">"+ra1+" and Y"+year+"<"+ra11+";"
    else:
     query1="Select "+ att1+","+att2+" from dbo.minnow"  #where "++">"+ra1+" and Y"+year+"<"+ra11+";"
    cur = connection.cursor()
    cur.execute(query1)
    val1 = cur.fetchall()
    import random
    centroid=[]
    centroidval=[]
    # clusters = 5
    i=0
    while i<clusters:
      value=random.randint(0,len(val1)-1)
      if value not in centroid:
       centroidval.append([val1[int(value)]])
       centroid.append(value)
       i+=1
    centroidvalues=centroidval
    centroidvaldist = []
    for i in range(len(centroidvalues)):
        distval=[]
        for j in range(len(centroidvalues)):
            dist = math.sqrt((centroidvalues[j][0][0] - centroidvalues[i][0][0]) ** 2 + (
                        centroidvalues[j][0][1] - centroidvalues[i][0][1]) ** 2)
            distval.append(dist)
        centroidvaldist.append(distval)
    # print(centroidval)
    # print(centroidvaldist)
    run=0
    run2=0
    while(True):
        centroidvaluesnew=centroidvalues
        print(centroidvaluesnew)
        for i in range(len(val1)):
            centroiddist=[]
            for j in range(len(centroidvalues)):
                dist=math.sqrt((centroidvalues[j][0][0]-val1[i][0])**2+(centroidvalues[j][0][1]-val1[i][1])**2)
                centroiddist.append(dist)
            centroidvalues[centroiddist.index(min(centroiddist))].append(val1[i])
        centroidvalues2=[]
        for i in range(len(centroidvalues)):
            xavg = 0
            yavg = 0
            for j in range(len(centroidvalues[i])):
                xavg+=centroidvalues[i][j][0]
                yavg+=centroidvalues[i][j][1]
            centroidpoint=(xavg/len(centroidvalues[i]),yavg/len(centroidvalues[i]))
            centroidvalues2.append([centroidpoint])
        centroidvalues3=centroidvalues
        pointcount=[]
        for i in range(clusters):
            pointcount.append(len(centroidvalues3[i]))
        print(pointcount)
        centroidvalues=centroidvalues2
        # print(centroidvalues)
        centroidvaldist2=centroidvaldist
        run=0
        # print(centroidvalues)
        for i in range(len(centroidvalues)):
            for j in range(len(centroidvalues)):
                dist=math.sqrt((centroidvalues[j][0][0]-centroidvalues[i][0][0])**2+(centroidvalues[j][0][1]-centroidvalues[i][0][1])**2)
                if (centroidvaldist2[i][j]-dist)<-1 or (centroidvaldist2[i][j]-dist)>1:
                    run += 1
                centroidvaldist[i][j]=dist
        # print(centroidvaldist)
        run2+=1
        print(run)
        print(run2)
        if run==0:
            break
        endtime=time()
        time_taken=endtime-strat
    point=(point1,point2)
    pointdis=[]
    for i in range(clusters):
        dist=math.sqrt((centroidvaluesnew[i][0][0]-int(point1))**2+(centroidvaluesnew[i][0][1]-int(point2))**2)
        pointdis.append(dist)
    pointcluster1=str(centroidvaluesnew[pointdis.index(min(pointdis))][6][0])
    pointcluster2 = str(centroidvaluesnew[pointdis.index(min(pointdis))][6][1])
    query1 = "Select * from dbo.minnow where "+att1+"="+ pointcluster1 + " and "+att2+"="+pointcluster2+";"
    # print(run2)
    print(query1)
    cur = connection.cursor()
    cur.execute(query1)
    val1 = cur.fetchall()
    print(val1[0][1])
    return render_template('kmeans.html',points=pointcount,time=time_taken,centroids=centroidvaluesnew,values=centroidvaldist2,len=clusters,age=val1[0][3],cbin=val1[0][0],sur=val1[0][4])
#     year=request.form['Year']
#     ra1 = int(request.form['ra1'])
#     ra1=str(ra1*100000)
#     print(ra1)
#     ra11 = int(request.form['ra11'])
#     ra11 = str(ra11*100000)
#     print(ra11)
#     ra2 = int(request.form['ra2'])
#     ra2 = str(ra2*1000000)
#     ra21 = int(request.form['ra21'])
#     ra21 = str(ra21*1000000)
#     ra3= int(request.form['ra3'])
#     ra3 = str(ra3*1000000)
#     ra31 = int(request.form['ra31'])
#     ra31 = str(ra31*100000)
#     query1 = "Select count(*) from dbo.population where Y"+year+">"+ra1+" and Y"+year+"<"+ra11+";"
#     query4 = "Select Year,BLPErcent from dbo.educationshare;"
#     query2 = "Select count(*) from dbo.population where Y"+year+">"+ra2+" and Y"+year+"<"+ra21+";"
#     query3 = "Select count(*) from dbo.population where Y"+year+">"+ra2+" and Y"+year+"<"+ra21+";"
#     print(query1)
#     cur = connection.cursor()
#     cur.execute(query1)
#
#     print(cur.execute(query1))
#     val1 = cur.fetchall()
#     cur.execute(query2)
#     val2 = cur.fetchall()
#     cur.execute(query3)
#     val3 = cur.fetchall()
#     cur.execute(query4)
#     val4= cur.fetchall()
#     print(val4)
#     x=[]
#     y=[]
#
#     for i in range(len(val4)):
#         x.append(list(val4[i]))
#         # x.append(val4[i][0])
#         # y.append(val4[i][1])
#     print(x)
#     # print(y)
#     dct1=dict()
#     dct2 = dict()
#     dct3 = dict()
#
#     dct1["label"]="ra1"
#     dct1["value"]=val1[0][0]
#     dct2["label"] = "ra2"
#     dct2["value"] = val2[0][0]
#     dct3["label"] = "ra3"
#     dct3["value"] = val3[0][0]
#     d=[]
#     d.append(dct1)
#     d.append(dct2)
#     d.append(dct3)
#     print(val1)
#     print(d)
#     leng=len(d)
#     connection.commit()
#     cursor.close()
#     return render_template('range.html', ra1=val1, ra2=val2,ra3=val3,d=d,xaxis=x,yaxis=y,data=val4,length=leng)


if __name__ == '__main__':
   app.run(debug = True)
