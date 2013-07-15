#《毛主席语录》的词频统计

心血来潮，写了一个Python脚本统计《毛主席语录》的词频，前五名为：

    $ pip install jieba
    $ python seg.py && cat mao_out.txt | sort | uniq -c | sort -rg | head -5

    405 我们
    220 人民
    145 革命
    145 他们
    136 工作

简而言之，**我们是人民，主要工作就是革命掉他们，即敌人！**——主席V5！Orz.Orz..Orz...

特别感谢中文分词库：[结巴](https://github.com/fxsjy/jieba)。
