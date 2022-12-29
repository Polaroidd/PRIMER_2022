import pymysql

def login(id,passwd):
    db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')

    #cursor 생성
    cursor = db.cursor()
    #sql문작성
    sql = """
        select * from user_info;
    """
    cursor.execute(sql)
    result = cursor.fetchall() #한개만 가져오려면 fetchone, 개수 정하려면 괄호 안에 size = 5
    for data in result:
        if(data[0] == id and data[1] == passwd):
            return id
    
    db.commit()
    db.close()
    return ""

def loginn(id):
    db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')

    #cursor 생성
    cursor = db.cursor()
    #sql문작성
    sql = """
        select * from user_info;
    """
    cursor.execute(sql)
    result = cursor.fetchall() #한개만 가져오려면 fetchone, 개수 정하려면 괄호 안에 size = 5
    for data in result:
        if(data[0] == id):
            return id
    
    db.commit()
    db.close()
    return ""


def select():
    db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')

    #cursor 생성
    cursor = db.cursor()
    #sql문작성
    sql = """
        select * from seojun_eleven;
    """
    cursor.execute(sql)
    result = cursor.fetchall() #한개만 가져오려면 fetchone, 개수 정하려면 괄호 안에 size = 5
    print("*********** SEOJUN_ELEVEN 품목 현황 *************")
    print('code\tname\t\tE/A\t가격')
    for data in result:
        if(len(data[1])<8):
            print("{} \t{}  \t{}\t{}원".format(data[0],data[1],data[2],data[3]))
        else:
            print("{} \t{}\t{}\t{}원".format(data[0],data[1],data[2],data[3]))
    #print(result)

    db.commit()#굳이 필요 X
    db.close()

def order():
    db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')

    #cursor 생성
    cursor = db.cursor()
    #sql문작성
    sql = """
        select * from seojun_eleven;
    """
    cursor.execute(sql)
    result = cursor.fetchall() #한개만 가져오려면 fetchone, 개수 정하려면 괄호 안에 size = 5
    print("*********** SEOJUN_ELEVEN 품목 현황 *************")
    print('code\tname\t\tE/A\t가격')
    result = nsjss(result)
    for data in result:
        if(len(data[1])<8):
            print("{} \t{}  \t{}\t{}원".format(data[0],data[1],data[2],data[3]))
        else:
            print("{} \t{}\t{}\t{}원".format(data[0],data[1],data[2],data[3]))
    #print(result)

    db.commit()#굳이 필요 X
    db.close()
def order2():
    db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')

    #cursor 생성
    cursor = db.cursor()
    #sql문작성
    sql = """
        select * from seojun_eleven;
    """
    cursor.execute(sql)
    result = cursor.fetchall() #한개만 가져오려면 fetchone, 개수 정하려면 괄호 안에 size = 5
    print("*********** SEOJUN_ELEVEN 품목 현황 *************")
    print('code\tname\t\tE/A\t가격')
    result = nsjss(result)
    for data in result:
        if(20-data[2]>0):
            if(len(data[1])<8):
                print("{} \t{}  \t{}\t{}원".format(data[0],data[1],20-data[2],data[3]))
            else:
                print("{} \t{}\t{}\t{}원".format(data[0],data[1],20-data[2],data[3]))
    #print(result)

    db.commit()#굳이 필요 X
    db.close()

def order3():
    print("부족한 재고를 주문 완료하였습니다.")
    db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')

    #cursor 생성
    cursor = db.cursor()
    #sql문작성
    sql = """
        update seojun_eleven set EA = 20 where EA <20;
    """
    cursor.execute(sql)
    result = cursor.fetchall() #한개만 가져오려면 fetchone, 개수 정하려면 괄호 안에 size = 5

    
    db.commit()#굳이 필요 X
    db.close()
    select()

def insert(): #insert문
    db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')
    #cursor 생성
    cursor = db.cursor()
    #sql문작성
    sql = """
        insert into seojun_eleven (name,EA,cost) values ("worldcon",21,1300);
    """
    cursor.execute(sql)
    db.commit()

    db.close()
