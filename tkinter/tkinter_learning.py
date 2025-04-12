from tkinter import *

window = Tk()
window.geometry("800x600")
window.title("Aynen Tkinter Öğrencem")

def click_clear_button():
    data_entry.delete(0, END)
def click_send_button():
    print("button clicked")
    data_entry.get()#data entryde yazılan veriyi almamızı sağlıyor onu bir deiişkene attık ve printledik
    data_input = data_entry.get()
    print(data_input)

def click_send_button_2():
    data_input_text = text_input.get("1.0",END)#textte veriyi almak için entryden farklı olarak başlangıç ve bitiş endexi vermemiz gerekiyor
    print(data_input_text)


data_entry = Entry(width=40)#veri girişi kısmı oluşturma
data_entry.pack()


clear_button = Button(text="Clear",width=30,command=click_clear_button)#command defi belirtme zaten biliyorsun
clear_button.pack()

send_button = Button(text="Send",width=30,command=click_send_button)
send_button.pack()

text_input = Text(width=30,height=5,bg= "light blue",fg="black",font="Arial 15")
text_input.pack(padx=10,pady=10)#sağdan ve soldan 10 piksel boşluk bırak demiş oldum
text_input.focus()

send_button_2 = Button(text="Send 2",width=30,command=click_send_button_2)
send_button_2.pack()
    











window.mainloop()
""""""""""""""""""""""""""
from tkinter import *

window = Tk()
window.title("python")#pencerenin adı
window.geometry("600x600")#boyutu ve ekranda nerede konumlanacağı



my_label = Label(text="this is a label",fg="red",bg="blue",font="Algerian 50 bold underline")
#my_label.pack(side="left")#zorunlu sonraki derste öğrenicez
my_label.grid(column=0,row=3)
def button_clicked():
    my_label.config(text="button clicked",fg="green")#butona basınca değiştirdi
    #print("butona tıklandı")



my_button = Button(text="benim butonum",fg="red",bg="blue",command=button_clicked)#buton oluşturma ve özellikleri tanımlma çok kullanıcaz
#my_button.pack(side="left")
#my_button.place(x=100,y=100)#(0,0) kordinatı sol üst oluyor pack, place,grid kullanabilirsin niyete göre
my_button.grid(column=2,row=3)
my_label_2 = Label(text="this is a label2",
                 fg="red",
                 bg="blue",
                 font="Algerian 50 bold underline")#yazı biçimi    #yazı tipi ve büyüklüğü bu şekilde belirtilebilir
#my_label_2.pack(side="left")#left,right,top ve bottom versiyonu var=>top default versiyonu
my_label_2.grid(column=1,row=3)#sayfayı parsellere ayırıyor






window.mainloop()
""""""""""""""""""
from tkinter import *
#kullanıcıların seçtiği elemanları alabilmek için kullanılır
window = Tk()
window.title("Python Tkinter Widgets")
window.geometry("600x600+200+200")

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))


my_listbox = Listbox()#klasik widget oluşturma hamlesi

item_list = ["item1","item2","item3","item4","item5","item6"]
for i in range(len(item_list)):  #range(len()) ile dinamik bir hamle yaptık listeye eleman eklense bile o kadar çalışacak
    my_listbox.insert(i,item_list[i])

my_listbox.bind("<<ListboxSelect>>",listbox_selected)#fonksiyonu text ile bağlamak için kullanılan ezber yöntem ezberle

my_listbox.pack()





window.mainloop()
""""""""""""
#import tkinter   => bu şekilde de edilebilir alttaki gibi de edilebilir
from tkinter import *

window = Tk()
window.title("python tkinter")
window.geometry("600x400+300+300")#x kısmında pencerenin boyutu + kısmında ise üstten ve soldan ne kadar boşluk bırakması gerektiği
#window.minsize(300,200)
#window.maxsize(700,500)
window.resizable(FALSE,TRUE)#dikey ya da yatay genişletmeyi ayarlama
my_label = Label(text="this is a label")
my_label.pack()


