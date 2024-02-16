from tkinter import *
from PIL import Image, ImageTk 
from tkinter import messagebox
import database,forget_password




class main:
    def __init__(self):

        self.root=Tk()
        self.root.geometry('1300x690')
        self.root.title("Main Window")
        self.root.config(bg='#071828')

        # set the wallpaper image
        self.signin_wallpaper=Image.open('pics\login_wallapaper.jpg').resize((1269,690))    
        self.signin_wallpaperTK=ImageTk.PhotoImage(self.signin_wallpaper)
        self.signin_wallpaper=Label(self.root,image=self.signin_wallpaperTK)
        self.signin_wallpaper.place(x=0,y=0)

        # making a frame for sign in 
        self.login_frame=Frame(self.root, height=609, width= 510, border= 10 ,bg="#FFFFFF")
        self.login_frame.place(x=650,y=17)

        # now write text on frame
        self.sign_in=Label(self.login_frame, text="Sign in", font=("Arail",25,"bold"),fg="#000000",bg="#FFFFFF")
        self.sign_in.place(x=30,y=18)

        self.exisisting_user=Label(self.login_frame, text="exisisting user?", font=("Arail",12),fg="#000000",bg="#FFFFFF")
        self.exisisting_user.place(x=30,y=70)

        self.create_new_user=Label(self.login_frame, text="Create an account.", font=("Arail",12),fg="#071828",bg="#FFFFFF",)
        self.create_new_user.place(x=130,y=70)


        self.email_label=Label(self.login_frame, text="Email address", font=("Arail",8),fg="#000000",bg="#FFFFFF")
        self.email_label.place(x=30,y=130)

        self.email_entry=Entry(self.login_frame, font=("arail") ,fg="#000000",width=40,border=4, borderwidth=2)
        self.email_entry.place(x=30,y=150)

        self.password_label=Label(self.login_frame, text="Password", font=("Arail",8),fg="#000000",bg="#FFFFFF")
        self.password_label.place(x=30,y=180)

        self.password_entry=Entry(self.login_frame, font=("arail") ,fg="#000000",width=40,border=4, borderwidth=2,show="*")
        self.password_entry.place(x=30,y=200)

        # making button to continue
        self.continue_button=Button(self.login_frame,text="Continue" ,font=("arail",14) ,fg="#000000",bg='#8390B0',command=self.sign_in_continue)
        self.continue_button.place(x=385,y=240)

        self.breakpoint=Label(self.login_frame, text="______________________________OR______________________________", font=("Arail",10),fg="#000000",bg="#FFFFFF")
        self.breakpoint.place(x=30,y=290)

        # making button for other sign in option like Google,Facebook

        self.signin_wallpaper1=Image.open('pics\ifoto-ai_1707238877732.png').resize((50,50))    
        self.signin_wallpaperTK1=ImageTk.PhotoImage(self.signin_wallpaper1)
        self.signin_wallpaper1=Label(self.login_frame,image=self.signin_wallpaperTK1,bg="#FFFFFF")
        self.signin_wallpaper1.place(x=120,y=326)

        self.GOOGLE_BUTTON=Button(self.login_frame,text="Sign in with Google" ,font=("arail",14) ,fg="#000000",bg='#FFFFFF')
        self.GOOGLE_BUTTON.place(x=200,y=330)

        self.FACEBOOK_LOGO=Image.open('pics\ifoto-ai_1707239150285.png').resize((60,50))    
        self.FACEBOOK_LOGOTK1=ImageTk.PhotoImage(self.FACEBOOK_LOGO)
        self.FACEBOOK_LOGO=Label(self.login_frame,image=self.FACEBOOK_LOGOTK1,bg="#FFFFFF")
        self.FACEBOOK_LOGO.place(x=120,y=400)

        self.FACEBOOK_BUTTON=Button(self.login_frame,text="Sign in with facebook" ,font=("arail",14) ,fg="#000000",bg='#FFFFFF')
        self.FACEBOOK_BUTTON.place(x=200,y=400)
       
       
        self.root.mainloop()
        

    def sign_in_continue(self):
        # condition
        if self.email_entry.get() and self.password_entry.get():
            res=database.sign_in((self.email_entry.get(), self.password_entry.get()))
            if res:
                messagebox.showinfo('Success','You are successful Sign in..') 
            elif self.email_entry.get()=="" or self.password_entry.get()=="":
                messagebox.showwarning('Warning','Fill your Credentials..') 
        else:
            messagebox.showerror('Error', 'The username or Password is incorrect.. ')
        
           
        

if __name__=="__main__":
    main()