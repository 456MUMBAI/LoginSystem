#registration file
import mysql.connector as ms

mycon = ms.connect(host='db4free.net', user='clairie', passwd='education', charset='utf8', database='skytouch')
if mycon.is_connected():
    print('connected!')