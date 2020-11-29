from code.xl_input import xl_input
from code.enter_address_mysql import enter_address_mysql

if __name__ == "__main__":
    print("프로그램 시작")
    address = xl_input()
    print("excel 데이터 가져옴")
    enter_address_mysql(address)
