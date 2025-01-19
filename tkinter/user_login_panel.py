#importing necessary libraries
from tkinter import *
from tkinter import messagebox



#preparing window and creating its name and size
root = Tk()
root.title("User Login Panel")
root.geometry("600x400+200+200")
root.config(padx=20, pady=20)

registered_username = "melahatpeker"
registered_password = ("kardelen")
def succesful_trial():
    username_label.destroy()
    password_label.destroy()
    username_entry.destroy()
    password_entry.destroy()
    enter_button.destroy()
    message_true = Label(root, text="Entered Data İs Succesful \n Welcome",fg="green")
    message_true.pack()
def unsuccesful_trial():
    messagebox.showerror("Error", "Entered Data İs İncorrect \n Try Again")
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    username_entry.focus()






def check_trial():
    entered_username = str(username_entry.get())
    entered_password = str(password_entry.get())
    if entered_username == registered_username and entered_password == registered_password:
        succesful_trial()
    else:
        unsuccesful_trial()







username_label = Label(text="Username", fg="black", bg="white")
username_label.grid(column=0, row=0, padx=50, pady=5)
password_label = Label(text="Password", fg="black", bg="white")
password_label.grid(column=0, row=1)
username_entry = Entry(root, fg="black", bg="white", width=60)
username_entry.grid(column=1, row=0)
password_entry = Entry(root, fg="black", bg="white", width=60, show="*")
password_entry.grid(column=1, row=1)
enter_button = Button(text="Enter", fg="black", bg="white", width=40,command=check_trial)
enter_button.grid(column=1, row=2)












root.mainloop()


