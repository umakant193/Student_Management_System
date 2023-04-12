
def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H :%M :%S")
        addeddate = time.strftime("%d/%m/%y")
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications',
                                            'Id {} Name {} Added successfully ... and want to clean the form'.format(id,
                                                                                                                     name),
                                            parent=addroot)
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id', parent=addroot)
        strr = 'select *from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studentTable.insert('', END, values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x490+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='#8BD8BD')
    addroot.resizable(False, False)

    # ---------------------------------------------   Add Student lables

    idlabel = Label(addroot, text='Enter Id :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Enter Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    # -------------------------------------------------- Add Student Entry

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    identry = Entry(addroot, font=('roman', 15, 'bold'), textvariable=idval, bd=5)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), textvariable=nameval, bd=5)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), textvariable=mobileval, bd=5)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), textvariable=emailval, bd=5)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), textvariable=addressval, bd=5)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), textvariable=genderval, bd=5)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), textvariable=dobval, bd=5)
    dobentry.place(x=250, y=370)
    #### ------------------------------ Add Button

    submitbtn = Button(addroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, bg='#243665',
                       activebackground='white', activeforeground='black', command=submitadd)
    submitbtn.place(x=150, y=430)
    addroot.mainloop()


def searchstudent():
    def submitsearch():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()

        addeddate = time.strftime("%d/%m/%y")

        if (id != ''):
            strr = 'select *from studentdata where id=%s'
            mycursor.execute(strr, (id))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentTable.insert('', END, values=vv)
        elif (name != ''):
            strr = 'select *from studentdata where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentTable.insert('', END, values=vv)
        elif (mobile != ''):
            strr = 'select *from studentdata where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentTable.insert('', END, values=vv)
        elif (email != ''):
            strr = 'select *from studentdata where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentTable.insert('', END, values=vv)
        elif (address != ''):
            strr = 'select *from studentdata where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentTable.insert('', END, values=vv)
        elif (gender != ''):
            strr = 'select *from studentdata where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentTable.insert('', END, values=vv)
        elif (dob != ''):
            strr = 'select *from studentdata where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentTable.insert('', END, values=vv)

        elif (addeddate != ''):
            strr = 'select *from studentdata where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentTable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x550+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='#8BD8BD')
    searchroot.resizable(False, False)

    # ---------------------------------------------   Add Student lables

    idlabel = Label(searchroot, text='Search Id :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Search Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Search Mobile :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Search Email :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Search Address :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Search Gender:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Search D.O.B :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Search Date :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)
    # -------------------------------------------------- Add Student Entry

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    identry = Entry(searchroot, font=('roman', 15, 'bold'), textvariable=idval, bd=5)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), textvariable=nameval, bd=5)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), textvariable=mobileval, bd=5)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), textvariable=emailval, bd=5)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), textvariable=addressval, bd=5)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), textvariable=genderval, bd=5)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), textvariable=dobval, bd=5)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), textvariable=dateval, bd=5)
    dateentry.place(x=250, y=430)
    #### ------------------------------ Add Button

    submitbtn = Button(searchroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, bg='#243665',
                       activebackground='white', activeforeground='black', command=submitsearch)
    submitbtn.place(x=150, y=490)
    searchroot.mainloop()


def deletestudent():
    cc = studentTable.focus()
    content = studentTable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr, (pp))
    con.commit()
    messagebox.showinfo('Notifications', 'Id  {} deleted successfully'.format(pp))
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studentTable.insert('', END, values=vv)


