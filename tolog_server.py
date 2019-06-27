import falcon
import json
import tolog_to_dropbox as t_td
import tolog_functions as t_f
import tolog_config as t_conf


class TologServer(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "tolog is not dead"


class TologAppendLog(object):
    def on_post(self, req, resp):
        # postパラメーターを取得
        body = req.stream.read()
        data = json.loads(body)

        date = data['date']
        tags = data['tags']
        text = data['text']

        config = t_conf.TologConfig()
        td = t_td.TologDropbox(config)
        tf = t_f.TologFunctions(td, config)

        ret = tf.appendLog(date, tags, text)

        resp.body = json.dumps({"message":"success"})

app = falcon.API()

tolog = TologServer()
append_log = TologAppendLog()

app.add_route('/tolog', tolog)
app.add_route('/append_log', append_log)
