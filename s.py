# -*- coding: UTF-8 -*-
__author__ = 'Administrator'
#socket_client.py
import socket
import time

def socket_send(command):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 11100))
    sock.send(command)
    result = sock.recv(2048)
    sock.close()
    return result

if __name__ == '__main__':
    print socket_send('date "+%Y-%m-%d %H:%M:%S"')
#    tt = raw_input("please reboot>>")
    vng = raw_input('please enter reboot or modify date,like 2013-10-21 21:33:33 >>')
    print vng

    vngformat = time.mktime(time.strptime(vng,'%Y-%m-%d %H:%M:%S'))
    print vngformat
    ct = socket_send('date +%s')
    print 'ct is %s' %  ct
#    ctformt = time.mktime(time.strptime(int(ct),'%Y-%m-%d %H:%M:%S'))
#    print 'ctformat is %s' % ctformt

    if vng == '2013-12-12 12:00:00':
        print socket_send('cd /data/game/qmrserver10002/qmrserver && /bin/sh stop.sh') #关闭服务器
        time.sleep(45)
        print socket_send('cd /data/game/qmrserver10002/qmrserver && /bin/sh start.sh') #开启服务器
        time.sleep(30)
        print socket_send('cd /data/game/qmrserver10002/qmrserver && /bin/sh checkserver.sh -ct') #检查是否开启成功
    else:
        if vngformat < ct:
             print socket_send('date -s "%s"' % vng)
        else:
             print socket_send('cd /data/game/qmrserver10002/qmrserver && /bin/sh stop.sh') #关闭服务器
             time.sleep(45)
             print socket_send('date -s "%s"' % vng)
             print socket_send('cd /data/game/qmrserver10002/qmrserver && /bin/sh start.sh') #开启服务器
             time.sleep(30)
             print socket_send('cd /data/game/qmrserver10002/qmrserver && /bin/sh checkserver.sh -ct') #检查是否开启成功



#    print socket_send('date -s "2013-10-15 23:59"')
#   print socket_send('date -s')
#    print socket_send('cd /data/game/qmrserver10002/qmrserver && /bin/sh stop.sh') #关闭服务器
#    print socket_send('cd /data/game/qmrserver10002/qmrserver && /bin/sh checkserver.sh -cp') #检查关闭是否成功
#    print socket_send('cd /data/game/qmrserver10002/qmrserver && /bin/sh start.sh') #开启服务器
    print socket_send('cd /data/game/qmrserver10002/qmrserver && /bin/sh checkserver.sh -ct') #检查是否开启成功




