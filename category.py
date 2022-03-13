import os.path
from cgitb import text
from textwrap import fill
from tkinter import*
from turtle import title
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
root_dir=os.path.dirname(__file__)

from pkg_resources import EntryPoint
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed By Leena")
        self.root.config(bg="white")
        self.root.focus_force()


        #========================Variable=====================
        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        #=======================title=========================
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=50,y=170,width=300)
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=100,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=470,y=170,width=100,height=30)
        btn_back= Button(self.root, text="Back", command=self.back, font=("goudy old style", 15), bg="black",fg="white", cursor="hand2").place(x=580, y=170, width=100, height=30)

        #=============category Details==============================
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        self.cateory_table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cateory_table.xview)
        scrolly.config(command=self.cateory_table.yview)

        self.cateory_table.heading("cid",text="C ID")
        self.cateory_table.heading("name",text="Name")
        self.cateory_table["show"]="headings"
        self.cateory_table.column("cid",width=90)
        self.cateory_table.column("name",width=100)
        self.cateory_table.pack(fill=BOTH,expand=1)
        self.cateory_table.bind("<ButtonRelease-1>",self.get_data)

        #=======================Images=====================
        self.im1=Image.open(os.path.join(root_dir,"Project Pic/cat2.jpg"))
        self.im1=self.im1.resize((500,250),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)
        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)

        self.im2=Image.open(os.path.join(root_dir,"Project Pic/cat3.jpg"))
        self.im2=self.im2.resize((500,250),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)
        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)

        
        self.show()

#=========================Functions===========================
    def add(self):
        con=sqlite3.connect(database=r'protuple_inventory.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category name must be required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                   messagebox.showerror("Error","Category already present try different",parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(
                        self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'protuple_inventory.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.cateory_table.delete(*self.cateory_table.get_children())
            for row in rows:
                self.cateory_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)



    def get_data(self,ev):
        f=self.cateory_table.focus()
        content=(self.cateory_table.item(f))
        row=content['values']
        
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])


        
    def delete(self):
        con=sqlite3.connect(database=r'protuple_inventory.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error"," Please select  category name",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error","Try again!!!",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def back(self):
        self.root.destroy()
        os.system("python dashboard.py")


if __name__=="__main__":
 root=Tk()
 obj=categoryClass(root)
 root.mainloop()
