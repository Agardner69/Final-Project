import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os

def main():
    root = tk.Tk()
    root.title("Insurance Schedule Helper")
    root.geometry("630x500")
    build_main_window(root)
    root.mainloop()

def build_main_window(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Insurance Schedule Helper", font=("Helvetica", 14)).pack(pady=10)

    tk.Label(root, text="Enter Full Name:").pack(pady=2)
    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=2)

    tk.Label(root, text="Enter Age:").pack(pady=2)
    age_entry = tk.Entry(root, width=10)
    age_entry.pack(pady=2)

    tk.Label(root, text="Select Insurance Type:").pack(pady=5)

    insurance_var = tk.StringVar()
    insurance_var.set("Life")

    insurance_frame = tk.Frame(root)
    insurance_frame.pack(pady=10, padx=50)

    current_dir = os.path.dirname(os.path.abspath(__file__))

    life_frame = tk.Frame(insurance_frame, borderwidth=1, relief="groove", padx=5, pady=5)
    life_frame.grid(row=0, column=0, padx=5)
    tk.Radiobutton(life_frame, text="Life", variable=insurance_var, value="Life").pack()
    tk.Label(life_frame, text="[Life Image Missing]").pack()

    health_frame = tk.Frame(insurance_frame, borderwidth=1, relief="groove", padx=5, pady=5)
    health_frame.grid(row=0, column=1, padx=5)
    tk.Radiobutton(health_frame, text="Health", variable=insurance_var, value="Health").pack()
    tk.Label(health_frame, text="[Health Image Missing]").pack()

    acc_frame = tk.Frame(insurance_frame, borderwidth=1, relief="groove", padx=5, pady=5)
    acc_frame.grid(row=0, column=2, padx=5)
    tk.Radiobutton(acc_frame, text="Accidental", variable=insurance_var, value="Accidental").pack()
    tk.Label(acc_frame, text="[Accidental Image Missing]").pack()

    tk.Button(root, text="Next", command=lambda: build_scheduling_window(root, name_entry, age_entry, insurance_var)).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

def build_scheduling_window(root, name_entry, age_entry, insurance_var):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Schedule Your Appointment", font=("Helvetica", 14)).pack(pady=10)

    tk.Label(root, text="Month:").pack(pady=5)
    month_var = tk.StringVar()
    month_var.set("January")
    tk.OptionMenu(root, month_var, "January", "February", "March", "April", "May", "June").pack()

    tk.Label(root, text="Day:").pack(pady=5)
    day_var = tk.StringVar()
    day_var.set("1")
    tk.OptionMenu(root, day_var, *[str(i) for i in range(1, 32)]).pack()

    tk.Label(root, text="Time:").pack(pady=5)
    time_var = tk.StringVar()
    time_var.set("9:00 AM")
    tk.OptionMenu(root, time_var, "9:00 AM", "11:00 AM", "2:00 PM", "4:00 PM").pack()

    tk.Button(root, text="Confirm", command=lambda: build_review_window(root, name_entry, age_entry, insurance_var, month_var, day_var, time_var)).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: build_main_window(root)).pack(pady=5)

def build_review_window(root, name_entry, age_entry, insurance_var, month_var, day_var, time_var):
    for widget in root.winfo_children():
        widget.destroy()

    name = name_entry.get().strip()
    age = age_entry.get().strip()
    insurance_type = insurance_var.get()
    month = month_var.get()
    day = day_var.get()
    time = time_var.get()

    tk.Label(root, text="Review Your Information", font=("Helvetica", 14)).pack(pady=10)
    tk.Label(root, text=f"Name: {name}").pack(pady=2)
    tk.Label(root, text=f"Age: {age}").pack(pady=2)
    tk.Label(root, text=f"Insurance Type: {insurance_type}").pack(pady=2)
    tk.Label(root, text=f"Appointment: {month} {day} at {time}").pack(pady=10)

    tk.Button(root, text="Confirm", command=lambda: confirm_appointment(root)).pack(pady=10)

def confirm_appointment(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Appointment Confirmed!", font=("Helvetica", 14)).pack(pady=10)
    tk.Label(root, text="Thank you for using the Insurance Schedule Helper.").pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

if __name__ == "__main__":
    main()
