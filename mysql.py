import pymysql
import sys
import random
	
host = "localhost"
user = "root"
passwd = ""
database = "newshop"

def SelectAll(tableName):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "Select * from "+tableName

    #executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    rows = list(rows)
    random.shuffle(rows)
    connection.close()
    return rows

def SelectAllProductA_Z():
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT * FROM `product` ORDER BY `NAME` ASC;"

    #executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    return rows
def RemoveProductById(id):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "DELETE FROM `product` WHERE ID = '{id}'".format( id = id)
    cursor.execute(retrive)
    connection.commit()

def InsertNewCategory(catename):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "INSERT INTO `categories`(`CATEGORY_ID`, `CATEGORY`) VALUES ('','{name}')".format( name = catename)
    cursor.execute(retrive)
    connection.commit()

def SelectAllCategoryWithId():
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT * FROM `categories` "

	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    connection.close()
    return rows

def SelectAllCategory():
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT `CATEGORY` FROM `categories` "

	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    connection.close()
    return rows

def SelectFromCategory(nameCategory):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT CATEGORY_ID FROM `categories` WHERE CATEGORY = " + "'" + nameCategory + "'" 
	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    cateID = rows[0][0]
    retrive = "SELECT * FROM `product` WHERE CATEGORY_ID = " + "'" + str(cateID) + "'"
    cursor.execute(retrive)
    rows = cursor.fetchall()
    rows = list(rows)
    random.shuffle(rows)
    connection.close()
    return rows

def SelectFromText(text):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT * FROM `product` WHERE NAME LIKE" + "'%" + text + "%'"

	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    connection.close()
    return rows

def ValidatePass(email , passw):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT * FROM `usermanager` WHERE E_MAIL = " + "'" + email + "' AND PASS = " + "'" + passw  + "'"

	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    connection.close()
    return rows

def SelectUserNameFromEmail(email):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT USER_NAME FROM `userinfo` WHERE E_MAIL =" + "'" + email + "'" 

	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    connection.close()
    return rows

def SelectProductFromCart(UserName):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT E_MAIL FROM `userinfo` WHERE USER_NAME = '{name}' ".format(name = UserName)
    # print(retrive)
	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    email = rows[0][0]
    retrive = "SELECT ID FROM `usermanager` WHERE E_MAIL = '{email}'".format(email = email)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    id = rows[0][0]
    retrive = " SELECT ID_ITEM FROM `cart` WHERE ID_CART = '{id}'".format(id = id)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return ();
    id_item = rows[0][0]
    retrive = "SELECT `ID_PRODUCT`, `AMOUNT` FROM `all_item_order` WHERE ID_ITEM = '{id_item}'".format(id_item = id_item)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return ();
    listdata = []
    listitem = rows
    # for i in listitem:# listitem[0] = "id" ; listitem[1]= amount
    #     print(i)
    for i in range(0,len(listitem)):          
        retrive = "SELECT * FROM `product` WHERE ID = '{proid}'".format(proid = listitem[i][0])
        cursor.execute(retrive)
        rows = cursor.fetchall()
        item = []
        item.append(rows[0][2])
        item.append(listitem[i][1])
        item.append(rows[0][1])
        item.append(rows[0][3])
        item.append(listitem[i][0])
        listdata.append(item)
    return listdata

def FindProductFromCart(UserName, idpro):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT E_MAIL FROM `userinfo` WHERE USER_NAME = '{name}' ".format(name = UserName)
    # print(retrive)
	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    email = rows[0][0]
    retrive = "SELECT ID FROM `usermanager` WHERE E_MAIL = '{email}'".format(email = email)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    id = rows[0][0]
    retrive = " SELECT ID_ITEM FROM `cart` WHERE ID_CART = '{id}'".format(id = id)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return False
    id_item = rows[0][0]
    retrive = "SELECT ID_PRODUCT FROM `all_item_order` WHERE ID_ITEM = '{id_item}'".format(id_item = id_item)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows) == 0):
        return False
    retrive = "SELECT ID_PRODUCT FROM `all_item_order` WHERE ID_PRODUCT = '{idpro}'".format(idpro = idpro)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows) == 0):
        return False
    else:
        return True


def InsertItemToCart(UserName, idpro):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT E_MAIL FROM `userinfo` WHERE USER_NAME = '{name}' ".format(name = UserName)
    # print(retrive)
	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    email = rows[0][0]
    retrive = "SELECT ID FROM `usermanager` WHERE E_MAIL = '{email}'".format(email = email)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    id = rows[0][0]
    retrive = " SELECT ID_ITEM FROM `cart` WHERE ID_CART = '{id}'".format(id = id)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows) == 0):
        retrive = "INSERT INTO `cart`(`ID_CART`, `ID_ITEM`) VALUES ('{id}','{id}')".format(id = id)
        cursor.execute(retrive)
        connection.commit()

        retrive = "SELECT `ID_ITEM` FROM `cart` WHERE ID_CART = '{id}'".format(id = id)
        cursor.execute(retrive)
        rows = cursor.fetchall()

        retrive = "INSERT INTO `all_item_order`(`ID`, `ID_ITEM`, `ID_PRODUCT`, `AMOUNT`) VALUES ('','{id_i}','{id}','1')".format(id_i = rows[0][0], id = idpro)
        cursor.execute(retrive)
        connection.commit()
    else:
        retrive = "SELECT `ID_ITEM` FROM `cart` WHERE ID_CART = '{id}'".format(id = id)
        cursor.execute(retrive)
        rows = cursor.fetchall()
        retrive = "INSERT INTO `all_item_order`(`ID`, `ID_ITEM`, `ID_PRODUCT`, `AMOUNT`) VALUES ('','{id_i}','{id}','1')".format(id_i = rows[0][0], id = idpro)
        print(retrive)
        cursor.execute(retrive)
        connection.commit()
    return True

