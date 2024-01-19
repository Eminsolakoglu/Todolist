import customtkinter
from tkinter import messagebox
import json
"""
    LOGİN EKRANI USERNAME : emin 
    ŞİFRE : 123



"""

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do List Uygulaması")

        self.login_frame = customtkinter.CTkFrame(master=root)
        self.login_frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.login_frame, text="Giriş Sistemi")
        self.label.pack(pady=12, padx=10)

        self.entry1 = customtkinter.CTkEntry(master=self.login_frame, placeholder_text="Kullanıcı Adı")
        self.entry1.pack(pady=12, padx=10)

        self.entry2 = customtkinter.CTkEntry(master=self.login_frame, placeholder_text="Şifre", show="*")
        self.entry2.pack(pady=12, padx=10)

        self.button = customtkinter.CTkButton(master=self.login_frame, text="Giriş", command=self.login)
        self.button.pack(pady=12, padx=10)

        self.checkbox = customtkinter.CTkCheckBox(master=self.login_frame, text="Beni Hatırla")
        self.checkbox.pack(pady=12, padx=10)

        self.todo_frame = customtkinter.CTkFrame(master=root)
        self.todo_frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.todo_frame.pack_forget()

        self.task_entry = customtkinter.CTkEntry(master=self.todo_frame, width=50, height=5)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.day_var = customtkinter.StringVar()
        self.day_combobox = customtkinter.CTkComboBox(master=self.todo_frame, values=["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"])
        self.day_combobox.grid(row=0, column=1, padx=10, pady=10)

        self.add_button = customtkinter.CTkButton(master=self.todo_frame, text="Görev Ekle", command=self.add_task)
        self.add_button.grid(row=1, column=0, padx=10, pady=10)

        self.remove_button = customtkinter.CTkButton(master=self.todo_frame, text="Görev Sil", command=self.remove_task)
        self.remove_button.grid(row=1, column=1, padx=10, pady=10)

        self.show_button = customtkinter.CTkButton(master=self.todo_frame, text="Görevleri Göster", command=self.show_tasks)
        self.show_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.tasks = {"Pazartesi": [], "Salı": [], "Çarşamba": [], "Perşembe": [], "Cuma": [], "Cumartesi": [], "Pazar": []}

    def save_data(self, filename="tasks_data.txt"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)

    def load_data(self, filename="tasks_data.txt"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError as e:
            messagebox.showwarning("Dosya Bulunamadı", f"Dosya '{filename}' bulunamadı. Boş görevlerle başlatılıyor.")
            self.tasks = {"Pazartesi": [], "Salı": [], "Çarşamba": [], "Perşembe": [], "Cuma": [], "Cumartesi": [], "Pazar": []}
        except json.JSONDecodeError as e:
            messagebox.showerror("JSON Çözme Hatası", f"'{filename}' dosyasındaki JSON çözme hatası: {e}")
            self.tasks = {"Pazartesi": [], "Salı": [], "Çarşamba": [], "Perşembe": [], "Cuma": [], "Cumartesi": [], "Pazar": []}

    def login(self):
        entered_username = self.entry1.get()
        entered_password = self.entry2.get()

        if entered_username == "emin" and entered_password == "123":
            self.login_frame.pack_forget()
            self.todo_frame.pack()
        else:
            messagebox.showerror("Hata", "Geçersiz kimlik bilgileri")
            self.load_data()

    def add_task(self):
        task = self.task_entry.get()
        day = self.day_combobox.get()
        if task and day:
            self.tasks[day].append(task)
            messagebox.showinfo("Başarı", f"Görev '{task}' {day} gününe eklendi")
            self.save_data()  # Görev ekledikten sonra veriyi kaydet
        self.load_data()

    def remove_task(self):
        task = self.task_entry.get()
        day = self.day_combobox.get()
        if task and day:
            if task in self.tasks[day]:
                self.tasks[day].remove(task)
                messagebox.showinfo("Başarı", f"Görev '{task}' {day} gününden kaldırıldı")
                self.save_data()  # Görevi kaldırdıktan sonra veriyi kaydet
            else:
                messagebox.showerror("Hata", f"Görev '{task}' {day} gününde bulunamadı")
        self.load_data()

    def show_tasks(self):
        day = self.day_combobox.get()
        if day:
            tasks = self.tasks[day]
            if tasks:
                messagebox.showinfo("Görevler", f"{day} günü için görevler: {', '.join(tasks)}")
            else:
                messagebox.showinfo("Görev Yok", f"{day} günü için görev bulunmamaktadır")
        else:
            messagebox.showerror("Hata", "Lütfen bir gün seçin.")
        self.load_data()

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = ToDoListApp(root)
    root.mainloop()
