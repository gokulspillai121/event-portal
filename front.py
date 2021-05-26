import tkinter as tk                
from tkinter import font  as tkfont 
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector


mycursor=mydb.cursor()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Event portal")
        self.title_font = tkfont.Font(family='Goudy Old Style', size=18, weight="bold", slant="italic")
        self.geometry("600x400+500+250")
        self.iconbitmap(r'1.ico')

        
        container = tk.Frame(self,bg="white")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}
        for F in (StartPage, User_Login, Host_Login, USign_In,USign_Up, HSign_In, HSign_Up ):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller
        

        headlabel1=tk.Label(self,text="Event Management System",font=("arial",30,"bold"),bg="#3d3d5c").place(x=50,y=30)
       
        headlabel2=tk.Label(self,text="Log In To Portal",font=("arial",18,"bold"),bg="#3d3d5c").place(x=210,y=140)
        
        Userbtn=tk.Button(self,text="User",command=lambda: controller.show_frame("User_Login"),font=controller.title_font).place(x=190,y=200)
        
        
        Hostbtn=tk.Button(self,text="Host",command=lambda: controller.show_frame("Host_Login"),font=controller.title_font).place(x=350,y=200)
        
        

class User_Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller
        
        Userlabel1=tk.Label(self,text="User Login Portal",font=("arial",30,"bold"),bg="#3d3d5c").place(x=150,y=50)
       
        Userlabel2=tk.Label(self,text=" Existing User ",font=("arial",18,"bold"),bg="#3d3d5c").place(x=90,y=150)
        SignInbtn=tk.Button(self,text="Sign In",command=lambda: controller.show_frame("USign_In"),font=controller.title_font).place(x=120,y=200)
        
        Userlabel3=tk.Label(self,text="   New User   ",font=("arial",18,"bold"),bg="#3d3d5c").place(x=350,y=150)
        SignUpbtn=tk.Button(self,text="Sign Up",command=lambda: controller.show_frame("USign_Up"),font=controller.title_font).place(x=380,y=200)
        
        Backbtn=tk.Button(self,text="Back To Main Page",command=lambda: controller.show_frame("StartPage"),font=controller.title_font).place(x=200,y=300)

class Host_Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller
        
        
        Hostlabel1=tk.Label(self,text="Host Login Portal",font=("arial",30,"bold"),bg="#3d3d5c").place(x=150,y=50)
       
        Hostlabel2=tk.Label(self,text=" Existing Host ",font=("arial",18,"bold"),bg="#3d3d5c").place(x=90,y=150)
        SignInbtn=tk.Button(self,text="Sign In",command=lambda: controller.show_frame("HSign_In"),font=controller.title_font).place(x=120,y=200)
        
        Hostlabel3=tk.Label(self,text="    New Host    ",font=("arial",18,"bold"),bg="#3d3d5c").place(x=350,y=150)
        SignUpbtn=tk.Button(self,text="Sign Up",command=lambda: controller.show_frame("HSign_Up"),font=controller.title_font).place(x=380,y=200)
        
        Backbtn=tk.Button(self,text="Back To Main Page",command=lambda: controller.show_frame("StartPage"),font=controller.title_font).place(x=200,y=300)
        