def CreateNewCustomer(First, Last, UserName, Email, Phone, Password):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    
    retrive = "INSERT INTO `userinfo`(`E_MAIL`, `FIRST_NAME`, `LAST_NAME`, `USER_NAME`, `PHONE_NUMBER`) VALUES ('{email}','{first}','{last}','{username}','{phone}')".format(email = Email, first = First, last = Last, username = UserName, phone = Phone)
    cursor.execute(retrive)
    connection.commit()

    retrive = "INSERT INTO `usermanager`(`ID`, `E_MAIL`, `PASS`, `PRIORITY`) VALUES ('','{email}','{password}','0')".format(email = Email, password = Password)
    cursor.execute(retrive)
    connection.commit()
    return True

def GetAmountProductInCart(UserName):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()

    retrive = "SELECT E_MAIL FROM `userinfo` WHERE USER_NAME = '{name}' ".format(name = UserName)
    # print(retrive)
	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    email = rows[0][0]
    retrive = "SELECT ID FROM `usermanager` WHERE E_MAIL = '{email}'".format(email = email)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    id = rows[0][0]
    retrive = " SELECT ID_ITEM FROM `cart` WHERE ID_CART = '{id}'".format(id = id)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return 0;
    id_item = rows[0][0]
    retrive = " SELECT COUNT(ID_ITEM) FROM `all_item_order` WHERE ID_ITEM = '{id_item}'".format(id_item = id_item)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return 0;
    connection.close()
    return rows[0][0]

def GetProductFromId(id):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT * FROM `product` WHERE ID = '{id}' ".format(id = id)

	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    connection.close()
    return rows

def RemoveProductInCartById(UserName, idpro):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT E_MAIL FROM `userinfo` WHERE USER_NAME = '{name}' ".format(name = UserName)
    # print(retrive)
	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    email = rows[0][0]
    retrive = "SELECT ID FROM `usermanager` WHERE E_MAIL = '{email}'".format(email = email)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    id = rows[0][0]
    retrive = " SELECT ID_ITEM FROM `cart` WHERE ID_CART = '{id}'".format(id = id)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return 0;
    id_item = rows[0][0]
    retrive = "DELETE FROM `all_item_order` WHERE ID_ITEM = '{iditem}' AND ID_PRODUCT = '{idpro}'".format(iditem = id_item, idpro = idpro)
    cursor.execute(retrive)
    connection.commit()

def IncreaseAmountInCardById(UserName, idpro):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT E_MAIL FROM `userinfo` WHERE USER_NAME = '{name}' ".format(name = UserName)
    # print(retrive)
	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    email = rows[0][0]
    retrive = "SELECT ID FROM `usermanager` WHERE E_MAIL = '{email}'".format(email = email)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    id = rows[0][0]
    retrive = " SELECT ID_ITEM FROM `cart` WHERE ID_CART = '{id}'".format(id = id)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return 0;
    id_item = rows[0][0]
    retrive = "update all_item_order set AMOUNT = AMOUNT + 1 where ID_ITEM = '{id_item}' AND ID_PRODUCT = '{idpro}'".format(id_item = id_item, idpro = idpro)
    cursor.execute(retrive)
    connection.commit()
    return True


def DecreaseAmountInCardById(UserName, idpro):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT E_MAIL FROM `userinfo` WHERE USER_NAME = '{name}' ".format(name = UserName)
    # print(retrive)
	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    email = rows[0][0]
    retrive = "SELECT ID FROM `usermanager` WHERE E_MAIL = '{email}'".format(email = email)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    id = rows[0][0]
    retrive = " SELECT ID_ITEM FROM `cart` WHERE ID_CART = '{id}'".format(id = id)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return 0;
    id_item = rows[0][0]
    retrive = "SELECT AMOUNT FROM `all_item_order` WHERE ID_PRODUCT = '{idpro}'".format(idpro = idpro)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(rows[0][0] > 1):
        retrive = "update all_item_order set AMOUNT = AMOUNT - 1 where ID_ITEM = '{id_item}' AND ID_PRODUCT = '{idpro}'".format(id_item = id_item, idpro = idpro)
        cursor.execute(retrive)
        connection.commit()
    return True

def SelectProductById(id):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT * FROM `product` WHERE ID = '{id}'".format(id = id)

	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    connection.close()
    return rows
    
