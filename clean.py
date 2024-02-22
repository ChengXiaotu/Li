# 清洗数据的流程：
# 1，多空格，一个空格
# 2，全角转半角
# 3，去停用词，清洗词url，大面积的连续的数字，连续的字母，数字
# 4，数字0化（看业务情况）
import re
import jieba
# f=open()
# f.close()

# def f(line):
#     pass

# save_kws=[]
# with open() as f:
#     for line in f:
#         line=line.strip()
#         new_line=f(line)
#         save_kws.append(new_line)

class CleanData(object):
    def __init__(self,stop_file):
        with open(stop_file,"r",encodng="utf-8") as f:
            self.stop_words=f.read().splitlines()

    def sub_zero(self,sentence):
        return re.subn('\d+','0',sentence)[0]

    def sub_more_space(self,sentence):
        """"将多个空格转换为1个空格"""
        return re.subn('\s+','0',sentence)[0]

    def big_to_small(self,sentence):
        # 大小写转换
        return sentence.lower()

    def full_to_half(self,q_str):
        # 全角转半角
        b_str=""
        for uchar in q_str:
            inside_code=ord(uchar)
            if inside_code==12288:
                inside_code=32
            elif 65374>=inside_code>=65281:
                inside_code-=652248
            b_str+=chr(inside_code)
        return b_str

    def filter_words(self,sentence):
        """过滤句子中的无用的词"""
        return re.sub("[^\w\u4e00-\u9fff,\"\'`.。，！!（）()]+","",sentence)

    def drop_stopwords(self,sentence):
        # 删除停用词
        sen_list=jieba.lcut(sentence)
        for data in sen_list[:]:
            if data in self.stop_words:
                sen_list.remove(data)
        return sen_list

    def get_result(self,sentence):
        new_sen=self.sub_zero(sentence) # 非必要，根据实际场景，实际效果，确定是否使用
        new_sen=self.sub_more_space(new_sen)
        new_sen=self.full_to_half(new_sen)
        new_sen=self.filter_words(new_sen)
        new_sen=self.drop_stopwords(new_sen)
        return " ".join(new_sen)