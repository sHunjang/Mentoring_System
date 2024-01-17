import pymysql

# Database 연결 세부 정ㅗ
DB = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='Mentoring', charset='utf8')
cursor = DB.cursor()

# Companies 테이블 조회 함수
def Companies_Table_Check():
    cursor.execute("SELECT * FROM Companies")
    rows = cursor.fetchall()
    print("'Companies' 테이블 데이터 조회 : ")
    for row in rows:
        print(row)
    
    return rows


# 기업 별 직무 테이블 데이터 조회
def Job_Position_Check():
    cursor.execute("SELECT * FROM Company_Job_Positions")
    rows = cursor.fetchall()
    print("'Job_Position' 테이블 데이터 조회 : ")
    for row in rows:
        print(row)
        
    return rows

# 기술 분류 테이블 데이터 조회
def Skill_Category_Check():
    cursor.execute("SELECT * FROM SKILLS")
    rows = cursor.fetchall()
    print("'SKILLS' 테이블 데이터 조회 : ")
    for row in rows:
        print(row)
    
    return rows
