import os
import SJ_eleven
import time
Error = "잘못된 입력입니다. 다시 입력해주세요."
cont = "계속 진행하려면 Enter를 입력해주세요."
def real_main():
    os.system('cls')
    UI()
    L = ["1","2","3"] #예외처리용
    num = 0 #예외처리용
    while(num !=3):
        print("SEOJUN ELEVEN에 오신 것을 환영합니다.")
        print("1. 로그인하기")
        print("2. 회원가입하기")
        print("3. 프로그램 종료")
        #예외처리 - 이 구문 끝나면 숫자 입력 완료
        a = input("입력 :")
        while(a not in L):
            print("1-3의 정수를 입력해 주세요.")
            a = input("입력 :")
        num = int(a)
        if(num == 1):
            Main()
        if(num==2):
            SJ_eleven.register()
            os.system('cls')
            UI()
        else:
            exit()
    print("프로그램을 종료합니다.")
    exit()


def Main():
    os.system('cls')
    print("===== WELCOME TO SEOJUN ELEVEN =====")
    print("로그인을 해주세요.")
    id = input("아이디 : ")
    passwd = input("비밀번호 : ")
    tempid = SJ_eleven.login(id,passwd)

    while(tempid == ""):
        print("id 혹은 비밀번호가 잘못되었습니다.")
        id = input("아이디 : ")
        passwd = input("비밀번호 : ")
        tempid = SJ_eleven.login(id,passwd)
    if(tempid == "admin"):
        admin_menu()
    else:
        user_menu(tempid)

#메뉴 UI
def admin_UI():
    os.system('cls')
    print("===== WELCOME TO SEOJUN ELEVEN =====")
    print("1. 품목 리스트 출력")
    print("2. 품목 추가")
    print("3. 부족한 품목 주문하기")
    print("4. 로그아웃")
    
def admin1():#품목 리스트 출력
    os.system('cls')
    SJ_eleven.select()
    input(cont)
    
    #SJ_eleven.select()
def admin2():#품목 추가
    os.system('cls')

    L = input("추가할 품목을 입력해주세요.(상품명, 수량, 가격)").split() #품목
    if("exit" in L):
        return
    while(len(L)!=3):
        print(Error)
        L = input("추가할 품목을 입력해주세요.(상품명, 수량, 가격)").split() #2개 입력됨
        if("exit" in L):
            return

    S = SJ_eleven.add(L[0],L[1],L[2])
    if(S == "X"):
        print(Error)
        admin2()

    
def admin3():
    os.system('cls')
    print("=========================")
    print("부족한 품목 주문하기")
    print('품목 현황(재고 적은 순)')
    SJ_eleven.order()
    input("필요 재고를 보려면 Enter를 눌러주세요")
    
    os.system('cls')
    print("=========================")
    print("필요 재고 현황")
    SJ_eleven.order2()
    A = input("필요 재고를 주문하시겠습니까?(Y/N)")
    while(A not in ["Y","N"]):
        print(Error)
        A = input("필요 재고를 주문하시겠습니까?(Y/N)")
    if(A == "Y"):
        SJ_eleven.order3()
    elif(A == "N"):
        print("부족 품묵 주문하기를 종료합니다.")
        return

def user_UI(userid):
    
    os.system('cls')
    print(userid,"님 환영합니다. SEOJUN ELEVEN입니다.")
    print("1. 품목 구매")
    print("2. 로그아웃")

def user1():
    admin1()
    print("============= 물품 구매하기 ============")
    print("exit를 입력할때까지 구매가 진행됩니다.")
    code = ""
    while(code != "exit"):
        code = input("구매할 품목 코드를 입력해주세요 : ")
        if(code == "exit"):
            return
        while(SJ_eleven.find(code)==""):

            print(Error)
            code = input("구매할 품목 코드를 입력해주세요 : ")
            if code == "exit":
                return
        num = input("수량을 입력해주세요 : ")
        A  = 0
        while(A == 0):
            try:
                num = int(num)
                A+=1
            except:
                print(Error)
                num = input("수량을 입력해주세요 : ")
        for a in range(0,num):
            str = SJ_eleven.buy(code)
            if(str == "X"):
                print("수량이 부족하여",a,"개만 구매하였습니다.")
                break

def admin_menu():
    
    L = ["1","2","3","4"] #예외처리용
    num = 0 #예외처리용
    while(num !=4):
        admin_UI()
        #예외처리 - 이 구문 끝나면 숫자 입력 완료
        a = input("입력 : ")
        while(a not in L):
            print("1-4의 정수를 입력해 주세요.")
            a = input("입력 : ")
        num = int(a)
        if(num == 1):
            admin1()
        if(num==2):
            admin2()
        if(num ==3):
            admin3()
    input("Enter를 누르면 로그아웃을 진행합니다.")
    return real_main()

def user_menu(userid):
    L = ["1","2"] #예외처리용1

    num = 0 #예외처리용
    while(num !=2):
        user_UI(userid)
        #예외처리 - 이 구문 끝나면 숫자 입력 완료
        a = input("입력 :")
        while(a not in L):
            print("1-2의 정수를 입력해 주세요.")
            a = input("입력 :")
        num = int(a)
        if(num == 1):
            user1()
    input("Enter를 누르면 로그아웃을 진행합니다.")
    return real_main()

def UI():
    print("""
□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□
□□□■■■■□■■■■■□□■■■□□□□□■□□■□□□■□■□□□■□□□□□□■■■■■□□■□□□□■■■■■□■□□□■□■■■■■□■□□□■□□
□□■□□□□□■□□□□□■□□□■□□□□■□□■□□□■□■■□□■□□□□□□■□□□□□□■□□□□■□□□□□■□□□■□■□□□□□■■□□■□□
□□□■■■■□■■■■■□■□□□■□□□□■□□■□□□■□■□■□■□□□□□□■■■■■□□■□□□□■■■■■□■□□□■□■■■■■□■□■□■□□
□□□□□□■□■□□□□□■□□□■□□■□■□□■□□□■□■□□■■□□□□□□■□□□□□□■□□□□■□□□□□□■□■□□■□□□□□■□□■■□□
□□■■■■□□■■■■■□□■■■□□□□■□□□□■■■□□■□□□■□□□□□□■■■■■□□■■■■□■■■■■□□□■□□□■■■■■□■□□□■□□
□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□
"""

    )


real_main()
