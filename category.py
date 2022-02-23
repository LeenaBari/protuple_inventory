from cgitb import text
from textwrap import fill
from tkinter import*
from turtle import title
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

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
        btn_add=Button(self.root,text="ADD",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)

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
        # self.category_table bind("<ButtonRelease-1>",self.get_data)











if __name__=="__main__":
 root=Tk()
 obj=categoryClass(root)
 root.mainloop()
