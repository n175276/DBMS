from tkinter import *
from PIL import Image,  ImageTk
from customer import Cust_window
from artist import Artist_win
from Exhibition import Exhi_window

class ArtGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Art Gallery")
        self.root.geometry("1500x800+0+0")

        img1 = Image.open("img1.jpg")
        img1 = img1.resize((1500,170), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img1)

        lbling = Label(self.root,image = self.photoimg, bd =5, relief=RIDGE)
        lbling.place(x=0, y=0,width=1500, height=170)

        lbl_title = Label(self.root, text="Art Gallery", font=("times new roman", 40,"bold"),bg= "black", fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=170, width=1500, height=70)

        main_frame =Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0,y=240,width=1500,height=560)

        lbl_menu = Label(main_frame, text="Menu", font=("times new roman", 20,"bold"),bg= "black", fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=130)

        btn_frame =Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0,y=35,width=128,height=150)

        cust_btn = Button(btn_frame,text="Customer",command=self.cust_deatails,width=11,font=("times new roman", 14,"bold"),bg= "black", fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        cust_btn.grid(row=0, column=0, pady =1)

        arts_btn= Button(btn_frame,text="Artist",command=self.artist_deatails,width=11,font=("times new roman", 14,"bold"),bg= "black", fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        arts_btn.grid(row=1, column=0, pady =1)

        admin_btn= Button(btn_frame,text="Exhibition",command=self.Exhibition_deatails,width=11,font=("times new roman", 14,"bold"),bg= "black", fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        admin_btn.grid(row=2, column=0, pady =1)

        exit_btn= Button(btn_frame,text="EXIT",command=self.root.destroy,width=11,font=("times new roman", 14,"bold"),bg= "black", fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        exit_btn.grid(row=3, column=0, pady =1)

        img2 = Image.open("img1.jpg")
        img2 = img2.resize((770,550), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img2)

        lbling = Label(main_frame,image = self.photoimg1, bd =5, relief=RIDGE)
        lbling.place(x=130, y=0,width=770, height=550)
    
    def cust_deatails(self):
        self.new_window = Toplevel(self.root)
        self.app=Cust_window( self.new_window)

    def artist_deatails(self):
        self.new_window = Toplevel(self.root)
        self.app=Artist_win( self.new_window)
    
    def Exhibition_deatails(self):
        self.new_window = Toplevel(self.root)
        self.app=Exhi_window( self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = ArtGallery(root)
    root.mainloop()