def updatestudent():
    def submitupdate():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr, (name, mobile, email, address, gender, dob, date, time, id))
        con.commit()
        messagebox.showinfo('Notification', 'Id {} Modified successfully...'.format(id))
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studentTable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x610+220+200')
    updateroot.title('Student Management System')
    updateroot.config(bg='#8BD8BD')
    updateroot.resizable(False, False)

    # ---------------------------------------------   Add Student lables

    idlabel = Label(updateroot, text='Update Id :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Update Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Update Mobile :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Update Email :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Update Address :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Update Gender:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Update D.O.B :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Update Date :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)
    timelabel = Label(updateroot, text='Update Time :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=490)

    
    # -------------------------------------------------- Add Student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    identry = Entry(updateroot, font=('roman', 15, 'bold'), textvariable=idval, bd=5)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), textvariable=nameval, bd=5)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), textvariable=mobileval, bd=5)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), textvariable=emailval, bd=5)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), textvariable=addressval, bd=5)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), textvariable=genderval, bd=5)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), textvariable=dobval, bd=5)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), textvariable=dateval, bd=5)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), textvariable=timeval, bd=5)
    timeentry.place(x=250, y=490)

    #### ------------------------------ Add Button
    submitbtn = Button(updateroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, bg='#243665',
                       activebackground='white', activeforeground='black', command=submitupdate)
    submitbtn.place(x=150, y=550)

    cc = studentTable.focus()
    content = studentTable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    updateroot.mainloop()


def showstudent():
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studentTable.insert('', END, values=vv)


def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studentTable.get_children()
    id, name, mobile, email, address, gender, dob, addeddate, addedtime = [], [], [], [], [], [], [], [], []
    for i in gg:
        content = studentTable.item(i)
        pp = content['values']
        id.append(pp[0]), name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(
            pp[4]), gender.append(pp[5]), dob.append(pp[6]), addeddate.append(pp[7]), addedtime.append(pp[8])
    dd = ['Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time']
    df = pandas.DataFrame(list(zip(id, name, mobile, email, address, gender, dob, addeddate, addedtime)), columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notification', 'Student data is Saved {}'.format(paths))


def exitstudent():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit ?')
    if (res == True):
        root.destroy()



# Connect to Database
def Connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification', 'Data is incorrect please enter again')
            return
        try:
            strr = 'create database studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int,name varchar(100),mobile varchar(20),email varchar(100),address varchar(100),gender varchar(20),dob varchar(20),date varchar(20),time varchar(20))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database created and Now you are connected to the database ...',
                                parent=dbroot)
        except:
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database ...', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.geometry('470x250+800+230')
    dbroot.grab_set()
    dbroot.resizable(False, False)
    dbroot.config(bg='skyblue')
    # -----------------------------Connectdb Labels
    hostlabel = Label(dbroot, text="Enter Host :", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=13, anchor='w')
    hostlabel.place(x=10, y=10)
    userlabel = Label(dbroot, text="Enter User :", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=13, anchor='w')
    userlabel.place(x=10, y=70)
    passwordlabel = Label(dbroot, text="Enter Password :", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=13, anchor='w')
    passwordlabel.place(x=10, y=130)


    # ------------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostEntry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    hostEntry.place(x=250, y=10)

    userEntry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userEntry.place(x=250, y=70)

    passwordEntry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordEntry.place(x=250, y=130)


    # -----------------------------Connectdb Button
    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='white',bd=5,width=20,activebackground='blue',activeforeground='white',command=submitdb)
    submitbutton.place(x=150, y=190)
    dbroot.mainloop()


def Tick():
    time_string = time.strftime("%H: %M: %S")
    date_string = time.strftime("%d /%m /%y")
    clock.config(text='Date :' + date_string + '\n' + 'Time : ' + time_string)
    clock.after(200, Tick)


import random

colors = ['black']


def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(20, IntroLabelColorTick)


def IntroLabelTick():
    global count, text
    if (count >= len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, IntroLabelTick)


# importing
from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time

root = Tk()
root.title('Student Management System')
root.config(bg='skyblue')
root.geometry('1174x700+200+50')
root.resizable(False, False)



# Frames

##-----------------------------------------------------------Dataenter frame Intro
DataEntryFrame = Frame(root,bg='skyblue',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel = Label(DataEntryFrame,text='>>>>>>>>>>>>> Welcome <<<<<<<<<<<<<',width=30,font=('arial',22,'italic bold'),bg='skyblue')
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('times',20,'bold'),bd=5,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('times',20,'bold'),bd=5,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('times',20,'bold'),bd=5,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('times',20,'bold'),bd=5,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('times',20,'bold'),bd=5,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export Data',width=25,font=('times',20,'bold'),bd=5,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7. Exit',width=25,font=('times',20,'bold'),bd=5,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)


##-----------------------------------------------------------ShowData frame Intro
ShowDataFrame = Frame(root,bg='black',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=540, y=80, height=600, width=620)



# -------------------------------------Show Data Frame
style = ttk.Style()
style.configure('Treeview.Heading',font=('times',17,'bold'),foreground='black')
style.configure('Treeview',font=('arial',15,'bold'),foreground='black',background='black')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
studentTable = Treeview(ShowDataFrame, columns=(
'Id', 'Name', 'Mobile no', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studentTable.xview)
scroll_y.config(command=studentTable.yview)
studentTable.heading('Id', text='Id')
studentTable.heading('Name', text='Name')
studentTable.heading('Mobile no', text='Mobile no')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')
studentTable['show'] = 'headings'
studentTable.column('Id', width=100)
studentTable.column('Name', width=200)
studentTable.column('Mobile no', width=200)
studentTable.column('Email', width=300)
studentTable.column('Address', width=200)
studentTable.column('Gender', width=100)
studentTable.column('D.O.B', width=150)
studentTable.column('Added Date', width=150)
studentTable.column('Added Time', width=150)

studentTable.pack(fill=BOTH, expand=1)



# Slider
ss = 'Welcome To Student Management System'
count = 0
text = ''
SliderLabel = Label(root,text=ss,font=('robot',30,'bold'),relief=RIDGE,borderwidth=4,width=32,bg='cyan')
SliderLabel.place(x=180,y=0)
IntroLabelTick()
IntroLabelColorTick()



# Time
clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=10, y=0)
Tick()



# Connecting Database
connectbutton = Button(root,text='Connect to Database',width=15,font=('times',15,'bold'),relief=RIDGE,borderwidth=4,bg='green2',
                activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=962, y=0)
root.mainloop()