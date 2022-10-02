from cProfile import label
from tkinter import *
from PIL import Image,ImageTk
from  tkinter import ttk

class employeeClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Սկաուտական")
        self.root.config(bg="white")
        self.root.focus_force()

        #all variables
        self.var_searchbye=StringVar()
        self.var_searchtxt=StringVar()

        
        
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()




        #search
        SearchFrame=LabelFrame(self.root,text="Սկաուտների որոնում",bg="white",font=("goudy old style",12,"bold"))
        SearchFrame.place(x=250,y=20,width=600,height=70)

        cbm_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchbye,values=("ընտրել","էլեկտրոնային հասցե","Անուն","համար"),state='readonly',justify=CENTER,font=("goudy old style",10))
        cbm_search.place(x=10,y=10,width=180)
        cbm_search.current(0)


        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",10),bg="lightyellow").place(x=220,y=10)
        btn_search=Button(SearchFrame,text="որոնում",font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=400,y=5,width=150,height=30)

        #title
        title=Label(self.root,text="սկաուտների մանրամասները",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)


        #Content
        lbl_empid=Label(self.root,text="ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Հատված",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="համար",font=("goudy old style",15),bg="white").place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
        cbm_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("ընտրել","Արի","Արենուշ","Կրտսեր","Գերագույն"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cbm_gender.place(x=500,y=150,width=180)
        cbm_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)

        
















if __name__=="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
