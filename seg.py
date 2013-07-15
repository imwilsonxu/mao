# -*- coding: utf-8 -*-

import jieba


STOPWORDS = [u'的', u'地', u'得', u'而', u'了', u'在', u'是', u'我', u'有', u'和', u'就',  u'不', u'人', u'都', u'一', u'一个', u'上', u'也', u'很', u'到', u'说', u'要', u'去', u'你',  u'会', u'着', u'没有', u'看', u'好', u'自己', u'这']
PUNCTUATIONS = [u'。', u'，', u'“', u'”', u'…', u'？', u'！', u'、', u'；', u'（', u'）']

f_in = open('mao_in.txt')
f_out = open('mao_out.txt', 'w')
try:
    for l in f_in:
        seg_list = jieba.cut(l)
        # print "/".join(seg_list)
        
        for seg in seg_list:
            if seg not in STOPWORDS and seg not in PUNCTUATIONS:
                f_out.write(seg.encode('utf-8', 'strict') + "\n")

        # python seg.py && cat mao_out.txt | sort | uniq -c | sort -rg | head -5
        #405 我们
        #220 人民
        #145 革命
        #145 他们
        #136 工作

finally:
    f_in.close()
