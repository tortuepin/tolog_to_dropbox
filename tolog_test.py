import os
import sys
import tolog_to_dropbox as t_td
import tolog_functions as t_f
import tolog_config as t_conf

config = t_conf.TologConfig()



td = t_td.TologDropbox(config)

tf = t_f.TologFunctions(td, config)

d = "991231"
tags = ["@hoge", "@test"]
text = "logのてきすとだょ"

print(tf.appendLog(d, tags, text))
