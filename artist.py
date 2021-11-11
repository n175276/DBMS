from tkinter import *
from PIL import Image,  ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Artist_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Art Gallery")
        self.root.geometry("1355x520+140+275")

        self.var_ref = StringVar()
        x = random.randint(10000,99999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_addr = StringVar()
        self.var_mono = StringVar()
        self.var_gid = StringVar()

        lbl_title = Label(self.root, text="Add Artist Details", font=("times new roman", 18,"bold"),bg= "black", fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1355, height=50)

        lebelframeleft = LabelFrame(self.root, bd =2, relief=RIDGE,text="Artist Datails",padx=2, font=("times new roman", 12,"bold"))
        lebelframeleft.place(x=5, y=50,width = 425, height=460)

        lbl_cust_ref = Label(lebelframeleft, text="Artist ID", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0, sticky=W)
        enty_ref = ttk.Entry(lebelframeleft,width=18,textvariable=self.var_ref, font=("times new roman", 13,"bold"))
        enty_ref.grid(row=1,column=1, sticky=W)

        btndata = Button(lebelframeleft,text="Data",command=self.fetch_Painting,font=("times new roman", 10,"bold"), bg ="black",fg="gold", width=9,padx=1)
        btndata.place(x=300,y=4)
        

        lbl_artist_name = Label(lebelframeleft, text="Name", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_artist_name.grid(row=2,column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeleft,width=29,textvariable=self.var_name, font=("times new roman", 13,"bold"))
        enty_name.grid(row=2,column=1)

        lbl_artist_addr = Label(lebelframeleft, text="Address", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_artist_addr.grid(row=3,column=0, sticky=W)
        enty_addr = ttk.Entry(lebelframeleft,width=29,textvariable=self.var_addr, font=("times new roman", 13,"bold"))
        enty_addr.grid(row=3,column=1)

        lbl_artist_mono = Label(lebelframeleft, text="Mobile no", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_artist_mono.grid(row=4,column=0, sticky=W)
        enty_mono = ttk.Entry(lebelframeleft,width=29,textvariable=self.var_mono, font=("times new roman", 13,"bold"))
        enty_mono.grid(row=4,column=1)

        lbl_artist_gid = Label(lebelframeleft, text="Gallery Id", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_artist_gid.grid(row=5,column=0, sticky=W)
        enty_gid = ttk.Entry(lebelframeleft,width=29,textvariable=self.var_gid, font=("times new roman", 13,"bold"))
        enty_gid.grid(row=5,column=1)

        btnPdata = Button(lebelframeleft,text="Gallery Details",command=self.fetch_Gallery,font=("times new roman", 10,"bold"), bg ="black",fg="gold", width=15,padx=1)
        btnPdata.place(x=0,y=200)

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
        TABLEFRAME.place(x=435, y=260,width = 910, height=245)

        lblsearchby = Label(TABLEFRAME, text="Search By", font=("times new roman", 12,"bold"), bg= "red", fg="white")
        lblsearchby.grid(row=0,column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(TABLEFRAME,textvariable=self.search_var, font=("times new roman", 12,"bold"), width=24, state="readonly" )        
        combo_search["value"] = ("ArtistId","name")
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
        Deatail_Table.place(x=0, y=50,width = 890, height=180)

        scroll_x = ttk.Scrollbar(Deatail_Table, orient=HORIZONTAL)     
        scroll_y = ttk.Scrollbar(Deatail_Table, orient=VERTICAL)  

        self.cust_datails_Table = ttk.Treeview(Deatail_Table, columns=("ID","Name","addr","mobileno","gid"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_datails_Table.xview)
        scroll_y.config(command=self.cust_datails_Table.yview)

        self.cust_datails_Table.heading("ID", text= "Artist ID")
        self.cust_datails_Table.heading("Name", text= "Artist Name")
        self.cust_datails_Table.heading("addr", text= "Address")
        self.cust_datails_Table.heading("mobileno", text= "Mobile No")
        self.cust_datails_Table.heading("gid", text= "Gallery Id")
        
        self.cust_datails_Table["show"]="headings"
        self.cust_datails_Table.pack(fill=BOTH, expand=1)
        self.cust_datails_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.Fetch_data()

    def fetch_Painting(self):
        if self.var_ref.get() =="":
            messagebox.showerror("Error","Please Enter ID", parent=(self.root))
        else:
            mydb = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Nut175276#",
                    database="art_gallary")
            my_cursor = mydb.cursor()
            query= ("SELECT * from Painting where a_id=%s")
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
            rows = my_cursor.fetchone()
            if rows == None:
                messagebox.showerror("Error","Artist Data nat Found !!",parent = self.root)
            else:
                mydb.commit()
                mydb.close()

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE,padx=2)
                showDataFrame.place(x=455,y=55,width=250, height=180)

                lblName = Label(showDataFrame,text="Painting ID: ", font=("arial",12,"bold"))
                lblName.place(x=0, y=0)
                lblName1 = Label(showDataFrame,text=rows[0], font=("arial",12,"bold"))
                lblName1.place(x=90, y=0)

                lblName = Label(showDataFrame,text="Painting Title: ", font=("arial",12,"bold"))
                lblName.place(x=0, y=50)
                lblName1 = Label(showDataFrame,text=rows[1], font=("arial",12,"bold"))
                lblName1.place(x=120, y=50)

                lblName = Label(showDataFrame,text="Year: ", font=("arial",12,"bold"))
                lblName.place(x=0, y=100)
                lblName1 = Label(showDataFrame,text=rows[2], font=("arial",12,"bold"))
                lblName1.place(x=90, y=100)


    def fetch_Gallery(self):
        if self.var_gid.get() =="":
            messagebox.showerror("Error","Please Enter Gallery ID", parent=(self.root))
        else:
            mydb = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Nut175276#",
                    database="art_gallary")
            my_cursor = mydb.cursor()
            query= ("SELECT * from gallery where ID=%s")
            value = (self.var_gid.get(),)
            my_cursor.execute(query,value)
            rows = my_cursor.fetchone()
            if rows == None:
                messagebox.showerror("Error","Artist Data nat Found !!",parent = self.root)
            else:
                mydb.commit()
                mydb.close()

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE,padx=2)
                showDataFrame.place(x=725,y=55,width=300, height=180)

                lblName = Label(showDataFrame,text="Gallery ID: ", font=("arial",12,"bold"))
                lblName.place(x=0, y=0)
                lblName1 = Label(showDataFrame,text=rows[0], font=("arial",12,"bold"))
                lblName1.place(x=90, y=0)

                lblName = Label(showDataFrame,text="Name: ", font=("arial",12,"bold"))
                lblName.place(x=0, y=50)
                lblName1 = Label(showDataFrame,text=rows[1], font=("arial",12,"bold"))
                lblName1.place(x=70, y=50)

                lblName = Label(showDataFrame,text="Location: ", font=("arial",12,"bold"))
                lblName.place(x=0, y=100)
                lblName1 = Label(showDataFrame,text=rows[2], font=("arial",12,"bold"))
                lblName1.place(x=90, y=100)              
    
    def add_data(self):
        if self.var_mono.get()=="" or self.var_name.get() == "":
            messagebox.showerror("Error","All Fields are Required !!",parent=self.root)
        else:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Nut175276#",
                    database="art_gallary")
                my_cursor = mydb.cursor()
                my_cursor.execute("INSERT into artist values(%s,%s,%s,%s,%s)",(
                                                                        self.var_ref.get(),
                                                                        self.var_name.get(),
                                                                        self.var_addr.get(),
                                                                        self.var_mono.get(),
                                                                        self.var_gid.get()
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
        my_cursor.execute("SELECT * From artist")
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
        self.var_mono.set(row[3]),
        self.var_gid.set(row[4])
    
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
            my_cursor.execute("UPDATE artist set name=%s,address=%s,mobile=%s,G_id=%s where ArtistId =%s",(
                                                                                            self.var_name.get(),
                                                                                            self.var_addr.get(),
                                                                                            self.var_mono.get(),
                                                                                            self.var_gid.get(),
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
            query = "delete from artist where artistid=%s"
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
        self.var_mono.set(""),
        self.var_gid.set("")

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
        my_cursor.execute("select * from artist where "+ str(self.search_var.get())+ " LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_datails_Table.delete(*self.cust_datails_Table.get_children())
            for i in rows:
                self.cust_datails_Table.insert("",END, values=i)
            mydb.commit()
        mydb.close()




if __name__ == "__main__":
    root = Tk()
    obj = Artist_win(root)
    root.mainloop()