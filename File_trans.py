#coding = utf-8

import xlrd
import xlwt

def trans(str_ch, num):
    #建立工作台
    data = xlrd.open_workbook('G:\QQPCmgr\Desktop\SVM_project\Data_all\Sample_indoor\{}{}.xls'.format(str_ch, num))
    sheet = data.sheet_by_index(0)

    f=open('G:\QQPCmgr\Desktop\SVM_project\Data_trans\Sample_indoor\{}{}.txt'.format(str_ch, num),'w')


    #总行数
    num_rows = sheet.nrows
    list=[]

    counter = 0
    while(counter<num_rows):
        row_tmp = sheet.row_values(counter)
        inner_counter = 0
        while(inner_counter<4):
            list.append(row_tmp[inner_counter])
            inner_counter += 1
            if(inner_counter == 4):
                list.append('n')
        counter += 1

    len_list = len(list)
    counter = 0
    while(counter<len_list):
        list_tmp = str(list[counter])
        if(counter%5 == 0):
            list_new_tmp = "+1 "
            f.write(list_new_tmp)
        if(list[counter] != 'n'):
            tmp_num = counter%5+1
            tmp_num_str = str(tmp_num)+":"
            tmp_num = str(list[counter])
            list_new_tmp = tmp_num_str+tmp_num+" "
            f.write(list_new_tmp)
        else:
            f.write('\n')
        counter += 1

    f.close()

temp_ch = 'A'
counter = 15
while(counter > 0):
    trans(temp_ch, counter)
    counter-=1
