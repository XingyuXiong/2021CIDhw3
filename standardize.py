#kdd99数据集预处理
#将kdd99符号型数据转化为数值型数据
 
#coding:utf-8
#参考https://blog.csdn.net/tangCprogranm/article/details/95494425?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-1&spm=1001.2101.3001.4242
 
import numpy as np
import pandas as pd
import csv
import time
import math


def Handle_data(source_file='20 Percent Training Set1',handled_file='20 Percent Training Set2'):
    data_file = open(handled_file,'w',newline='')
    with open(source_file,'r') as data_source:
        csv_reader = csv.reader(data_source)       
        count = 0        
        row_num = []#row matrix 40000*43
        for row in csv_reader:
            count = count+1        
            row_num.append(row)

        column_len=len(row_num[0]) # Count the average and standard of feature at each column(at around 43)
        sum = np.zeros(column_len)  #和
        sum.astype(float) 
        avg = np.zeros(column_len) #平均值
        avg.astype(float)
        stadsum = np.zeros(column_len) #绝对误差
        stadsum.astype(float)        
        stad = np.zeros(column_len) #平均绝对误差
        stad.astype(float)  
        dic = {} 
        lists = [] 
        for i in range(0,column_len):
            with open(source_file,'r') as data_source:
                csv_reader = csv.reader(data_source)
                for row in csv_reader:
                    #print(len(row))
                    #print(i)                    
                    sum[i] += float(row[i])
            avg[i] = sum[i] / count    #每一列的平均值求得                    
            with open(source_file,'r') as data_source:
                csv_reader = csv.reader(data_source)
                for row in csv_reader:
                    stadsum[i] += math.pow(abs(float(row[i]) - avg[i]), 2)
            stad[i] = math.pow(stadsum[i] / count,0.5) #每一列的平均绝对误差求得       
            with open(source_file,'r') as data_source:
                csv_reader = csv.reader(data_source)
                li = []                                                              
                for row in csv_reader:                        
                    temp_line=np.array(row)   #将每行数据存入temp_line数组里                  
                    if avg[i] == 0 or stad[i] == 0:
                        temp_line[i] = 0
                    else:
                        temp_line[i] = abs(float(row[i]) - avg[i]) / stad[i]                                             
                    li.append(temp_line[i])                          
                lists.append(li)     

#            break 
        #print(lists)          
        for j in range(0,len(lists)):                                                                
            dic[j] = lists[j] #将每一列的元素值存入字典中                                                                                                          
        df = pd.DataFrame(data = dic)
        df.to_csv(data_file,index=False,header=False)                              
        data_file.close()


if __name__=='__main__':
    Handle_data()