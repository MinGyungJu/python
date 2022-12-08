import cx_Oracle as oci
import csv

def createDBTable():
    # 1.연결객체 얻어오기
    conn = oci.connect('scott/tiger@192.168.0.69:1521/xe')

    # 2.sql 문장
    sql ="""
    create table supply
    (
     id             number  primary key,
     Supplie_Name   varchar2(50),
     Invoice_Number varchar2(50),
     Part_Number    varchar2(30),
     Cost           number,
     Purchase_Date  date
     )
    """
    # 3.cursor 객체 얻어오기

    cursor = conn.cursor()

    # 4. 실행
    cursor.execute(sql)

    sql2 = 'create sequence seq_supply_id'
    cursor.execute(sql2)
    # 5.cursor객체 닫기
    cursor.close()

    # 6.연결객체닫기
    conn.close()

def saveDBTable(data):
    # 1.연결객체 얻어오기
    conn = oci.connect('scott/tiger@192.168.0.69:1521/xe')

    # 2.sql 문장
    sql = """
        Insert Into supply
        values(seq_supply_id.NEXTVAL, :0,:1,:2,:3,:4)
        """
    # 3.cursor 객체 얻어오기

    cursor = conn.cursor()

    # 4. 실행
    cursor.execute(sql,data)

    # 5.cursor객체 닫기
    cursor.close()
    conn.commit() #잊지말자

    # 6.연결객체닫기
    conn.close()

def viewDBTable(data):
    # 1.연결객체 얻어오기
    conn = oci.connect('scott/tiger@192.168.0.69:1521/xe')

    # 2.sql 문장
    sql = """
           Select * from supply
           """
    # 3.cursor 객체 얻어오기

    cursor = conn.cursor()

    # 4. 실행
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    # 5.cursor객체 닫기
    cursor.close()
    conn.commit()  # 잊지말자

    # 6.연결객체닫기
    conn.close()


if __name__ == '__main__':

    #(1) 테이블 생성
    # createDBTable()

    #(2-0) 입력확인
    # imsi = ['kosmo','9999','8888',1000,'2022-12-24']
    # saveDBTable(imsi)

    #(2) CSV 파일을 읽어서 -> db입력

    # file = open('supply.csv','r')
    # datas =csv.reader(file)
    # # print(datas)
    # header = next(datas, None)
    # print(header)
    # print('-'*50)
    # for row in datas:
    #     # print(row)
    #     saveDBTable(row)

    # (3) 테이블 내용 출력

    viewDBTable('supply')