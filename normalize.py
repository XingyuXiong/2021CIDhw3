#kdd99数据集预处理
#将kdd99符号型数据转化为数值型数据
 
#coding:utf-8
#https://blog.csdn.net/tangCprogranm/article/details/95494425?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-1&spm=1001.2101.3001.4242
 
import numpy as np
import pandas as pd
import csv
import time
global label_list  #label_list为全局变量
 
#定义kdd99数据预处理函数
def Find_Maxmin(source_file='20 Percent Training Set2',handled_file='20 Percent Training Set3'):
    dic = {}
    data_file = open(handled_file,'w',newline='')
    with open(source_file,'r') as data_source:
        csv_reader=csv.reader(data_source)       
        count = 0        
        row_num = ""        
        for row in csv_reader:
            count = count+1        
            row_num = row       
        with open(source_file,'r') as data_source:
            csv_reader=csv.reader(data_source)
            final_list = list(csv_reader)
            #print(final_list)
            jmax = []
            jmin = []
            for k in range(0, len(final_list)):                              
                jmax.append(max(final_list[k]))
                jmin.append(min(final_list[k]))
            jjmax = float(max(jmax))  
            jjmin = float(min(jmin))           
            listss = []  
            for i in range(0,len(row_num)):
                lists = [] 
                with open(source_file,'r') as data_source:
                    csv_reader=csv.reader(data_source)           
                    for row in csv_reader: 
                        if (jjmax-jjmin) == 0:
                            x = 0
                        else:
                            x = (float(row[i])-jjmin) / (jjmax-jjmin)                      
                        lists.append(x)
                listss.append(lists)
            for j in range(0,len(listss)):                                         
                dic[j] = listss[j]
            df = pd.DataFrame(data = dic)
            df.to_csv(data_file,index=False,header=False)
            data_file.close()


if __name__=='__main__':
    Find_Maxmin()