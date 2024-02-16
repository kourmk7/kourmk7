from tkinter import *
from PIL import Image, ImageTk 
from tkinter import messagebox
import database



class main:
    def __init__(self):

        self.root=Tk()
        self.root.geometry('1300x690')
        self.root.title("Main Window")
        self.root.config(bg='#071828')

        # set the wallpaper image
        self.signin_wallpaper=Image.open('pics/login_wallapaper.jpg').resize((1269,690))    
        self.signin_wallpaperTK=ImageTk.PhotoImage(self.signin_wallpaper)
        self.signin_wallpaper=Label(self.root,image=self.signin_wallpaperTK)
        self.signin_wallpaper.place(x=0,y=0)

 # making a frame for sign in 
        self.login_frame=Frame(self.root, height=609, width= 510, border= 10 ,bg="#FFFFFF")
        self.login_frame.place(x=650,y=17)
        
        # now write text on frame
        self.reset_password=Label(self.login_frame, text="Reset Password", font=("Arail",25,"bold"),fg="#285982" ,bg="#FFFFFF")
        self.reset_password.place(x=30,y=18)
        
        self.forget_password=Label(self.login_frame, text="Forget Password", font=("Arail",12,"bold"),fg="#000000",bg="#FFFFFF")
        self.forget_password.place(x=30,y=70)
        
        self.email_label=Label(self.login_frame, text=" Existing Email", font=("Arail",16,"bold"),fg="#000000",bg="#FFFFFF")
        self.email_label.place(x=30,y=120)
        
        self.email_entry=Entry(self.login_frame, font=("arail") ,fg="#000000",width=40,border=4, borderwidth=2)
        self.email_entry.place(x=30,y=150)
        
        self.new_password_label=Label(self.login_frame, text=" New Password ", font=("Arail",16,"bold"),fg="#000000",bg="#FFFFFF")
        self.new_password_label.place(x=30,y=190)
        
        self.new_password_entry=Entry(self.login_frame, font=("arail") ,fg="#000000",width=40,border=4, borderwidth=2,show="*")
        self.new_password_entry.place(x=30,y=220)
        
        # self.reenter_password_label=Label(self.login_frame, text="Re-enter Password", font=("Arail",16,"bold"),fg="#000000",bg="#FFFFFF")
        # self.reenter_password_label.place(x=30,y=250)
        
        # self.reenter_password_entry=Entry(self.login_frame, font=("arail") ,fg="#000000",width=40,border=4, borderwidth=2,show="*")
        # self.reenter_password_entry.place(x=30,y=280)
        
        # making button to continue
        self.continue_button=Button(self.login_frame,text="Continue" ,font=("arail",16,"bold") ,fg="#FFFFFF",bg='#071828',command=self.forget_passwords)
        self.continue_button.place(x=170,y=320)
        
        self.root.mainloop()

    def forget_passwords(self):
        if self.email_entry.get() and self.new_password_entry.get() :
            res=database.forget_password((self.email_entry.get(),self.new_password_entry.get()))
            if res:
                messagebox.showinfo("Success", "Your Password is now Update.")
            elif self.email_entry.get()=="" or self.new_password_entry.get()=="":
                messagebox.showwarning("Warning","Fill Your Details.")
        else:
            messagebox.showerror("Error","Something went wrong.")
        
if __name__=="__main__":
    main()