window.mainloop()
""""""""""""
from tkinter import *

root = Tk()
root.geometry("400x200+250+250")
root.title("Menu Learning")

menubar = Menu(root)#üstteki ilk menünün açılışı
root.config(menu=menubar)#ezber kod.d


file_menu = Menu(menubar,tearoff=0)#menünün içindeki menüyü oluşturma,tearoff 3 çizgiyi kaldırmak içindi chatgpt de yapabilir

menubar.add_cascade(label="File", menu=file_menu)#ezber işlemler

def open_button():#yeni pencere açma defi buton görevi görüyor
    open_window = Toplevel(root)
def copy_button():#basic basınca terminale yazdır
    print("copied")


file_menu.add_command(label="Open",command=open_button)#teker teker isim verip ekleme
#file_menu.add_command(label="Save")
save_menu = Menu(file_menu,tearoff=0)#yeni menü açma
file_menu.add_cascade(label="Save", menu=save_menu)#ezber
save_menu.add_command(label=".py")
save_menu.add_command(label=".exe")

file_menu.add_command(label="Exıt",command=exit)

edit_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy",command=copy_button)




root.mainloop()
""""""""""""
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x200+250+250")
root.title("Messagebox Learning")

#def click_message_button():
    # information messagebox
    # messagebox.showinfo("showinfo", "information")
    # warning messagebox
    # messagebox.showwarning("showwarning", "warning")
    # error messagebox
    # messagebox.showerror("showerror", "error")

    # Question messagebox
    # messagebox.askquestion("askquestion","Are You Sure?")
    # messagebox.askokcancel("askokcancel","Want To Continue?")
    # messagebox.askyesno("askyesno","Find The Value?")
    # messagebox.askretrycancel("askretrycancel","Try Again?")
    # messagebox.askyesnocancel("askyesnocancel","Are You Sure?")


message_button = Button(root,text="Message",command=click_message_button)
message_button.pack()





root.mainloop()
""""""""""""""
from tkinter import *

window = Tk()
window.title("Tkinter Learning")
window.geometry("600x400")

#scale

my_scale = Scale(from_=100,to=200,orient=HORIZONTAL,label="volume")#kaç ile kaç arasını alabilsin burada belirledim label de koyabilirim
my_scale.pack(side=LEFT)

my_scale_2 = Scale(from_=1,to=100,label="bas")
my_scale_2.pack(side=LEFT)

#spinbox
def spinbox_selected():#scale de value demiştim burada dememe gerek yok
    print(my_spinbox.get())


my_spinbox  = Spinbox(from_=0,to=100,values=(0,10,20,30,40,50,60,70,80,90,100),command=spinbox_selected)#values kısmında alabileceği değerleri belirledim
my_spinbox.pack()








window.mainloop()
""""""""""""
from tkinter import *

window = Tk()
window.title("python")#pencerenin adı
#window.geometry("600x600+200+200")#boyutu ve ekranda nerede konumlanacağı
"""
my_scrollbar = Scrollbar()
my_scrollbar.pack(side=RIGHT,fill=Y)#side nerede konumlanacağı,fill ile de o klasik tamamı doldurulmuş görüntüyü sağlamak için kullan

my_text = Text(yscrollcommand=my_scrollbar.set)#text ile scrollbarı bağlamak için
my_text.pack()

my_scrollbar.config(command=my_text.yview)#işlemleri anlık olarak takip etmesi için config ettik
"""
my_scrollbar = Scrollbar()#dikey olarak yönel diyorum y de belirtmeye gerek yok x de biraz daha karışık
my_scrollbar.pack(side=RIGHT,fill=Y)#side nerede konumlanacağı,fill ile de o klasik tamamı doldurulmuş görüntüyü sağlamak için kullan

