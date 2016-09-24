# encoding=utf-8

import top.api
import requests
import re
import time

ISO_TIME_FORMAT = '%Y-%m-%d %X'


# 阿里云信息发送API调用
def send_message():
    req=top.api.AlibabaAliqinFcSmsNumSendRequest("gw.api.taobao.com", 80)
    req.set_app_info(top.appinfo(23460289, "1e012cc5a9db0c209a6d010724e54b22"))
    req.sms_type="normal"
    req.sms_free_sign_name="王帅鹏"
    req.rec_num="13937463312"
    req.sms_template_code="SMS_15220019"
    try:
        resp = req.getResponse()
        print(resp)
    except Exception, e:
        print(e)


# 阿里云电话通知API调用
def call_me():
    req = top.api.AlibabaAliqinFcTtsNumSinglecallRequest("gw.api.taobao.com",80)
    req.set_app_info(top.appinfo(23461859,"6d5a2fcf969838b47d6d6e00cc5e54f8"))
    req.extend = ""
    req.tts_param = ""
    req.called_num = "13937463312"
    req.called_show_num = "051482043270"
    req.tts_code = "TTS_15315481"
    try :
        resp = req.getResponse()
        print (resp)
    except Exception,e:
        print (e)


def check_activity():
    time.sleep(3)
    r = requests.get('http://10.104.0.225/forum.php?mod=viewthread&tid=310')
    pattern = re.compile(r'alert_error')
    match = pattern.findall(r.text)
    if match:
        print >>f,time.strftime(ISO_TIME_FORMAT, time.localtime()) + '  failed'
        print time.strftime(ISO_TIME_FORMAT, time.localtime()) + '  failed'
        return 1
    else:
        print >>f,time.strftime(ISO_TIME_FORMAT, time.localtime()) + '  success'
        print time.strftime(ISO_TIME_FORMAT, time.localtime()) + '  success'
        call_me()
        return 0

f = open('out.txt', 'w+')
flag = 1
while flag == 1:
    flag = check_activity()
    print >>f, flag
    print flag
f.close()