def GetNameCategory(id):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT `CATEGORY` FROM `categories` WHERE CATEGORY_ID = '{id}'".format(id = id)

	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    connection.close()
    return rows[0][0]

# def GetIdFromCartByID(UserName, id):
#     connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
#     cursor = connection.cursor()
#     retrive = "SELECT `ID` FROM `{name}_cart` WHERE PRODUCT_ID = '{id}'".format(name = UserName , id = id)

#     #executing the quires
#     cursor.execute(retrive)
#     rows = cursor.fetchall()
#     connection.close()
#     return rows[0][0]

def GetNumberCustomer():
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT COUNT(PRIORITY) FROM `usermanager` WHERE PRIORITY = '0'"

    #executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    connection.close()
    return rows[0][0]

def GetNumberProduct():
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT COUNT(*) FROM `product` WHERE 1"

    #executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    connection.close()
    return rows[0][0]

def GetInfoCustomerForAdmin():
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT `ID`, `E_MAIL` FROM `usermanager` WHERE 1"

    #executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    listuser = []
    for i in range(0,len(rows)):
        temp = []
        temp.append(rows[i][0])
        retrive = "SELECT `USER_NAME`, `PHONE_NUMBER` FROM `userinfo` WHERE E_MAIL = '{email}'".format(email = rows[i][1]) 
        cursor.execute(retrive)
        rowss = cursor.fetchall()
        temp.append(rowss[0][0])
        temp.append(rowss[0][1])
        temp.append(rows[i][1])
        listuser.append(temp)
    connection.close()
    return listuser

def AddNewProduct(name, img, price, cateid, des):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "INSERT INTO `product`(`ID`, `NAME`, `IMAGE`, `PRICE`, `RATING`, `CATEGORY_ID`, `DESCRIPTON`) VALUES ('','{name}','{img}','{price}','{rating}','{cate}','{des}')".format(name = name, img = img, price = price, rating = 5.0, cate = cateid, des = des)
    cursor.execute(retrive)
    connection.commit()

def GetIdProductAndAmountInCart(UserName):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()

    retrive = "SELECT E_MAIL FROM `userinfo` WHERE USER_NAME = '{name}' ".format(name = UserName)
    # print(retrive)
	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    email = rows[0][0]
    retrive = "SELECT ID FROM `usermanager` WHERE E_MAIL = '{email}'".format(email = email)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    id = rows[0][0]
    retrive = " SELECT ID_ITEM FROM `cart` WHERE ID_CART = '{id}'".format(id = id)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return [];
    id_item = rows[0][0]
    retrive = " SELECT `ID_PRODUCT`, `AMOUNT` FROM `all_item_order` WHERE ID_ITEM = '{id_item}'".format(id_item = id_item)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return [];
    connection.close()
    return rows

def InserToOrder(info_order, UserName):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()

    retrive = "INSERT INTO `order`(`ID`, `USER_NAME`, `ADDRESS`, `INFO_CART`) VALUES ('','{name}','','{info}')".format(name = UserName, info = info_order)
    cursor.execute(retrive)
    connection.commit()

def SelectOrder():
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT `USER_NAME`,`INFO_CART` FROM `order` WHERE 1"
    cursor.execute(retrive)
    rows = cursor.fetchall()
    data = []
    if(len(rows) != 0):
        numorder = len(rows)
        totalprice = []
        for i in rows:
            # print("Cart of {name}".format(name = i[0]))
            datapro = i[1]
            totalpro = datapro.split('/')
            num = len(totalpro) - 1
            toto = 0
            for j in totalpro:
                if(num > 0):
                    idpro = j[0:j.find('x')]
                    amount = j[j.find('x')+1:len(j)]
                    proprice = GetProductFromId(idpro)[0][3]
                    tprice = proprice*float(amount)
                    toto  = toto + tprice
                    # print("--->Id product: {id} {price}\t Amount {amount} \t total {to}".format(id = idpro, price = proprice, amount = amount, to = tprice))
                num = num - 1
            # print("total: {t}".format(t = toto))
            totalprice.append(toto)
        for i in range(0,numorder):
            temp = []
            temp.append(rows[i][0])
            temp.append(totalprice[i])
            data.append(temp)
        return data
    return []

def GetNumberOrder():
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()
    retrive = "SELECT COUNT(ID) FROM `order` WHERE 1"
    cursor.execute(retrive)
    rows = cursor.fetchall()
    return rows[0][0]

def DeleteCart(UserName):
    connection = pymysql.connect(host=host , user=user, passwd=passwd, database=database)
    cursor = connection.cursor()

    retrive = "SELECT E_MAIL FROM `userinfo` WHERE USER_NAME = '{name}' ".format(name = UserName)
    # print(retrive)
	#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    email = rows[0][0]
    retrive = "SELECT ID FROM `usermanager` WHERE E_MAIL = '{email}'".format(email = email)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    id = rows[0][0]
    retrive = "DELETE FROM `all_item_order` WHERE ID_ITEM = '{id}'".format(id = id)
    cursor.execute(retrive)
    connection.commit()
    retrive = "DELETE FROM `cart` WHERE ID_CART = '{id}'".format(id = id)
    cursor.execute(retrive)
    connection.commit()

