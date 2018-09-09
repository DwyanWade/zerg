"""
Created on 2018/9/5 13:47

"""
import datetime
import random
import time

__Author__ = '阿强'


def generator_order_no():
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    a = random.randint(65, 90)
    b = random.randint(97, 122)
    c = chr(a)
    d = chr(b)

    return c + str(random.randint(100, 999)) + str(random.randint(100, 999)) + str(now_time) + d


def timestamp_to_localtime(timestamp):
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt
