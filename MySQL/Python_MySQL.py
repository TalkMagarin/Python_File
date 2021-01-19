# pip install pymysql : MySQL을 연동할 수 있는 라이브러리 설치
import pymysql


"""
MySQL Database로 요청한 Query 명령어를 실행합니다.

in_host: 접속하려는 서버 주소(ex: localhost)
in_user: 아이디(ex: root)
in_password: 비밀번호(ex: root)
in_database: 데이터베이스 이름
in_query_sql: 실행할 명령어(ex: SELECT * FROM db;)
"""
def MySQL_Connect(in_host, in_user, in_password, in_database, in_query_sql):
    conn = pymysql.connect(host=in_host, user=in_user, password=in_password, db=in_database, charset='utf8')
    with conn.cursor() as curs:
        curs.execute(in_query_sql)
    conn.close()


"""
MySQL Database로 요청한 Query 명령어를 실행하여 QuerySet 데이터를 불러옵니다.

in_host: 접속하려는 서버 주소(ex: localhost)
in_user: 아이디(ex: root)
in_password: 비밀번호(ex: root)
in_database: 데이터베이스 이름
in_query_sql: 실행할 명령어(ex: SELECT * FROM db;)
"""
def MySQL_Return_Rows(in_host, in_user, in_password, in_database, in_query_sql):
    conn = pymysql.connect(host=in_host, user=in_user, password=in_password, db=in_database, charset='utf8')
    with conn.cursor() as curs:
        curs.execute(in_query_sql)
        rows = curs.fetchall()
    conn.close()

    return rows
