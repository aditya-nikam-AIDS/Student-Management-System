
from tkinter import * 
#import all the packages for gui
import mysql.connector as mysql
import tkinter.messagebox  as MessageBox
conc=mysql.connect(host="localhost",user="root",passwd="aditya",database="mini_project")
def Insert():
        r=e_roll_no.get()
        phone=e_mob_no.get()
        name=e_name.get()
        c=e_class.get()
        age=e_age.get()
        if(r ==""):
            MessageBox.showinfo('insert status','all filled required fill it')
        else:
            roll_no=int(r,10)
            #conc=mysql.connect(host="localhost",user="root",passwd="aditya",database="mini_project")
            cursor=conc.cursor()
            query="Insert into student values({},'{}',{},'{}','{}')".format(roll_no,name,age,phone,c)
            cursor.execute(query)
            conc.commit()
            MessageBox.showinfo('insert status','inserted successfully')
            e_roll_no.delete('0','end')
            e_mob_no.delete('0','end')
            e_age.delete('0','end')
            e_name.delete('0','end')
            e_class.delete('0','end')
            print("insert successfully")

def Update():
        r=e_roll_no.get()
        phone=e_mob_no.get()
        name=e_name.get()
        c=e_class.get()
        age=e_age.get()
        if(r ==""):
            MessageBox.showinfo('update status','all filled required fill it')
        else:
           #r_n=int(r,10)
            #conc=mysql.connect(host="localhost",user="root",passwd="aditya",database="mini_project")
            cursor=conc.cursor()
          #  query="update student set name='"+name+"' where roll_no='"+r+"'"
            query="update student set name=%s, age=%s , mob_no=%s, c_lass=%s where roll_no=%s"
            input=(name,age,phone,c,r)

            cursor.execute(query,input)
            conc.commit()
            MessageBox.showinfo('Update status','Updated successfully')
            e_roll_no.delete('0','end')
            e_mob_no.delete('0','end')
            e_age.delete('0','end')
            e_name.delete('0','end')
            e_class.delete('0','end')
            print("insert successfully")
        



def Delete():
     if(e_roll_no.get() == ""):
         MessageBox.showinfo('Delete status','enter the student roll no which has to be deleted')
     else:
            r=e_roll_no.get()
            roll_no=int(r,10)
            #conc=mysql.connect(host="localhost",user="root",passwd="aditya",database="mini_project")
            cursor=conc.cursor()
            query="delete from student where roll_no={}".format(roll_no)
            cursor.execute(query)
            conc.commit()
            MessageBox.showinfo(' delete status','deleted successfully')
            e_roll_no.delete('0','end')
            e_mob_no.delete('0','end')
            e_age.delete('0','end')
            e_name.delete('0','end')
            e_class.delete('0','end')
            print("deleted successfully")



    
def show():
        if(e_roll_no.get() == ""):
         MessageBox.showinfo('search  status','enter the student roll no which has to be searched')
        else:
            r=e_roll_no.get()
            roll_no=int(r,10)
            #conc=mysql.connect(host="localhost",user="root",passwd="aditya",database="mini_project")
            cursor=conc.cursor()
            query="select * from student where roll_no={}".format(roll_no)
            cursor.execute(query)
            rows=cursor.fetchall()
            for row in rows:
                 # e_roll_no.insert(0,row[0])
                  e_mob_no.insert(0,row[3])
                  e_age.insert(0,row[2])
                  e_name.insert(0,row[1])
                  e_class.insert(0,row[4])
            MessageBox.showinfo('search  status','seached has been successful')
            
            print("search successfully")





window=Tk()
#tk() function create a window container for application
window.geometry("600x300")
window.title("STUDENT MANAGEMENT SYSTEM")
ROLL_NO=Label(window,text='ROLL_NO', font=('bold',10))
ROLL_NO.place(x=20,y=30)
e_roll_no=Entry()
e_roll_no.place(x=150,y=30)
Name=Label(window,text='Name', font=('bold',10))
Name.place(x=20,y=60)
e_name=Entry()
e_name.place(x=150,y=60)
AGE=Label(window,text='AGE', font=('bold',10))
AGE.place(x=20,y=90)
e_age=Entry()
e_age.place(x=150,y=90)
MOBILE_NO=Label(window,text='MOBILE_NO', font=('bold',10))
MOBILE_NO.place(x=20,y=120)
e_mob_no=Entry()
e_mob_no.place(x=150,y=120)
CLASS=Label(window,text='CLASS', font=('bold',10))
CLASS.place(x=20,y=150)
e_class=Entry()
e_class.place(x=150,y=150)
insert=Button(window,text='INSERT',font=("bold",10),bg='yellow',command=Insert)
insert.place(x=20,y=180)
delete=Button(window,text='DELETE',font=("bold",10),bg='yellow',command=Delete)
delete.place(x=90,y=180)
update=Button(window,text='Update_Record',font=("bold",10),bg='yellow',command=Update)
update.place(x=160,y=180)
get=Button(window,text='SHOW',font=("bold",10),bg='yellow',command=show)
get.place(x=280,y=180)


window.mainloop()

