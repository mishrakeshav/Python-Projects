from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

#Main window
root = Tk()
root.title("E. M. S")
root.geometry("500x400+200+200")

#to open the addEmp window
def f1():
    addEmp.deiconify()
    root.withdraw()

#to open the viewEmp window()
def f3():
    viewEmp.deiconify()
    root.withdraw()
    import cx_Oracle
    con = None
    cursor = None

    try:
        con = cx_Oracle.connect('system/abc123')
        print("Connected")
        cursor = con.cursor()
        sql = "SELECT * FROM employees"
        cursor.execute(sql)
        data = cursor.fetchall()
        mdata = ""
        st.delete('1.0', END)
        for d in data:
            mdata = mdata + str(d[0]) + " " + d[1] + "\n"
        st.insert(INSERT, mdata)
        con.commit()
        print(cursor.rowcount, " record inserted")
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        print("Issue: ", e)
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()
            print("Disconnected")

btnAdd = Button(root, text = "Add", width = 20, command = f1)
btnView = Button(root, text = "View", width = 20, command = f3)

btnAdd.pack(pady = 10)
btnView.pack(pady = 10)

#Add window

addEmp = Toplevel(root)
addEmp.title("Add E")
addEmp.geometry("500x400+200+200")
addEmp.withdraw()

lblEid = Label(addEmp, text= "Enter eid")
entEid = Entry(addEmp, bd = 5)

lblEname = Label(addEmp, text = "Enter ename")
entEname = Entry(addEmp, bd = 5)

def f5():
    import cx_Oracle
    con = None
    cursor = None

    try:
        con = cx_Oracle.connect('system/abc123')
        print("Connected")
        cursor = con.cursor()
        sql = "INSERT INTO employees VALUES('%d', '%s')"
        eid = int(entEid.get())
        ename = entEname.get()
        args = (eid, ename)
        cursor.execute(sql % args)
        con.commit()
        msg = str(cursor.rowcount) + " record inserted"
        messagebox.showinfo("Success ", msg)
    except cx_Oracle.DatabaseError as e:
        con.rollback()
    
        messagebox.showerror("Failure: ", e)
    except ValueError as v:
        con.rollback()
        messagebox.showerror("Failure: ", v)
    finally:
        if cursor is not None:
            cursor.close()
    if con is not None:
        con.close()
        print("Disconnected")

btnAddSave = Button(addEmp, text = "Save", command = f5)

#to go back to the main window
def f2():
    entEid.delete(0, END)
    entEname.delete(0, END)
    root.deiconify()
    addEmp.withdraw()

btnAddBack = Button(addEmp, text = "Back", command = f2)

lblEid.pack(pady = 10)
entEid.pack(pady = 10)

lblEname.pack(pady = 10)
entEname.pack(pady = 10)

btnAddSave.pack(pady = 10)
btnAddBack.pack(pady = 10)

#View Window
viewEmp = Toplevel(root)
viewEmp.title("View E")
viewEmp.geometry("500x400+200+200")
viewEmp.withdraw()

#to go back to the main window
def f4():
    st.delete(1.0, END)
    root.deiconify()
    viewEmp.withdraw()
st = scrolledtext.ScrolledText(viewEmp, width = 30, height = 5)

btnViewBack = Button(viewEmp, text = "Back", command = f4)

st.pack(pady = 10)
btnViewBack.pack(pady = 10)


root.mainloop()
