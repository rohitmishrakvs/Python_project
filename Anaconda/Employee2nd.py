
from tkinter import messagebox
#import tkFont

############################## Inserting into database######################### 
def register():
    Emp_id = e1.get()
    UserName=e2.get()
    password=e3.get()
    confermPassword=e4.get()
    sex=str(var.get()) 
    name=e5.get()
    phon_No=e6.get()
    Address=e7.get()
    import pymysql
    db=pymysql.connect("localhost","root","","employee")
 
    cursor=db.cursor()
    sql="INSERT INTO emp_details(Emp_id,UserName,password,confermPassword,name,phon_No,Address,sex)values('{}','{}','{}','{}','{}','{}','{}','{}')".format(Emp_id,UserName,password,confermPassword,name,phon_No,Address,sex)
    if Emp_id=="" or UserName=="" or password=="" or confermPassword=="" or name=="" or sex=="" or phon_No=="" or Address=="":
        messagebox.showerror("failed","please filled all required fields")
    if password!=confermPassword:
        messagebox.showerror("failed","password and confermPassword didnt matched")
    
    
    
    
    else:
        try:
            cursor.execute(sql)
            db.commit()
            messagebox.showinfo("success","sucessfully inserted")
        except:
            db.rollback()
            messagebox.showerror("error", "something went wrong")
            
    

def log():
    import Employee1st
    
####################################### Main program start here #####################

'''
canvas=Canvas(width=1500,height=883)
canvas.pack()
photo=PhotoImage(file='C:\\Users\\hp\\Desktop\\normal\\u.png')
canvas.create_image(0,0, image=photo, anchor=NW)'''
root=Tk()
root.title("Employee payroll system")
root.geometry('1350x650+0+0')
root.configure(background="lavender")

Tops=Frame(root,width=1350,height=50,bd=8,bg="lavender")
Tops.pack(side=TOP)

f1=Frame(root,width=600,height=600,bd=8,bg="lavender")
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,bd=8,bg="lavender")
f2.pack(side=RIGHT)

fla=Frame(f1,width=600,height=200,bd=8,bg="lavender")
fla.pack(side=TOP)
flb=Frame(f1,width=300,height=600,bd=8,bg="lavender")
flb.pack(side=TOP)

lb =Label(Tops,font=('arial',35,'bold'),text="Registration Page",bd=10,fg="purple",bg="lavender")
lb.grid(row=0,column=0)

frame=Frame(root,width=200,height=70,bg='lavender')
var=IntVar()


'''root.title("registeration form")
root.geometry("2000x800" )

var=IntVar()
frame=Frame(root)'''
#helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
l=Label(frame,text="Registration form",font=('arial',15 ),bd=20,fg="purple",bg="lavender",anchor="w")
l.grid(row=0,columnspan=3)

l1=Label(frame,text="Emp_id",font=('arial',15),bd=10,fg="black",bg="lavender",anchor=W)
l1.grid(row=1,column=0,sticky=W)
e1=Entry(frame,width=40)
e1.grid(row=1,column=2)

l2=Label(frame,text="UserName",font=('arial',15 ),bd=10,fg="black",bg="lavender",anchor=W)
l2.grid(row=2,column=0,sticky=W)
e2=Entry(frame,width=40)
e2.grid(row=2,column=2)


l3=Label(frame,text="password",font=('arial',15),bd=10,fg="black",bg="lavender",anchor=W)
l3.grid(row=3,column=0,sticky=W)
e3=Entry(frame,show="*",width=40)
e3.grid(row=3,column=2)


l4=Label(frame,text="confermPassword", font=('arial',15 ),bd=10,fg="black",bg="lavender",anchor=W)
#l4=Label(frame,text="confermPassword",bg='green')
l4.grid(row=4,column=0,sticky=W)
e4=Entry(frame,show="*",width=40)
e4.grid(row=4,column=2)


l5=Label(frame,text="name",font=('arial',15 ),bd=10,fg="black",bg="lavender")
#l5=Label(frame,text="name",bg='green')
l5.grid(row=5,column=0,sticky=W)
e5=Entry(frame,width=40)
e5.grid(row=5,column=2)


l6=Label(frame,text="gender",font=('arial',15),bd=10,fg="black",bg="lavender")
#l6=Label(frame,text="gender",bg='green')
l6.grid(row=6,column=0,sticky=W)


r1=Radiobutton(frame,text="male",font=('arial',10),variable=var,value="m",bg="lavender")
r1.grid(row=6,column=2,sticky=W)
r2=Radiobutton(frame,text="female",font=('arial',10),variable=var,value="f",bg="lavender")
r2.grid(row=6,column=3,sticky=W) 


l7=Label(frame,text="phon_No",font=('arial',15),bd=10,fg="black",bg="lavender")
#l7=Label(frame,text="phon_No",bg='green')
l7.grid(row=7,column=0,sticky=W)
e6=Entry(frame,width=40)
e6.grid(row=7,column=2)


l8=Label(frame,text="Address",font=('arial',15),bd=10,fg="black",bg="lavender",anchor="w")
#l8=Label(frame,text="Address",bg='green')
l8.grid(row=8,column=0,sticky=W)
e7=Entry(frame,width=40)
e7.grid(row=8,column=2)
 
#b1=Button(frame,text='SignIn',bd=3,font=('arial',12,'bold'),width=8,fg="black",bg="silver",command=login)
b1=Button(frame,text='register',bd=3,font=('arial',12,'bold'),width=15,fg="black",bg="silver",command=register)
b1.grid(row=10,column=0)
 
frame.place(x=420,y=100)
root.mainloop()