import mysql.connector
import datetime
from fpdf import FPDF
from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog
from time import strftime
import base64
import io
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="asdfghjkl",
  database="EHTISHAM SIDDIQUI")
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()
mycursor3 = mydb.cursor()
mycursor4 = mydb.cursor()
mycursor5 = mydb.cursor()
mycursor6 = mydb.cursor()
mycursor7 = mydb.cursor()

splash_s=Tk()
splash_s.geometry("400x250+400+250")
#splash_s.title("")
splash_s.overrideredirect(True)
splash_s.configure(background="black")
img1path=Image.open("burger.png")
rimg1=img1path.resize((100,100))
myIMG1=ImageTk.PhotoImage(rimg1)
my_label=Label(image=myIMG1,bg="black")
my_label.place(x=150 , y=30)
# splash_image=Image.open(r"C:\sample2.png")
# splash_image2=ImageTk.PhotoImage(splash_image)
# splash_s.configure(background="red")
splash_s_msg=Label(splash_s,text="FOOD SHOP",bg="black", fg="green3", font="none 20 bold")
splash_s_msg.place(x=112,y=125)
splash_s_msg2=Label(splash_s,text="WELCOME",bg="black", fg="green3", font="none 15 bold")
splash_s_msg2.place(x=150,y=170)

# bg_img=PhotoImage(file=r"C:\sample2.png")
# Label(splash_s, image=bg_img).place(x=0, y=0)


def Submit():
    gend=r.get()
    val1=name_entry.get()
    val2=email_entry.get()
    if val2.find("@")>=1 and val2.find(".com")>=1:
        print(val2)
        email_r=Label(reg,text="  valid email",fg="green").place(x=170, y=119)
        e=1
    else:
        print("invalid email")
        inv_email_r=Label(reg,text="Invalid email",fg="red").place(x=170, y=119)
        e=0
    val3=pas_entry.get()
    a=len(val3)
    if a>=8:
        print(val3)
        password_r=Label(reg,text="  valid password",fg="green").place(x=170, y=159)
        p=1
    else:
        print("invalid password")
        p=0
        inv_password_r=Label(reg,text="Invalid password",fg="red").place(x=170, y=159)
    val4=num_entry.get()
    if len(val4)==11:
        print(val4)
        number_r=Label(reg,text="  valid number",fg="green").place(x=170, y=199)
        n=1
    else:
        print("invalid number")    
        n=0
        inv_number_r=Label(reg,text="Invalid number",fg="red").place(x=170, y=199)
    if e==1 and p==1 and n==1:
        sql = "INSERT INTO abcdata (name, email, password, number,gender,date,photo) VALUES (%s, %s,%s,%s,%s,%s,%s)"
        val = [(str(val1),(str(val2)),(str(val3)),(str(val4)),(str(gend)),(str(date)),encodestring)]
        mycursor.executemany(sql, val)
        mydb.commit()
        #mydb.close()
        reg.withdraw()
    
def Info():
    c=c1-1
    info=Toplevel(root)
    info.geometry("500x400")
    info_color="white"
    info.configure(bg=info_color)
    info.title("user information")
    info_msg=Label(info, text="ABC INSTITUTE",bg=info_color, font="none 25 bold").place(x=150, y=10)
    info_msg=Label(info, text="USER INFORMATION", bg=info_color,font="none 17 bold").place(x=150, y=50)
    name=Label(info, text="name : ", bg=info_color,font="none 12 bold").place(x=90, y=100)
    name_r=Label(info, text=name_result[c], bg=info_color,font="none 12 bold").place(x=170, y=100)
    email=Label(info, text="email : ",bg=info_color, font="none 12 bold").place(x=90, y=130)
    email_r=Label(info, text=email_result[c],bg=info_color,font="none 12 bold").place(x=170, y=130)
    password=Label(info, text="password : ",bg=info_color,font="none 12 bold").place(x=75, y=160)
    password_r=Label(info, text=password_result[c],bg=info_color,font="none 12 bold").place(x=170, y=160)
    number=Label(info, text="number : ",bg=info_color,font="none 12 bold").place(x=80, y=190)
    number_r=Label(info, text=number_result[c],bg=info_color,font="none 12 bold").place(x=170, y=190)
    gender=Label(info, text="gender : ",bg=info_color,font="none 12 bold").place(x=80, y=220)
    gender_r=Label(info, text=gender_result[c],bg=info_color,font="none 12 bold").place(x=170, y=220)
    Date=Label(info, text="registered on : ",bg=info_color,font="none 12 bold").place(x=60, y=250)
    Date_r=Label(info, text=date_result[c],bg=info_color,font="none 12 bold").place(x=170, y=250)
    # data1=base64.b64decode(image_r[12][0])
    # file_like=io.BytesIO(data1)
    # print(file_like)
    # Charphoto = ImageTk.PhotoImage(Image.open(file_like))
    # ChLabel = Label(info, image=Charphoto).place(x=0,y=0)
