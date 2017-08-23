#!/usr/bin/env python
#  -*- coding:utf-8 -*-

import csv
import pandas as pd
import collections
from tkinter import messagebox


def readCsv(filename):
    # find valid indexes for the convenience of reading the whole csv using pandas
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            col_list = row
            break
    while (col_list[-1]==''):
        col_list.pop()
    #print (col_list)
    col_num = len(col_list)
    #print (col_num)


    # if the head has blank in it, it may be troublesome in the following process
    need_change = False
    for head in col_list:
        if len(head.split(' '))!=1:
            messagebox.showwarning("警告", message="csv文件中有列表项存在空格，自动将以_填充")
            need_change = True
            break
    if need_change:
        new_col_list = []
        for head in col_list:
            if len(head.split(' '))!=1:
                new_col_list.append('_'.join(head.split(' ')))
            else:
                new_col_list.append(head)
        col_list = new_col_list


    # Read valid columns. Notice here type are seen as string for convenience
    df = pd.read_csv(filename, usecols=[i for i in range(col_num)], dtype=str, encoding="gb2312")
    if need_change:
        tmp_df = pd.DataFrame(df.values, columns=col_list)
        tmp_df.to_csv(filename, index=False)
        df = tmp_df
    print (df)

    type_list = []
    sample = df.iloc[0]
    for item in sample:
        print ([item, operand_type(item)])




