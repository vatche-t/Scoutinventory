from cProfile import label
from tkinter import *
from PIL import Image,ImageTk
from employee import employeeClass


class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Սկաուտական")
        self.root.config(bg="white")

        #Title
        self.icon_title=PhotoImage(file="images/ararat.png")
        title=Label(self.root,text="Սկաուտական Միութիւն",image=self.icon_title,compound=LEFT,font=("times new romen",30,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,heigh=70)

        #btnLogout
        btn_logout=Button(self.root,text="Դուրս գալ",font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
        #clock
        self.lbl_clock=Label(self.root,text="բարի գալուստ սկաուտական ​​համակարգ\t\t թւական։ DD-MM-YYYY\t\t Ժամ։ HH",font=("times new romen",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,heigh=30)

        #menue
        self.MenuLogo=Image.open("images/ararat.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        lbl_menu=Label(LeftMenu,text="մենյու",font=("times new roman",18),bg="#009688").pack(side=TOP,fill=X)
        
        btn_employee=Button(LeftMenu,text="Սկաուտներ",command=self.employee,font=("times new roman",18,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
        btn_suppliers=Button(LeftMenu,text="կազմ",font=("times new roman",18,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
        btn_catagory=Button(LeftMenu,text="կատեգորիա",font=("times new roman",18,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Պահեստ",font=("times new roman",18,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Նիւթական",font=("times new roman",18,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Ելք",font=("times new roman",18,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)

            
        #content
        self.lbl_employee=Label(self.root,text="ընդհանուր սկաուտներ\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",15,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        
        self.lbl_supplier=Label(self.root,text="ընդհանուր կազմ\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",15,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_catagory=Label(self.root,text="ընդհանուր կատեգորիա\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",15,"bold"))
        self.lbl_catagory.place(x=1000,y=120,height=150,width=300)
        
        self.lbl_product=Label(self.root,text="ընդհանուր Պահեստ\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",15,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text="ընդհանուր Նիւթական\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",15,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        #footer
        lbl_footer=Label(self.root,text="IMS-Scout | Developed By Vatche Thorossian\n ցանկացած տեխնիկական խնդրի համար դիմեք: 09129332760",font=("times new romen",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
#===============================



    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()