def Pdf():
    c=c1-1
    mypdf= FPDF()
    mypdf.add_page()
    mypdf.set_font("Arial",size = 20)
    mypdf.cell(100,10,txt="FOOD SHOP ", ln=1, align="C")
    mypdf.cell(100,10,txt=f"Date : {d1}, {d2} {d3} {d4}", ln=2, align="C")
    mypdf.cell(100,10,txt=f"Time: {string}", ln=3, align="C")
    # s_n=list(name_result)
    # s_name=s_n[c]
    # print(s_name)
    # s_name1=s_name.replace("(","")
    # s_name1=s_name1.replace(")","")
    # s_name1=s_name1.replace(",","")
    # s_name1=s_name1.replace("'","")
    mypdf.cell(100,10,txt=f"Seller Name: {name_result[c]} ", ln=4, align="C")
    mypdf.cell(100,10,txt=f"Buyer Name: {buyer_name_entry.get()}", ln=5, align="C")
    mypdf.cell(100,10,txt=f"Selected item: {clicked.get()}", ln=6, align="C")
    mypdf.cell(100,10,txt=f"Item Price: {item_pr} PKR", ln=7, align="C")
    mypdf.cell(100,10,txt=f"Quantity: {quantity_entry.get()}"  , ln=8, align="C")
    mypdf.cell(100,10,txt=f"Total Price: {total_pr} PKR", ln=9, align="C")
    mypdf.cell(100,10,txt=f"Entered Amount: {amount_entry.get()} PKR", ln=10, align="C")
    mypdf.cell(100,10,txt=f"Returned Amount: {bn2-total_pr} PKR", ln=11, align="C")
    #mypdf.cell(100,100,txt="", ln=12, align="C")
    mypdf.output("mypdf.pdf")
