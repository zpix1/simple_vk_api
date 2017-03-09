import vk
import sys
import time
import json
import threading
import utils as u
params = u.json_read('params.json')
session = vk.AuthSession(app_id=params["app_id"], user_login=params["user_login"], user_password=params["user_password"], scope=params["scope"])
api = vk.API(session)
_symbs = [' ',' ']
_no_spam_trigger = 0

def sleep(secs):
    time.sleep(secs)

def on_message_listener(listener,time_interval):
    def tread_func(listener,time_interval):
        while True:
            n = 1
            me = api.messages.get(count=n)
            if(len(me) > 1):
                for i in range(1, len(me)):
                    if me[i]['read_state']==0:
                        api.messages.markAsRead(message_ids=str(me[i]['mid']))
                        listener(me[i])
            time.sleep(time_interval)
    t1 = threading.Thread(target=tread_func, args=(listener,time_interval))
    t1.start()
    return t1
def send_message(user_id,message):
    global _no_spam_trigger
    _no_spam_trigger = (_no_spam_trigger+1)%len(_symbs)
    api.messages.send(user_id=user_id,message=message+_symbs[_no_spam_trigger])
def wall_post(owner_id,text):
    api.wall.post(owner_id=owner_id,message=text)