#my_text = Text(wrap=NONE,xscrollcommand=my_scrollbar.set)
#my_text.pack()

my_list = Listbox(yscrollcommand=my_scrollbar.set, width=30,height=10)

for line in range(1,100):
    my_list.insert(END,"Item" + str(line))

my_list.pack(side=LEFT,fill=BOTH)
my_scrollbar.config(command=my_list.yview)



window.mainloop()
""""""""""""""""""
from tkinter import *

root = Tk()
root.title("Tkinter Learning")
root.geometry("400x300")

label1 = Label(root,text="This is a label")#iki pencere varsa root yazılan yere top da yazabilirim nerede çalışacağını belirlemem lazım bişey yazmassam rootta çalışır
label1.pack()

def add_window():
    top = Toplevel()
    top.geometry("200x100")
    top.title("Toplevel")
    label2 = Label(top,text="This is toplevel label")
    label2.pack()
    #exit_button = Button(top,text="exit",command=top.destroy)
    exit_button = Button(top, text="exit", command=exit)#top.destroy sadece top windowu kapatıyor exit direk tüm pencereleri kapatıyor
    exit_button.pack()


add_button=Button(root,text="Add Window",command=add_window)
add_button.pack()

root.mainloop()
""""""""""""
#importing necessary libraries
from tkinter import *
from tkinter import messagebox



#preparing window and creating its name and size
root = Tk()
root.title("User Login Panel")
root.geometry("600x400+200+200")
root.config(padx=20, pady=20)#direk sayfadan boşluk bırakmasını söyledim böylece arasının açılmasını önlemiş oldum configle de çıkmazda kalındığı zaman çözüm üretilebilir

registered_username = "kabadayi24"
registered_password = ("55trendAA.")
def succesful_trial():#iki olasılığı böylece ayırdım
    username_label.destroy()#her şeyi teker teker destroy edebilirim
    password_label.destroy()
    username_entry.destroy()
    password_entry.destroy()
    enter_button.destroy()
    message_true = Label(root, text="Entered Data İs Succesful \n Welcome",fg="green")
    message_true.pack()
def unsuccesful_trial():
    messagebox.showerror("Error", "Entered Data İs İncorrect \n Try Again")
    username_entry.delete(0, END)#kendisini değil sadece yazılan inputu sildim
    password_entry.delete(0, END)
    username_entry.focus()#focuslanmayı biliyorsun






def check_trial():
    entered_username = str(username_entry.get())#yazılan şifre ve kullanıcı adını değişkene çektim
    entered_password = str(password_entry.get())
    if entered_username == registered_username and entered_password == registered_password:
        succesful_trial()
    else:
        unsuccesful_trial()
#if ve else kısmında yapılacak adımları yazmak amatörlük olur başka fonksiyonda hazırlayıp aktarmak kodu daha temiz ve anlaşılır kılacaktır ,yani öyle yap







def enter():
    global username_entry,password_entry,username_label,password_label,enter_button
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


enter()









root.mainloop()
""""""""""""
from tkinter import *

window = Tk()
window.title("Python Tkinter Widgets")
window.geometry("600x600+200+200")

#check button oluşturma
def checkbutton_selected():
    print(check_state.get())

check_state = IntVar()#butona tıklandıysa 1 değerini tıklanmadıysa 2 değerini üretiyor
my_check_button = Checkbutton(text="Check Button",variable=check_state,command=checkbutton_selected)
my_check_button.pack()
#radiobutton oluşturma

def radiobutton_selected():
    print(radio_check_state.get())

radio_check_state = IntVar()

my_radiobutton = Radiobutton(text="Radio Button 1",value=100,variable=radio_check_state,command=radiobutton_selected)
my_radiobutton_2 = Radiobutton(text="Radio Button 2",value=200,variable=radio_check_state,command=radiobutton_selected)
my_radiobutton.pack()
my_radiobutton_2.pack()





window.mainloop()
""""""""""""