def find(code):
    db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')

    #cursor 생성
    cursor = db.cursor()
    #sql문작성
    sql = """
        select * from seojun_eleven;
    """
    cursor.execute(sql)
    result = cursor.fetchall() #한개만 가져오려면 fetchone, 개수 정하려면 괄호 안에 size = 5
    
    for data in result:
        if(str(data[0]) ==code):
            db.commit()#굳이 필요 X
            db.close()
            return data[1]
    db.commit()#굳이 필요 X
    db.close()
    return ""
            
    #print(result)

    db.commit()#굳이 필요 X
    db.close()

def buy(code): #insert문
    db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')
    #개수 가져오기
    cursor = db.cursor()
    #sql문작성
    sql = """
        select EA from seojun_eleven where item_code =
    """
    sql += code
    sql += ";"

    cursor.execute(sql)
    result = cursor.fetchone()
    k = result[0]
    num = int(k)
    if(num == 0):
        return "X"
    else:
        num -=1
        #cursor 생성
        cursor = db.cursor()
        #sql문작성
        sql = """
            update seojun_eleven set EA = 
        """
        sql += str(num)
        sql += " where item_code = "
        sql += code
        sql += ";"
        cursor.execute(sql)
        db.commit()
        db.close()

def register():#회원가입
    id = input("아이디를 입력해주세요 : ")
    while(loginn(id) != ""):
        print("이미 존재하는 아이디입니다. 다시 입력해주세요.")
        id = input("아이디를 입력해주세요 : ")
        if(id == "exit"):
            return
    
    passwd = input("비밀번호를 입력해주세요 : ")
    repass = input("비밀번호를 한 번 더 입력해주세요 : ")
    while(passwd != repass):
        repass = input("비밀번호를 한 번 더 입력해주세요 : ")
        if(repass == "exit"):
            return
    if id == "" or passwd == "":
        return
    db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')

    #cursor 생성
    cursor = db.cursor()
    #sql문작성
    sql = "insert into user_info values('"+id+"', '"+passwd+"');"

    cursor.execute(sql)
    
    db.commit()
    db.close()

def nsjss(tpl):
    arr = list(tpl)
    for a in range(0,len(arr)):
        minix = a
        for b in range(0,len(arr)):
            if a<b:
                if arr[minix][2] > arr[b][2]:
                    minix = b
        temp = arr[a]
        arr[a] = arr[minix]
        arr[minix] = temp
    return arr

def add(name, temp_num, temp_cost):#회원가입
    num = 0
    cost = 0
    try:
        cost = int(temp_cost)
    except:
        return "X"
    try:
        num = int(temp_num)
    except:
        return "X"
    if(cost <0 or num<0):
        return "X"
    
    if(find(name) != ""): #품목 수량 추가
        add2(name,num)
        print("수량 추가가 완료되었습니다.")
        return
    else:
    

        db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')

        #cursor 생성
        cursor = db.cursor()
        #sql문작성
        sql = "insert into seojun_eleven(name, EA, cost) values('"+name+"', "+str(num)+","+str(cost)+");"

        cursor.execute(sql)
        
        db.commit()
        db.close()

def add2(name, n):
    db = pymysql.connect(host = 'localhost', port = 3307, db = 'nsj', user = 'root', passwd = 'noh10309', autocommit = True, charset = 'utf8')
    #개수 가져오기
    cursor = db.cursor()
    #sql문작성
    sql = "select EA from seojun_eleven where name ="
    sql += name
    sql += ";"

    cursor.execute(sql)
    result = cursor.fetchone()
    k = result[0]
    
    num = int(k)
    
    num += n
        #cursor 생성
    cursor = db.cursor()
        #sql문작성
    sql = """
            update seojun_eleven set EA = 
        """
    sql += str(num)
    sql += " where name = "
    sql += name
    sql += ";"
    cursor.execute(sql)
    db.commit()
    db.close()
