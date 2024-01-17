import pymysql

# DataBaseßœ
db = pymysql.connect(host='localhost', port=3306, user='root', password='', db='Mentoring', charset='utf8')


# DB 연결 닫기
db.close()
