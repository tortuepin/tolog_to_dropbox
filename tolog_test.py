import os
import sys
import tolog_to_dropbox as t_td
import tolog_functions as t_f
import tolog_config as t_conf

config = t_conf.TologConfig()

#TOKEN="TOLOG_DB_TOKEN"
#LOG_DIR="TOLOG_DB_LOG_DIR"
#
#
#token = os.getenv(TOKEN)
#log_dir = os.getenv(LOG_DIR)




td = t_td.TologDropbox(config.Token, config.Log_dir)

tf = t_f.TologFunctions(td)

d = "991231"
tags = ["@hoge", "@test"]
text = "logのてきすとだょ"

print(tf.appendLog(d, tags, text))
