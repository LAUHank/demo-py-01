python streaming word count

yarn jar /usr/hdp/2.4.3.0-227/hadoop-mapreduce/hadoop-streaming.jar \
-Dmapreduce.job.name="lhl-py-strm-wc-01" \
-input /user/lhl13/wordcount \
-output /user/lhl13/pystrm_wc_out_03 \
-mapper "python wc_m.py" \
-reducer "python wc_r.py" \
-file wc_m.py \
-file wc_r.py 

yarn jar /usr/hdp/2.4.3.0-227/hadoop-mapreduce/hadoop-streaming.jar \
-Dmapreduce.job.name="lhl-py-strm-wc-01" \
-input /user/lhl13/wordcount \
-output /user/lhl13/pystrm_wc_out_03 \
-mapper "./wc_m.py" \
-reducer "./wc_r.py" \
-file wc_m.py \
-file wc_r.py 
