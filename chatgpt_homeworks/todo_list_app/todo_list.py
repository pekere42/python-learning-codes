from tkinter import *
from tkinter import messagebox
import json
import sys
import os

def resource_path(relative_path):
    """PyInstaller ile paketlenince dosya yolu doğru şekilde alınsın diye"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_data_file():
    """tasks.json dosyasını kalıcı bir yere (kullanıcının AppData klasörüne) kaydeder."""
    app_folder = os.path.join(os.getenv("APPDATA"), "MyToDoApp")
    os.makedirs(app_folder, exist_ok=True)
    return os.path.join(app_folder, "tasks.json")

def load_tasks():
    try:
        with open(get_data_file(), "r", encoding="utf-8") as f:
            data = json.load(f)
            for task, detail in data.items():
                task_details[task] = detail
                my_listbox.insert(END, task)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        messagebox.showerror("Hata", "tasks.json dosyası okunamadı!")

def save_tasks():
    with open(get_data_file(), "w", encoding="utf-8") as f:
        json.dump(task_details, f, ensure_ascii=False, indent=4)

def add_task():
    veri = data_entry.get()
    if not veri.strip():
        messagebox.showwarning("Uyarı", "Görev boş olamaz!")
        return
    if veri in task_details:
        messagebox.showwarning("Uyarı", "Bu görev zaten var!")
        return
    my_listbox.insert(END, veri)
    task_details[veri] = ""
    data_entry.delete(0, END)
    save_tasks()

def open_task_detail():
    selected_index = my_listbox.curselection()
    if not selected_index:
        return
    task = my_listbox.get(selected_index)

    def delete_task():
        cevap = messagebox.askyesno("Sil", "Bu görevi silmek istediğine emin misin?")
        if cevap:
            my_listbox.delete(selected_index)
            task_details.pop(task, None)
            save_tasks()
            top.destroy()

    def save_task_detail():
        metin = text_input.get("1.0", END).strip()
        task_details[task] = metin
        save_tasks()
        messagebox.showinfo("Bilgi", "Görev detayları kaydedildi!")

    top = Toplevel()
    top.geometry("300x250")
    top.title("Görev Detayı")
    top.config(bg="#2b2b2b")

    task_label = Label(top, text=task, fg="yellow", bg="black", font=("Arial", 12, "bold"))
    task_label.pack(pady=5)

    text_input = Text(top, width=30, height=5, bg="#e3e5df", fg="grey", font="Arial 12")
    text_input.pack(pady=10)
    text_input.insert("1.0", task_details.get(task, ""))
    text_input.focus()

    delete_button = Button(top, text="Sil", command=delete_task)
    delete_button.pack(pady=5)

    save_button = Button(top, text="Kaydet", command=save_task_detail)
    save_button.pack(pady=5)

def on_closing():
    save_tasks()
    window.destroy()

# ---------- GUI BAŞLANGICI ----------
window = Tk()
window.geometry("800x800")
window.title("To-Do List")
window.config(bg="#2b2b2b")
window.resizable(False, False)

task_details = {}

# Resimleri yükle
try:
    ikon = PhotoImage(file=resource_path("pngwing.com.png"))
    ikon_2 = PhotoImage(file=resource_path("delete_button.png"))
except:
    ikon = None
    ikon_2 = None

my_label = Label(text="TO-DO LİST", fg="white", bg="grey", font="Segoe 50")
my_label.pack()

data_entry = Entry(width=70, font=("Arial", 15))
data_entry.pack(pady=10, ipady=10)
data_entry.focus()
data_entry.bind("<Return>", lambda event: add_task())

frame = Frame(window)
frame.pack(pady=40)

my_listbox = Listbox(frame, height=20, width=30, font=("Arial", 15))
my_listbox.pack(side=LEFT, fill=BOTH)
my_listbox.bind("<Double-Button-1>", lambda event: open_task_detail())

add_button = Button(window, text="", image=ikon, bd=0, highlightthickness=0, cursor="hand2", command=add_task)
add_button.pack()

my_scrollbar = Scrollbar(frame)
my_listbox.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

window.protocol("WM_DELETE_WINDOW", on_closing)

load_tasks()
window.mainloop()
