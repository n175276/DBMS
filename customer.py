from tkinter import *
from PIL import Image,  ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Art Gallery")
        self.root.geometry("1355x520+140+275")

        self.var_ref = StringVar()
        x = random.randint(10000,99999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_addr = StringVar()
        self.var_Pid = StringVar()
        self.var_mono = StringVar()
        self.var_cost = StringVar()

        lbl_title = Label(self.root, text="Add  Customer Details", font=("times new roman", 18,"bold"),bg= "black", fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1355, height=50)

        lebelframeleft = LabelFrame(self.root, bd =2, relief=RIDGE,text="Customer Datails",padx=2, font=("times new roman", 12,"bold"))
        lebelframeleft.place(x=5, y=50,width = 425, height=460)

        lbl_cust_ref = Label(lebelframeleft, text="Customer ID", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0, sticky=W)
        enty_ref = ttk.Entry(lebelframeleft,width=29,textvariable=self.var_ref, font=("times new roman", 13,"bold"), state="readonly")
        enty_ref.grid(row=1,column=1)

        lbl_cust_name = Label(lebelframeleft, text="Customer Name", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=2,column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeleft,width=29,textvariable=self.var_name, font=("times new roman", 13,"bold"))
        enty_name.grid(row=2,column=1)

        lbl_cust_addr = Label(lebelframeleft, text="Address", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_addr.grid(row=3,column=0, sticky=W)
        enty_addr = ttk.Entry(lebelframeleft,width=29,textvariable=self.var_addr, font=("times new roman", 13,"bold"))
        enty_addr.grid(row=3,column=1)

        lbl_cust_painting = Label(lebelframeleft, text="Painting ID", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_painting.grid(row=4,column=0, sticky=W)
        enty_painting = ttk.Entry(lebelframeleft,width=29,textvariable=self.var_Pid, font=("times new roman", 13,"bold"))
        enty_painting.grid(row=4,column=1)

        lbl_cust_mo_no = Label(lebelframeleft, text="Mobile No", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_mo_no.grid(row=5,column=0, sticky=W)
        enty_mo_no = ttk.Entry(lebelframeleft,width=29,textvariable=self.var_mono, font=("times new roman", 13,"bold"))
        enty_mo_no.grid(row=5,column=1)

        lbl_cust_cost = Label(lebelframeleft, text="Cost", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_cost.grid(row=6,column=0, sticky=W)
        enty_cost = ttk.Entry(lebelframeleft,width=29,textvariable=self.var_cost, font=("times new roman", 13,"bold"))
        enty_cost.grid(row=6,column=1)

        btn_frame = Frame(lebelframeleft,bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=412,height=40)

        btnAdd = Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman", 13,"bold"), bg ="black",fg="gold", width=9,padx=1)
        btnAdd.grid(row=0,column=0)
        
        btnUpdate = Button(btn_frame,text="UPDATE",command=self.update,font=("times new roman", 13,"bold"), bg ="black",fg="gold", width=9,padx=1)
        btnUpdate.grid(row=0,column=1)

        btnDelete = Button(btn_frame,text="DELETE",command=self.ddelete,font=("times new roman", 13,"bold"), bg ="black",fg="gold", width=9,padx=1)
        btnDelete.grid(row=0,column=2)
        
        btnReset = Button(btn_frame,text="RESET",command=self.reset,font=("times new roman", 13,"bold"), bg ="black",fg="gold", width=9,padx=1)
        btnReset.grid(row=0,column=3)

        TABLEFRAME = LabelFrame(self.root, bd =2, relief=RIDGE,text="View Details and Search Syatem",padx=2, font=("times new roman", 12,"bold"))
        TABLEFRAME.place(x=435, y=50,width = 910, height=460)

        lblsearchby = Label(TABLEFRAME, text="Search By", font=("times new roman", 12,"bold"), bg= "red", fg="white")
        lblsearchby.grid(row=0,column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(TABLEFRAME,textvariable=self.search_var, font=("times new roman", 12,"bold"), width=24, state="readonly" )        
        combo_search["value"] = ("cust_id","Mobile")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(TABLEFRAME,textvariable=self.txt_search,width=24, font=("times new roman", 13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch = Button(TABLEFRAME,text="SEARCH",command=self.search,font=("times new roman", 11,"bold"), bg ="black",fg="gold", width=9,padx=1)
        btnSearch.grid(row=0,column=3,padx=2)
        
        btnShowAll = Button(TABLEFRAME,text="SHOW ALL",command=self.Fetch_data,font=("times new roman", 11,"bold"), bg ="black",fg="gold", width=9,padx=1)
        btnShowAll.grid(row=0,column=4,padx=2)

        Deatail_Table =Frame(TABLEFRAME,bd=2, relief=RIDGE)
        Deatail_Table.place(x=0, y=50,width = 890, height=370)

        scroll_x = ttk.Scrollbar(Deatail_Table, orient=HORIZONTAL)     
        scroll_y = ttk.Scrollbar(Deatail_Table, orient=VERTICAL)  

        self.cust_datails_Table = ttk.Treeview(Deatail_Table, columns=("ID","Name","addr","P_id","mobileno","cost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_datails_Table.xview)
        scroll_y.config(command=self.cust_datails_Table.yview)

        self.cust_datails_Table.heading("ID", text= "customer ID")
        self.cust_datails_Table.heading("Name", text= "customer Name")
        self.cust_datails_Table.heading("addr", text= "Address")
        self.cust_datails_Table.heading("P_id", text= "Painting ID")
        self.cust_datails_Table.heading("mobileno", text= "Mobile No")
        self.cust_datails_Table.heading("cost", text= "Cost")
        
        self.cust_datails_Table["show"]="headings"
        self.cust_datails_Table.pack(fill=BOTH, expand=1)
        self.cust_datails_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.Fetch_data()


    def add_data(self):
        if self.var_mono.get()=="" or self.var_Pid.get() == "":
            messagebox.showerror("Error","All Fields are Required !!",parent=self.root)
        else:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Nut175276#",
                    database="art_gallary")
                my_cursor = mydb.cursor()
                my_cursor.execute("INSERT into customer values(%s,%s,%s,%s,%s,%s)",(
                                                                        self.var_ref.get(),
                                                                        self.var_name.get(),
                                                                        self.var_addr.get(),
                                                                        self.var_Pid.get(),
                                                                        self.var_mono.get(),
                                                                        self.var_cost.get()
                                                                    ))
                mydb.commit()
                self.Fetch_data()
                mydb.close()
                messagebox.showinfo("Success","customer has been Added", parent=self.root)
            except EXCEPTION as es:
                messagebox.showwarning("Warning",f" Something Went Wrong !!!! : {str(es)}",parent=self.root)

    def Fetch_data(self):
        mydb = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Nut175276#",
                    database="art_gallary")
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * From customer")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_datails_Table.delete(*self.cust_datails_Table.get_children())
            for i in rows:
                self.cust_datails_Table.insert("",END,values=i)
            mydb.commit()
        mydb.close()

    def get_cursor(self,event=""):
        cursor_row = self.cust_datails_Table.focus()
        content = self.cust_datails_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_addr.set(row[2]),
        self.var_Pid.set(row[3]),
        self.var_mono.set(row[4]),
        self.var_cost.set(row[5])

    def update(self):
        if self.var_mono.get()=="":
            messagebox.showerror("Error", " Please Enter Valid Mobile No !!!", parent = self.root)
        else:
            mydb = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Nut175276#",
                    database="art_gallary")
            my_cursor = mydb.cursor()
            my_cursor.execute("UPDATE customer set cust_name=%s,cust_addr=%s,painting_id=%s,mobile=%s,cost=%s where cust_id =%s",(
                                                                                            self.var_name.get(),
                                                                                            self.var_addr.get(),
                                                                                            self.var_Pid.get(),
                                                                                            self.var_mono.get(),
                                                                                            self.var_cost.get(),
                                                                                            self.var_ref.get()  ))     
                             
            mydb.commit()  
            self.Fetch_data()                                                                                                
            mydb.close()
            messagebox.showinfo("Update","Customer Details has Been Updated Succesfully !",parent = self.root)

    def ddelete(self):
        ddelete= messagebox.askyesno("Art Gallery System","Do you want to delete this Customer", parent = self.root)
        if ddelete > 0:
            mydb = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Nut175276#",
                    database="art_gallary")
            my_cursor = mydb.cursor()
            query = "delete from customer where cust_id=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not ddelete:
                return
        mydb.commit()
        self.Fetch_data()
        mydb.close()
    
    def reset(self):
        # self.var_ref.set(""),
        self.var_name.set(""),
        self.var_addr.set(""),
        self.var_Pid.set(""),
        self.var_mono.set(""),
        self.var_cost.set("")

        x = random.randint(10000,99999)
        self.var_ref.set(str(x))
    
    def search(self):
        mydb = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Nut175276#",
                    database="art_gallary")
        my_cursor = mydb.cursor()
        # query = "select * from customer where "+ str(self.search_var.get())+ " LIKE '%"+str(self.txt_search.get())+"%'"
        # value = (self.var_ref.get(),)
        my_cursor.execute("select * from customer where "+ str(self.search_var.get())+ " LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_datails_Table.delete(*self.cust_datails_Table.get_children())
            for i in rows:
                self.cust_datails_Table.insert("",END, values=i)
            mydb.commit()
        mydb.close()



if __name__ == "__main__":
    root = Tk()
    obj = Cust_window(root)
    root.mainloop()