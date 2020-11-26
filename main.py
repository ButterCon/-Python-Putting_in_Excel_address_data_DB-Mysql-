from code.xl_input import xl_input
from code.enter_address_mysql import enter_address_mysql

if __name__ == "__main__":
    print("main")
    address = xl_input()
    enter_address_mysql(address)