class USign_Up(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller
        
        Slabel1=tk.Label(self,text="User Sign Up",font=controller.title_font,bg="#3d3d5c").place(x=250,y=50)
        name= tk.Label(self,text="Name",bg="#3d3d5c").place(x=210,y=110)
        gmail= tk.Label(self,text="Gmail",bg="#3d3d5c").place(x=210,y=150)
        password= tk.Label(self,text="Password",bg="#3d3d5c").place(x=210,y=190)
        
        Nmval=tk.StringVar()
        Gmval=tk.StringVar()
        Pasval=tk.StringVar()
        checkval=tk.IntVar()
        
        nameentry= tk.Entry(self, textvariable=Nmval).place(x=300,y=110)
        gmailentry= tk.Entry(self, textvariable=Gmval).place(x=300,y=150)
        passwordentry= tk.Entry(self, textvariable=Pasval).place(x=300,y=190)
        
        checkbtn= tk.Checkbutton(self,text="Not a Robot", variable = checkval,bg="#3d3d5c").place(x=250,y=230)
        
        def getvals():
            messagebox.showinfo("SignUp Successfull","Account Created Successfully")
            #Nmval=self.nameentry.get()
            #Gmval=self.gmailentry.get()
            #Pasval=self.passwordentry.get()
            #try:
                #sql="Insert into eventreg(Uname,Ugmail,Upass) values(%s,%s,%s)"
                #val=(Nmval,Gmval,Pasval)
                #mycursor.execute(sql,val)
                #mydb.commit()
                #messagebox.showinfo("information","recoed entered")
            #except Exception as e:
                #print(e)
            
            
        Signbtn=tk.Button(self,text="Create Account", command=getvals).place(x=250,y=270)
        Backbtn=tk.Button(self,text="Back To Main Page",command=lambda: controller.show_frame("StartPage")).place(x=180,y=350)
        Backbtn=tk.Button(self,text="Back To User Login",command=lambda: controller.show_frame("User_Login")).place(x=300,y=350)


    
class USign_In(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller
        
        Slabel1=tk.Label(self,text="User Sign In",font=controller.title_font,bg="#3d3d5c").place(x=250,y=50)
        gmail= tk.Label(self,text="Gmail",bg="#3d3d5c").place(x=210,y=110)
        password= tk.Label(self,text="Password",bg="#3d3d5c").place(x=210,y=150)
        
        Gmval=tk.StringVar()
        Pasval=tk.StringVar()
        checkval=tk.IntVar()
        
        gmailentry= tk.Entry(self, textvariable=Gmval).place(x=300,y=110)
        passwordentry= tk.Entry(self, textvariable=Pasval).place(x=300,y=150)
        
        checkbtn= tk.Checkbutton(self,text="Not a Robot", variable = checkval).place(x=250,y=190)
        def getvals():
            messagebox.showinfo("SignIn Successfull","Signed In Successfully")
        Signbtn=tk.Button(self,text="Sign In", command=getvals).place(x=250,y=230)
        Backbtn=tk.Button(self,text="Back To Main Page",command=lambda: controller.show_frame("StartPage")).place(x=240,y=350)
        


class HSign_In(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller
        
        Slabel1=tk.Label(self,text="Host Sign In",font=controller.title_font,bg="#3d3d5c").place(x=250,y=50)
        gmail= tk.Label(self,text="Gmail",bg="#3d3d5c").place(x=210,y=110)
        password= tk.Label(self,text="Password",bg="#3d3d5c").place(x=210,y=150)
        
        Gmval=tk.StringVar()
        Pasval=tk.StringVar()
        checkval=tk.IntVar()
    
        gmailentry= tk.Entry(self, textvariable=Gmval).place(x=300,y=110)
        passwordentry= tk.Entry(self, textvariable=Pasval).place(x=300,y=150)
        
        checkbtn= tk.Checkbutton(self,text="Not a Robot", variable = checkval).place(x=250,y=190)
        def getvals():
            messagebox.showinfo("SignIn Successfull","Signed In Successfully")
        Signbtn=tk.Button(self,text="Sign In", command=getvals).place(x=250,y=230)
        Backbtn=tk.Button(self,text="Back To Main Page",command=lambda: controller.show_frame("StartPage")).place(x=250,y=350)



class HSign_Up(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller
        
        Hlabel1=tk.Label(self,text="Host Sign Up",font=controller.title_font,bg="#3d3d5c").place(x=250,y=50)
        name= tk.Label(self,text="Host Name",bg="#3d3d5c").place(x=210,y=110)
        gmail= tk.Label(self,text="Host Mail",bg="#3d3d5c").place(x=210,y=150)
        password= tk.Label(self,text="Password",bg="#3d3d5c").place(x=210,y=190)
        
        Nmval=tk.StringVar()
        Gmval=tk.StringVar()
        Pasval=tk.StringVar()
        checkval=tk.IntVar()
        
        nameentry= tk.Entry(self, textvariable=Nmval).place(x=300,y=110)
        gmailentry= tk.Entry(self, textvariable=Gmval).place(x=300,y=150)
        passwordentry= tk.Entry(self, textvariable=Pasval).place(x=300,y=190)
        
        checkbtn= tk.Checkbutton(self,text="Not a Robot", variable = checkval,bg="#3d3d5c").place(x=250,y=230)
        def getvals():
            messagebox.showinfo("SignUp Successfull","Account Created Successfully")
        Signbtn=tk.Button(self,text="Create Account", command=getvals).place(x=250,y=270)
        Backbtn=tk.Button(self,text="Back To Main Page",command=lambda: controller.show_frame("StartPage")).place(x=180,y=350)
        Backbtn=tk.Button(self,text="Back To Host Login",command=lambda: controller.show_frame("Host_Login")).place(x=300,y=350)


class Ecreate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller
        
        
class Ereg(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