def generate_rec():
    c=c1-1
    global item_pr
    if clicked.get()=="zinger burger 200 PKR":
        print("200")
        item_pr=200
    elif clicked.get()=="biryani 140 PKR":
        print("140")
        item_pr=140
    elif clicked.get()=="Pizza 1000 PKR":
        print("1000")
        item_pr=1000
    elif clicked.get()=="club sandwich 130 PKR":
        print("130")
        item_pr=130
    elif clicked.get()=="Chicken tikka 190 PKR":
        print("190")
        item_pr=190
    #print(type(item_pr))
    shop_name=Label(item, text= "FOOD SHOP",bg=item_color ,fg=item_fg , font="none 20 bold")
    shop_name.place(x=430, y=130)
    Date(item,410,160,"black")
    time_g=Label(item, text=f"Time {string}",bg=item_color ,fg=item_fg).place(x=410, y=180)
    underline=Label(item,text="_____________________________",bg=item_color,fg=item_fg).place(x=505 ,y=205)
    seller_name=Label(item, text="Seller Name",bg=item_color,fg=item_fg).place(x=410, y=200)
    
    seller_name1=Label(item, text=name_result[c], bg=item_color,fg=item_fg).place(x=510 ,y=200)
    
    buyer_name=Label(item, text="Buyer Name",bg=item_color,fg=item_fg).place(x=410, y=250)
    
    #buyer_name1=Label(item, text=buyer_name_entry.get() ).place(x=600 ,y=250)
    underline=Label(item,text="_____________________________",bg=item_color,fg=item_fg).place(x=505 ,y=255)
    
    selected_item=Label(item, text="Selected Item",bg=item_color,fg=item_fg).place(x=410,y=300)
    
    underline=Label(item,text="_____________________________",bg=item_color,fg=item_fg).place(x=505 ,y=305)
    selected_item1=Label(item, text=clicked.get(),bg=item_color,fg=item_fg).place(x=510,y=300)
    
    item_price=Label(item, text="item Price", bg=item_color,fg=item_fg).place(x=410,y=350)
    underline=Label(item,text="_____________________________",bg=item_color,fg=item_fg).place(x=505 ,y=355)
    item_price1=Label(item, text=item_pr,bg=item_color,fg=item_fg).place(x=510,y=350)
    #amount_entered=Label(item, text=amount_entry.get()).place(x=600,y=350)
    
    quantity_g=Label(item, text="Quantity",bg=item_color,fg=item_fg).place(x=410,y=400)
    underline=Label(item,text="_____________________________",bg=item_color,fg=item_fg).place(x=505 ,y=405)
    #quantity_g1=Label(item, text=quantity_entry.get()).place(x=600,y=400)
    bn1=buyer_name_entry.get()
    buyer_name1=Label(item, text=bn1 ,bg=item_color,fg=item_fg).place(x=510 ,y=250)
    
    
    bn3=quantity_entry.get()
    bn4=int(bn3)
    global total_pr
    total_pr=bn4*item_pr
    quantity_g1=Label(item, text=quantity_entry.get() ,bg=item_color,fg=item_fg)
    quantity_g1.place(x=510,y=400)
    
    total_price=Label(item, text="Total Price",bg=item_color,fg=item_fg).place(x=410,y=450)
    underline=Label(item,text="_____________________________",bg=item_color,fg=item_fg).place(x=505 ,y=455)
    total_price1=Label(item, text=f"{total_pr} PKR" ,bg=item_color,fg=item_fg).place(x=510,y=450)
    
    amount_entered=Label(item, text="Amount Entered", bg=item_color,fg=item_fg).place(x=405,y=500)
    underline=Label(item,text="_____________________________",bg=item_color,fg=item_fg).place(x=505 ,y=505)
    amount_entered=Label(item, text=f"{amount_entry.get()} PKR" ,bg=item_color,fg=item_fg).place(x=510,y=500)
    global bn2
    bn2=int(amount_entry.get())
    amount_returned=Label(item, text="Amount Returned", bg=item_color,fg=item_fg).place(x=405,y=550)
    underline=Label(item,text="_____________________________",bg=item_color,fg=item_fg).place(x=505 ,y=555)
    amount_returned1=Label(item, text=f"{bn2-total_pr} PKR" , bg=item_color,fg=item_fg).place(x=510,y=550)
    
def Close():
    root.destroy()

def Logout():
    root.deiconify()
    item.withdraw()
