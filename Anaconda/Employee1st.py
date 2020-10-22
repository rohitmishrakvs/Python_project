import time
import datetime
from tkinter import *
from tkinter import messagebox



def login():
    UserName=e1.get()
    password=e2.get()
    
    if UserName=="" or password=="":
        messagebox.showerror("login error","please enter username and password")
    else:
        import pymysql
        db=pymysql.connect("localhost","root","","employee")  #previous db is hry;
        print(db)
        cursor=db.cursor()
        sql="select UserName,password from Emp_details"
        cursor.execute(sql)
        data=cursor.fetchall()
        if data!=0:
            for row in range(len(data)):
                if UserName==data[row][0] and password==data[row][1]:
                    messagebox.showinfo("success","you are sucessfully logged in")
                    import Employee

                    break
                else:
                    messagebox.showwarning("Failed","please enter valid username or password or register yourself ") 
        db.close()
        
        
def register():
         
        import Employee2nd
        #frame.Employee2nd
           

root=Tk()
'''canvas=Canvas(width=1500,height=883,bg='black' )
canvas.pack()

photo=PhotoImage(file='C:\\Users\\hp\\Desktop\\normal\\image\\ok.png')
canvas.create_image(0,0, image=photo, anchor=NW)'''


root.title("Login page")
root.geometry('1350x650+0+0')
root.configure(background="lavender")
 
 
Tops=Frame(root,width=1350,height=50,bd=8,bg="lavender")
Tops.pack(side=TOP)

 
 
lblinfo=Label(Tops,font=('arial',45,'bold'),text="Employee Payment Management system ",bd=10,bg="lavender",fg="purple")
lblinfo.grid(row=0,column=0)

#lb=Label(Tops,font=('arial',14),text="Login Page",bd=10,bg="lavender",fg="purple")
#lb.grid(row=1,column=0)




frame=Frame(root,width=200,height=70,bg='lavender')
 
lb=Label(frame,font=('arial',14,'bold'),text="Login Page",bd=10,bg="lavender",fg="black",underline="0")
lb.grid(row=0,column=0)
l1=Label(frame,text="UserName",font=('arial',16),bd=13,fg="black",bg="lavender")
l1.grid(row=1,column=0,sticky=W)
e1=Entry(frame,width=40)
e1.grid(row=1,column=1)



l2=Label(frame,text="password",font=('arial',16),bd=13,fg="black",bg="lavender")
l2.grid(row=2,column=0,sticky=W)
e2=Entry(frame,show="*",width=40)
e2.grid(row=2,column=1)






b1=Button(frame,text='SignIn',bd=3,font=('arial',12,'bold'),width=8,fg="black",bg="silver",command=login)
#b1=Button(frame,text="submit",command=login,bg='green')
b1.grid(row=3,column=0)


#b2=Button(flb,text='SignUp',padx=16,pady=16,bd=5,font=('arial',16,'bold'),width=14,command=register,fg="black",bg="silver")

b2=Button(frame,text='SignUp',bd=3,font=('arial',12,'bold'),width=8,fg="black",bg="silver",command=register)
#b2=Button(frame,text="register",command=register,bg='red')
b2.grid(row=3,column=1)
frame.place(x=468,y=200)

#frame.pack()
root.mainloop()
