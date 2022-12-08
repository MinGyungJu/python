import cx_Oracle as oci

"""
0. DB에 저장할 테이블 생성
1. 사용자 입력 받아 확인
2. 모든 연락처 출력하기
3. 연락처 삭제하기
"""
class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def createDBTable():
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = '''
        create table info
        (
            name            varchar2(50),
            phone_name      varchar2(30),
            email           varchar2(50),
            addr            varchar2(100)
        )
    '''
    cursor = conn.cursor()
    cursor.execute(sql)

    cursor.close()
    conn.close()

def set_contact():
    # (1)
    # 이름, 전화번호, 이메일, 주소를 입력받아
    name = input('이름은?')
    phone_name = input('전화번호는?')
    email = input('이메일은?')
    addr = input('주소는?')

    # Contact 객체를 생성하고 DB 에 입력
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = "insert into info Values ('{0}', '{1}', '{2}', '{3}')".format(name, phone_name, email, addr)
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.commit()  # 잊지 말자
    conn.close()

def print_contact():
    # (2)
    #  테이블의 전체 레코드 출력
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = """
            select * from info
          """
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print('이름은',row[0])
        print('전화번호는',row[1])
        print('이메일은',row[2])
        print('주소는',row[3])

    cursor.close()
    conn.close()

def delete_contact(name):
    # (3)
    # 해당이름과 같은 요소를 찾아서 삭제


    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = " delete from info where name = '{}'".format(name)

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def run():
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            set_contact()
        elif menu==2: # 출력을 선택하면
            print_contact()
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)


if __name__ == "__main__":
    # createDBTable()
    run()