from logging import info
from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.utils import format_string
import mysql as SQL
app = Flask(__name__)


@app.route("/")
def main():
    listproduct = SQL.SelectAll("product")
    listcategory = SQL.SelectAllCategory()
    return render_template('frontend.html', listitem = listproduct,  listcategory =  listcategory)

@app.route("/<category>")
def loadCategory(category):
    listcategory = SQL.SelectAllCategory()
    if(category == "all"):
        listproduct = SQL.SelectAll("product")
        return render_template('Sub-page.html', listitem = listproduct,  listcategory =  listcategory)
    else:
        listproduct = SQL.SelectFromCategory(category)
        return render_template('Sub-page.html', listitem = listproduct,  listcategory =  listcategory)

@app.route('/search/', methods = ['POST'])
def searching():
    listcategory = SQL.SelectAllCategory()
    if request.method == "POST":
        text = request.form.get("search-data")
        listproduct = SQL.SelectFromText(text)
    return render_template('Sub-page.html', listitem = listproduct,  listcategory =  listcategory)

@app.route('/signup')
def render_signup():
    return render_template('SignUpAIShop.html')

@app.route('/signup', methods = ['POST'])
def signup():
    if(request.method == 'POST'):
        first = request.form.get("first_name")
        last = request.form.get("last_name")
        username = request.form.get("user_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        passw = request.form.get("password")
        cpassw = request.form.get("c_password")
        print(first)
        print(last)
        print(username)
        print(email)
        print(phone)
        print(passw)
        print(cpassw)
        if(cpassw != passw):
            return render_template('SignUpAIShop.html', message = "Confirm password doesn't match!")  
        SQL.CreateNewCustomer(first, last, username, email, phone, passw)
        return redirect("/signin")
    
@app.route('/signin')
def render_signin():
    return render_template('SignInAIShop.html')

@app.route('/signin', methods = ['POST'])
def check():
    if request.method == "POST":
        email = request.form.get("Email")
        passw = request.form.get("Password")
        data = SQL.ValidatePass(email, passw)
        if(len(data) == 0):
            return render_template('SignInAIShop.html',  message = "Email or password invalid!")
        if(email == data[0][1] and passw == data[0][2]):
            if(data[0][3] == 1):
                userdata = SQL.SelectUserNameFromEmail(email)
                username = userdata[0][0]
                return redirect("adminpage/" + username)
            else:
                userdata = SQL.SelectUserNameFromEmail(email)
                username = userdata[0][0]
                return redirect("login/" + username)
        return render_template('SignInAIShop.html',  message = "Email or password invalid!")

@app.route('/forgot')
def render_forgot():
    return render_template('forgotpassword.html')

@app.route('/login/<UserName>')
def render_userpage(UserName):
    listproduct = SQL.SelectAll("product")
    listcategory = SQL.SelectAllCategory()
    numpro = SQL.GetAmountProductInCart(UserName)
    return render_template('userpage.html', listitem = listproduct,  listcategory =  listcategory, UserName = UserName, cartAmount = numpro)

@app.route('/login/<UserName>/search/', methods = ['POST'])
def search_user(UserName):
    listcategory = SQL.SelectAllCategory()
    numpro = SQL.GetAmountProductInCart(UserName)
    if request.method == "POST":
        text = request.form.get("search-data")
        listproduct = SQL.SelectFromText(text)
    return render_template('sub_userpage.html', listitem = listproduct,  listcategory =  listcategory, UserName = UserName, cartAmount = numpro)

@app.route("/login/<UserName>/<category>")
def loadCategory_user(UserName, category):
    listcategory = SQL.SelectAllCategory()
    numpro = SQL.GetAmountProductInCart(UserName)
    if(category == "all"):
        listproduct = SQL.SelectAll("product")
        return render_template('sub_userpage.html', listitem = listproduct,  listcategory =  listcategory, UserName = UserName, cartAmount = numpro)
    else:
        listproduct = SQL.SelectFromCategory(category)
        return render_template('sub_userpage.html', listitem = listproduct,  listcategory =  listcategory, UserName = UserName, cartAmount = numpro)

@app.route("/login/<UserName>/cart")
def render_cart(UserName):
    listitem = []
    listproduct = SQL.SelectProductFromCart(UserName)
    total = 0;
    numpro = SQL.GetAmountProductInCart(UserName)
    if(len(listproduct) == 0):
        return render_template("Payment.html", listitem = listitem , total = round(total, 2), UserName = UserName, cartAmount = numpro)
    for item in listproduct:
        price = item[1] * item[3]
        item.append(round(price,2))
        total = total + price
        listitem.append(item)
    for i in listitem:
        print(i)
    return render_template("Payment.html", listitem = listitem , total = round(total, 2), UserName = UserName, cartAmount = numpro)

@app.route("/login/<UserName>/cart/remove/<id>")
def remove(UserName, id):
    SQL.RemoveProductInCartById(UserName,id)
    return redirect("/login/{name}/cart".format(name = UserName))

@app.route("/login/<UserName>/cart/increase/<id>")
def increase(UserName, id):
    SQL.IncreaseAmountInCardById(UserName,id)
    return redirect("/login/{name}/cart".format(name = UserName))

@app.route("/login/<UserName>/cart/decrease/<id>")
def decrease(UserName, id):
    SQL.DecreaseAmountInCardById(UserName,id)
    return redirect("/login/{name}/cart".format(name = UserName))


@app.route("/add/<UserName>/<id>")
def add_item(UserName, id):
    if(SQL.FindProductFromCart(UserName, id)):
        SQL.IncreaseAmountInCardById(UserName, id)
        return redirect("/login/{UserName}".format(UserName = UserName))
    else:
        SQL.InsertItemToCart(UserName, id)
        return redirect("/login/{UserName}".format(UserName = UserName))

@app.route("/login/<UserName>/product/<id>")
def detailPro(UserName, id):
    numpro = SQL.GetAmountProductInCart(UserName)
    data = SQL.SelectProductById(id)
    cate = SQL.GetNameCategory(data[0][5])
    listmore = SQL.SelectFromCategory(cate)
    return render_template("productDetail.html", UserName = UserName, cartAmount = numpro, data = data , cate = cate, listmore = listmore, id = id)

@app.route("/product/<id>")
def detailPro_nonuser(id):
    data = SQL.SelectProductById(id)
    cate = SQL.GetNameCategory(data[0][5])
    listmore = SQL.SelectFromCategory(cate)
    return render_template("productdetail_nonuser.html", data = data , cate = cate, listmore = listmore, id = id)

@app.route("/add/propage/<UserName>/<id>")
def add_item_producpage(UserName, id):
    if(SQL.FindProductFromCart(UserName, id)):
        subid = SQL.GetIdFromCartByID(UserName, id)
        SQL.IncreaseAmountInCardById(UserName, subid)
        return redirect("/login/{UserName}/product/{id}".format(UserName = UserName, id = id))
    else:
        SQL.InsertItemToCart(UserName, id)
        return redirect("/login/{UserName}/product/{id}".format(UserName = UserName, id = id))

@app.route("/adminpage/<UserName>")
def render_adminpage(UserName):
    numberCustomer = SQL.GetNumberCustomer()
    numberProduct = SQL.GetNumberProduct()
    listcustomer =  SQL.GetInfoCustomerForAdmin()
    listorder = SQL.SelectOrder()
    numorder = SQL.GetNumberOrder()
    income = 0
    for i in listorder:
        income = income + float(i[1])
    return render_template('adminpage.html', UserName = UserName, numCustomer = numberCustomer, numProduct = numberProduct, listcustomer = listcustomer, listorder = listorder, numorder = numorder, income = income)

@app.route("/adminpage/<UserName>/productmanager")
def render_productmanager(UserName):
    listproduct = SQL.SelectAllProductA_Z()
    listcate = SQL.SelectAllCategoryWithId()
    return render_template('Product-Cat.html', UserName = UserName, listproduct = listproduct, listcate = listcate)

@app.route("/adminpage/<UserName>/newproduct")
def render_addproduct(UserName):
    listcate = SQL.SelectAllCategoryWithId()
    return render_template('addProduct.html', UserName = UserName , listcate = listcate)

@app.route("/adminpage/<UserName>/newproduct", methods = ['POST'])
def addproduct(UserName):
    if(request.method == "POST"):
        listcate = SQL.SelectAllCategoryWithId()
        proname = request.form.get('name')
        imgpath = request.form.get('img')
        proprice = request.form.get('price')
        catepro = request.form.get('cate')
        despro = request.form.get('des')
        print(proname)
        print(imgpath)
        print(proprice)
        print(catepro)
        print(despro)
        SQL.AddNewProduct(proname, imgpath, proprice, catepro, despro)
    return render_template('addProduct.html', UserName = UserName , listcate = listcate)

@app.route("/adminpage/<UserName>/newproduct/add-category", methods = ['POST'])
def addcategory(UserName):
    listcate = SQL.SelectAllCategoryWithId()
    if(request.method == "POST"):
        catename = request.form.get('name')
        SQL.InsertNewCategory(catename)
    return render_template('addProduct.html', UserName = UserName , listcate = listcate)    
        
@app.route("/adminpage/<UserName>/productmanager/remove/<id>")
def remove_product(UserName, id):
    SQL.RemoveProductById(id)
    return redirect("/adminpage/{UserName}/productmanager".format(UserName = UserName))

@app.route("/adminpage/<UserName>/productmanager/search", methods = ['POST'])
def search_pro(UserName):
    if(request.method == "POST"):
        namesearch = request.form.get('search')
        listproduct = SQL.SelectFromText(namesearch)
        listcate = SQL.SelectAllCategoryWithId()
        return render_template('Product-Cat.html', UserName = UserName, listproduct = listproduct, listcate = listcate)

@app.route("/login/<UserName>/cart/sent")
def sent_order(UserName):
    data = SQL.GetIdProductAndAmountInCart(UserName)
    if(len(data) != 0):
        info_order = ""
        for item in data:
            block = str(item[0]) +"x"+str(item[1])
            info_order = info_order + block + "/"
        SQL.InserToOrder(info_order, UserName)
        SQL.DeleteCart(UserName)
        return redirect("/login/{name}".format(name = UserName))
    return redirect("/login/{name}/cart".format(name = UserName))

if __name__ == "__main__":
    # app.run(host='127.1.0.0', port = "8080") 
    app.run() 