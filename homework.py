from clean_data import CleanData

"""
3.读取一个txt文件位置在这里https://raw.githubusercontent.com/Jacen789/relation-extraction/master/datasets/all_data.txt，
下载下来，并清洗数据，去除停用词，然后分词。
"""
def process_data(filename):
    f_w=open("data/cleandata.txt", "w", encoding="utf8")
    op=CleanData("data/hit_stopwords.txt")
    with open(filename,"r",encoding="utf8") as f:
        for line in f:
            line=line.strip("\n")
            newline=op.get_result(line)
            f_w.write(newline+"\n")
    f_w.close()

"""
4.去网上找一个csv文件，tsv文件，以及excel文件以.xlsx 结尾的文件，
练习打开文件，读取内容，并新建一个csv，然后写入内容（内容自己随便编写）
"""
import pandas as pd
import openpyxl

def deal_csv(csvfile):
    data=pd.read_csv(csvfile)
    data.to_excel("1.xlsx")

def deal_tsv(tsvfile):
    data=pd.read_csv(tsvfile,sep="\t")
    data.to_excel("2.xlsx")

def deal_excel(excelfile):
    wb=openpyxl.load_workbook(excelfile)#
    sheet=wb.active#获取活动工作表
    data=[]
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))#将每一行的数据添加到data列表中

    csv_file='outputexcel1.csv'
    import csv
    with open(csv_file,mode='w',newline='',encoding='utf8') as f:
        writer=csv.writer(f)
        writer.writerows(data)

if __name__=="__main__":
    # process_data("data/data.txt")
    # deal_csv("data/submission.csv")
    # deal_tsv("data/dev.tsv")
    deal_excel("data/data.xlsx")