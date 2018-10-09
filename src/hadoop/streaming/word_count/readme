python streaming word count

cat wc_src.txt | python wc_m.py | sort | python wc_r.py
cat wc_src.txt | ./wc_m.py | sort | ./wc_r.py

# streaming word count 脚本不能使用 -files
yarn jar /usr/hdp/2.4.3.0-227/hadoop-mapreduce/hadoop-streaming.jar \
-Dmapreduce.job.name="lhl-py-strm-wc-01" \
-input /user/lhl13/wordcount \
-output /user/lhl13/pystrm_wc_out_03 \
-mapper "python wc_m.py" \
-reducer "python wc_r.py" \
-file wc_m.py \
-file wc_r.py 

# streaming word count 脚本不能使用 -files
yarn jar /usr/hdp/2.4.3.0-227/hadoop-mapreduce/hadoop-streaming.jar \
-Dmapreduce.job.name="lhl-py-strm-wc-01" \
-input /user/lhl13/wordcount \
-output /user/lhl13/pystrm_wc_out_03 \
-mapper "./wc_m.py" \
-reducer "./wc_r.py" \
-file wc_m.py \
-file wc_r.py 


# streaming 上传边数据文件 实现黑白名单 普通文件上传可以使用 -file -files 均可
yarn jar /usr/hdp/2.4.3.0-227/hadoop-mapreduce/hadoop-streaming.jar \
-Dmapreduce.job.name="lhl-py-strm-wc-01" \
-input /user/lhl13/wordcount \
-output /user/lhl13/pystrm_wc_out_04 \
-mapper "./wc_m.py" \
-reducer "./wc_r.py" \
-file wc_m.py \
-file wc_r.py \
-file my_name_list

# streaming 上传边数据文件 实现黑白名单 普通文件上传可以使用 -file -files 均可
yarn jar /usr/hdp/2.4.3.0-227/hadoop-mapreduce/hadoop-streaming.jar \
-files my_name_list \
-Dmapreduce.job.name="lhl-py-strm-wc-01" \
-input /user/lhl13/wordcount \
-output /user/lhl13/pystrm_wc_out_05 \
-mapper "./wc_m.py" \
-reducer "./wc_r.py" \
-file wc_m.py \
-file wc_r.py 

# 使用黑白名单时 mapper 要修改如下
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys

def readFileAsSet(filePath = "myfile") :
    mySet = set()
    try :
        file = open(filePath)
        for line in file :
            mySet.add(line.strip())
    except Exception, e :
        print e
    finally :
        if file :
            file.close()
    return mySet

mySet = readFileAsSet('my_name_list')

for line in sys.stdin :
    word_arr = line.strip().split(' ')
    for word in word_arr :
        # 白名单用 in 黑名单用 not in
        if word in mySet :
            print '%s\t%s' % (word, 1)