def item_win():
    root.withdraw()
    c=c1-1
    global item
    global item_color
    global buyer_name_entry
    global clicked
    global amount_entry
    global quantity_entry
    global item_fg
    item_color="gray4"
    item_fg="white"
    item=Toplevel(root)
    item.geometry("700x600+400+100")
    item.overrideredirect(True)
    item.configure(bg=item_color)
    Date(item,150,50,"black")
    def time(): 
        global lbl
        global string
        string = strftime('%H:%M:%S %p') 
        lbl = Label(item, text = "" ,font = ('calibri', 10, 'bold'), 
                    background = 'black', 
                    foreground = 'white')
        lbl.place(x=400,y=50)
        lbl.configure(text=f"Time: {string}")
        lbl.after(1000, time) 
    time()
    # img=PhotoImage(file=r"C:\Users\ehtisham siddiqui\Downloads\New folder (2)\burger-outline-filled.png")
    # img1=Label(item, image=img).place(x=0,y=0)
    close_btn=Button(item,text="X" , bg="red",fg=item_fg, width=4 , command=Close).place(x=665,y=0)
    seller_name_top=Label(item, text=name_result[c],bg=item_color ,fg=item_fg).place(x=600,y=25)
    logout_btn=Button(item,text="Logout",bg="light yellow", command= Logout).place(x=610,y=50)
    shop_name=Label(item, text= "FOOD SHOP",bg=item_color ,fg=item_fg , font="none 20 bold").place(x=250, y=9)
    select_item=Label(item, text="select item",bg=item_color,fg=item_fg).place(x=10,y=120)
    options=["zinger burger 200 PKR","biryani 140 PKR","Pizza 1000 PKR","club sandwich 130 PKR","Chicken Tikka 190 PKR"]
    clicked=StringVar()
    clicked.set(options[0])
    drop=OptionMenu(item,clicked,*options).place(x=110,y=120)
    
    # if clicked.get()=="zinger burger":
    #     print("200")
    # elif clicked.get()=="biryani":
    #     print("140")
    # elif clicked.get()=="Pizza":
    #     print("1000")
    # elif clicked.get()=="club sandwich":
    #     print("130")
    # elif clicked.get()=="Chicken tikka":
    #     print("190")
    
    quantity=Label(item, text="Enter Quantity",bg=item_color,fg=item_fg).place(x=10,y=160)
    quantity_entry=Entry(item,width=26)
    quantity_entry.place(x=110, y=160)
    Enter_amount=Label(item, text="Enter Amount",bg=item_color,fg=item_fg).place(x=10, y=200)
    amount_entry=Entry(item,width=26)
    amount_entry.place(x=110, y=200)
    Enter_name=Label(item, text="Enter Name",bg=item_color,fg=item_fg).place(x=10, y=240)
    
    buyer_name_entry=Entry(item,width=26)
    buyer_name_entry.place(x=110, y=240)
    
   
    gen_btn=Button(item, text="Generate receipt",bg="light yellow" ,command= lambda: generate_rec()).place(x=130,y=350)
    save_btn=Button(item, text="Save",bg="light yellow", command=lambda: Pdf()).place(x=280,y=350)
    
def Login(color):
    global name_result
    global email_result
    global password_result
    global number_result
    global gender_result
    global date_result
    global c1
    global inv_email
    global image_r
    global Charphoto
    val2=email_entry.get()
    val3=pas_entry.get()
    mycursor.execute("SELECT name FROM abcdata")
    name_result = mycursor.fetchall()
    
    mycursor2.execute("SELECT email FROM abcdata") 
    email_result = mycursor2.fetchall()
    
    mycursor3.execute("SELECT password FROM abcdata") 
    password_result = mycursor3.fetchall()
    
    mycursor4.execute("SELECT number FROM abcdata") 
    number_result = mycursor4.fetchall()
    
    mycursor5.execute("SELECT gender FROM abcdata") 
    gender_result = mycursor5.fetchall()
    
    mycursor6.execute("SELECT date FROM abcdata") 
    date_result = mycursor6.fetchall()
    
    mycursor7.execute("SELECT photo FROM abcdata")
    image_r = mycursor7.fetchall()
    # # data1=base64.b64decode(data[0][0])
    # # file_like=io.BytesIO(data1)
    # # img=PIL.Image.open(file_like)

    
    # sql1="select photo from abcdata"
    # mycursor7.execute(sql1)
    # data = mycursor7.fetchall()
    # data1=base64.b64decode(data[12][0])
    # file_like=io.BytesIO(data1)
    # img=PIL.Image.open(file_like)
    # Charphoto = ImageTk.PhotoImage(Image.open(file_like))
    c1=0
    c2=0
    L_emailresult=len(email_result)
    L_passwordresult=len(password_result)
    for x in email_result:
        c1=c1+1
        if x==(val2,):
            v_email=Label(root,text="  valid email",bg=color,fg="green").place(x=170, y=109)
            correct_e=Label(root,text="✓",bg=color,fg="green", font="none 10 bold").place(x=400, y=90)
            for y in password_result:
                c2=c2+1
                
                if y==(val3,) and c1==c2:
                    #print(email_result[c1])
                    v_password=Label(root,text="  valid password",bg=color,fg="green").place(x=170,y=149)
                    correct_p=Label(root,text="✓",bg=color,fg="green", font="none 10 bold").place(x=400, y=130)
                    
                    #Info()
                    item_win()
                    
                    break
                elif c2==L_passwordresult:
                    inv_password=Label(root,text="Invalid password",bg=color,fg="red").place(x=170,y=149)
                    wrong_p=Label(root,text="X",bg=color,fg="red", font="none 10 bold").place(x=400, y=130)
            
            break
        elif c1==L_emailresult:
            inv_email=Label(root,text="Invalid email",bg=color,fg="red").place(x=170, y=109)
            wrong_e=Label(root,text="X",bg=color,fg="red", font="none 10 bold").place(x=400, y=90)
