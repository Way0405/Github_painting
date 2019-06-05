#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import time
import datetime
 
 
def calculate_date(start, end):
    # 计算日期相差天数
    start_sec = time.mktime(time.strptime(start, '%Y-%m-%d'))
    end_sec = time.mktime(time.strptime(end, '%Y-%m-%d'))
 
    days = int((end_sec - start_sec) / (24 * 60 * 60))
 
    return days
 
 
def commit(flag):
    if flag:
        for n in range(100):  # 设置commit次数
            with open('./record.txt', 'a') as record:
                record.write('.')
                record.close()
                os.system('git commit -a -m \"HeartBeat\"')
 
    else:  # 每天推一条
        with open('./record.txt', 'a') as record:
            record.write('.')
            record.close()
            os.system('git commit -a -m \"HeartBeat\"')
 
    os.system('git pull && git push origin master')
 
 
with open('./model.json') as f:  # 加载模型
    PATTEN = json.loads(f.read())
    f.close()
 
PERIOD = len(PATTEN[0])  # 周期(图案列数)
 
START_DATE = '2019-2-10'  # 开始日期，很重要，左上角提一格的日期，自己手动修改
now ='2019-6-1'
# datetime.datetime.now().strftime('%Y-%m-%d')
 
row = calculate_date(START_DATE, now) % 7
col = int(calculate_date(START_DATE, now) / 7) % PERIOD
 
commit(PATTEN[row][col])