def Image():
    global encodestring
    myfile=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes=(("png files","*.png"),("all files","*.*")) )
    with open(myfile, 'rb') as f:
        photo = f.read()
    encodestring = base64.b64encode(photo)
    

    # sql = "INSERT INTO regform (photo,name) VALUES (%s, %s)"
    # val = [(encodestring, "ehtishamulhaq")]
    # mycursor.executemany(sql, val)
    # db.commit()
    # db.close()

def Date(w,x1,y1,color):  
    global date
    global d1
    global d2
    global d3
    global d4
    
    X= datetime.datetime.now()
    date=X.strftime("%c")
    d1=X.strftime("%A")
    d2=X.strftime("%d")
    d3=X.strftime("%B")
    d4=X.strftime("%Y")
    date_show=Label(w, text= f"Date : {d1}, {d2} {d3} {d4}",bg=color, fg="blue").place(x=x1,y=y1)
        #date.after(200,Date)
def register():
    global name_entry
    global email_entry
    global pas_entry
    global num_entry
    global r
    global reg
    
    reg=Toplevel(root)
    reg.title("Registration form")
    reg.geometry("450x400")
    
    reg_heading=Label(reg, text="REGISTRATION FORM",font="none 17 bold").place(x=140, y=10)
    name = Label(reg, text="Enter name")
    name.place(x=20, y=60)
    name_entry = Entry(reg,width=45)
    name_entry.place(x=100, y=60)
    
    email = Label(reg, text="Enter email")
    email.place(x=20, y=100)
    email_entry = Entry(reg,width=45)
    email_entry.place(x=100, y=100)
    
    password = Label(reg, text="Enter password")
    password.place(x=20, y=140)
    pas_entry = Entry(reg,width=45)
    pas_entry.place(x=100, y=140)
    
    number = Label(reg, text="number")
    number.place(x=20, y=180)
    num_entry = Entry(reg,width=45)
    num_entry.place(x=100, y=180)
    
    r=StringVar()
    r.set("male")
    Date(reg,0,380,"white")
    Radiobutton(reg ,text="male",variable=r,value="male").place(x=120, y=240)
    Radiobutton(reg ,text="female",variable=r,value="female").place(x=220, y=240)
    img_btn=Button(reg, text="select image", command=Image).place(x=190,y=300)
    submit_btn=Button(reg,text="Submit",command=lambda: Submit()).place(x=200, y=340)
    
    
    #root.destroy()
    #f"Time: {string}"

def mainwindow():
    splash_s.destroy()
    global root
    
    root = Tk()
    root_color="light green"
    root.geometry("450x400+400+250")
    root.title("FOOD SHOP")
    root.overrideredirect(True)
    root.configure(bg=root_color)
      
    root_msg=Label(root, text="FOOD SHOP",bg=root_color, font="none 20 bold").place(x=130,y=20)
    root_msg2=Label(root, text="Sign in",bg=root_color, font="none 12 bold").place(x=130,y=60)
    
    # img1path=Image.open(r"C:\sample.png")
    # rimg1=img1path.resize((200,200))
    # myIMG1=ImageTk.PhotoImage(rimg1)
    # sss=Label(root, image=myIMG1).place(x=0,y=0)
    email = Label(root, text="Enter email",bg=root_color)
    email.place(x=30,y=90)
    global email_entry
    email_entry = Entry(root, width=45)
    email_entry.place(x=120,y=90)

    password = Label(root, text="Enter password",bg=root_color)
    password.place(x=20,y=130)
    global pas_entry
    pas_entry = Entry(root,width=45)
    pas_entry.place(x=120,y=130)
    login_btn=Button(root,text="Login",bg="light yellow", command=lambda: Login(root_color)).place(x=130,y=200)
    register_btn = Button(root, text="Register",bg="light yellow" ,command=lambda:register()).place(x=270,y=200)
    Date(root,1,375,root_color)
    #time()
    clos=Button(root, text="X", bg="red" ,fg="white" ,width=4, command=Close ).place(x=415,y=0)

splash_s.after(4000,mainwindow)

mainloop()
