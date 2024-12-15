# M08 Final Project 
# 2024/12/15
# AG
# Visual Code Studio

#Import Modules
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os

def main():
    #Create main application window
    root = tk.Tk()
    root.title("Insurance Schedule Helper")
    root.geometry("630x500")

    # Set background color of the app window
    root.configure(bg="#420D09")  #Pretty Dark Red Background

    # Build main window UI
    build_main_window(root)

    # Start GUI 
    root.mainloop()

def build_main_window(root):
    """
    Build main window for collecting client information.
    Includes fields for Name, Age, Email, Phone, and Insurance Type.
    """
    # Clear the window first if needed
    for widget in root.winfo_children():
        widget.destroy()

    # Add title 
    tk.Label(root, text="Welcome to the Insurance Schedule Helper", font=("Helvetica", 14)).pack(pady=10)

    # Name
    tk.Label(root, text="Enter Full Name:").pack(pady=2)
    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=2)

    # Age
    tk.Label(root, text="Enter Age:").pack(pady=2)
    age_entry = tk.Entry(root, width=10)
    age_entry.pack(pady=2)

    # Email
    tk.Label(root, text="Enter Email:").pack(pady=2)
    email_entry = tk.Entry(root, width=30)
    email_entry.pack(pady=2)

    # Phone
    tk.Label(root, text="Enter Phone Number:").pack(pady=2)
    phone_entry = tk.Entry(root, width=20)
    phone_entry.pack(pady=2)

    # Insurance Type Section
    tk.Label(root, text="Select Insurance Type:").pack(pady=5)

    insurance_var = tk.StringVar()
    insurance_var.set("Life")  # default selection

    # Frame to hold three option boxes
    insurance_frame = tk.Frame(root)
    insurance_frame.pack(pady=10)

    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # LIFE BOX 
    life_frame = tk.Frame(insurance_frame, borderwidth=1, relief="groove", padx=5, pady=5)
    life_frame.grid(row=0, column=0, padx=5)
    life_radio = tk.Radiobutton(life_frame, text="Life", variable=insurance_var, value="Life")
    life_radio.pack(anchor="center", pady=5)

    try:
        life_img = Image.open(os.path.join(current_dir, "Life_Insurance.png")).resize((50, 50))
        life_img_tk = ImageTk.PhotoImage(life_img)
        life_label = tk.Label(life_frame, image=life_img_tk)
        life_label.pack()
        life_frame.life_img_tk = life_img_tk  # Garbage prevention
    except FileNotFoundError:
        tk.Label(life_frame, text="[Life Insurance Image Missing]").pack()

    # HEALTH BOX 
    health_frame = tk.Frame(insurance_frame, borderwidth=1, relief="groove", padx=5, pady=5)
    health_frame.grid(row=0, column=1, padx=5)
    health_radio = tk.Radiobutton(health_frame, text="Health", variable=insurance_var, value="Health")
    health_radio.pack(anchor="center", pady=5)

    try:
        health_img = Image.open(os.path.join(current_dir, "Health_Insurance.png")).resize((50, 50))
        health_img_tk = ImageTk.PhotoImage(health_img)
        health_label = tk.Label(health_frame, image=health_img_tk)
        health_label.pack()
        health_frame.health_img_tk = health_img_tk  # Garbage Prevention
    except FileNotFoundError:
        tk.Label(health_frame, text="[Health Insurance Image Missing]").pack()

    # ACCIDENTAL BOX 
    acc_frame = tk.Frame(insurance_frame, borderwidth=1, relief="groove", padx=5, pady=5)
    acc_frame.grid(row=0, column=2, padx=5)
    acc_radio = tk.Radiobutton(acc_frame, text="Accidental", variable=insurance_var, value="Accidental")
    acc_radio.pack(anchor="center", pady=5)

    try:
        acc_img = Image.open(os.path.join(current_dir, "Accidental.png")).resize((50, 50))
        acc_img_tk = ImageTk.PhotoImage(acc_img)
        acc_label = tk.Label(acc_frame, image=acc_img_tk)
        acc_label.pack()
        acc_frame.acc_img_tk = acc_img_tk  # Garbage Prevention
    except FileNotFoundError:
        tk.Label(acc_frame, text="[Accidental Insurance Image Missing]").pack()

    # Navigation Buttons
    tk.Button(root, text="Next", command=lambda: validate_and_go(name_entry, age_entry, email_entry, phone_entry, insurance_var, root)).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

def validate_and_go(name_entry, age_entry, email_entry, phone_entry, insurance_var, root):
    """
    Validate user inputs from main window.
    If valid, proceed to the offerings window.
    """
    name = name_entry.get().strip()
    age_str = age_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    insurance_type = insurance_var.get()

    # Validate Name
    if not name:
        messagebox.showerror("Input Error", "Name cannot be empty.")
        return

    # Validate Age
    if not age_str.isdigit():
        messagebox.showerror("Input Error", "Age must be a number.")
        return
    age = int(age_str)
    if age < 18 or age > 120:
        messagebox.showerror("Input Error", "Age must be between 18 and 120.")
        return

    # Validate Email ("@" and "." check)
    if "@" not in email or "." not in email:
        messagebox.showerror("Input Error", "Please enter a valid email.")
        return

    # Validate Phone (10 digit check)
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Input Error", "Phone number must be exactly 10 digits.")
        return

    # If all validations pass, store data
    client_data = {
        "name": name,
        "age": age,
        "email": email,
        "phone": phone,
        "insurance_type": insurance_type}

    # Move to next window
    build_offerings_window(root, client_data)

def build_offerings_window(root, client_data):
    """
    Display chosen insurance product details and images.
    Provide button to Scheduling or back to the main window.
    """
    for widget in root.winfo_children():
        widget.destroy()

    # Title label
    tk.Label(root, text=f"You selected {client_data['insurance_type']} Insurance", font=("Helvetica", 12)).pack(pady=10)

    # Add label as a heading
    tk.Label(root, text="Here is more information about this product:", font=("Helvetica", 10)).pack(pady=5)

    # Create a text box to display insurance-specific information
    info_text = tk.Text(root, wrap="word", width=70, height=10)
    info_text.pack(pady=10)

    # Present Insurance infomation based on the selected insurance type
    if client_data['insurance_type'] == "Life":
        info_content = (
            "This insurance plan provides coverage for:\n\n"
            "There are currently over 20 different plans from multiple carriers we will search through. "
            "The main types of plans include:\n"
            "- Whole Life: A traditional plan for those with guaranteed growth rates and coverage that will last you a lifetime.\n"
            "- Indexed Universal Life (IUL): A varied interest plan that is indexed to the S&P 500 with a guaranteed 0% minimum "
            "on growth that will last you a lifetime.\n"
            "- Term Life: A short-term life insurance product designed for those looking for the cheapest coverage to help them "
            "bridge a gap and provide limited-time security.\n\n"
            "Coverage includes:\n"
            "- Whole Life (18-40) & (55-110)\n"
            "- IUL (18-110)\n"
            "- Term (18-110)"
        )
    elif client_data['insurance_type'] == "Health":
        info_content = (
            "This Health Insurance plan provides coverage for:\n\n"
            "Individual health plans and group plans are available from 7 different companies, along with dental from 3 companies.\n\n"
            "This Health Insurance plan is tailored to fit your personal needs, wants, and desires. "
            "You can choose the coverage that best suits your lifestyle, ensuring peace of mind for you and your family."
        )
    elif client_data['insurance_type'] == "Accidental":
        info_content = (
            "This Accidental Insurance plan provides coverage against accidental death and dismemberment.\n\n"
            "Coverage details:\n"
            "- Available for individuals aged 18 and above\n"
            "- Provides financial security in case of accidents."
        )
    else:
        info_content = "Details about this insurance type will be provided during the appointment."

    # Insert text into text box
    info_text.insert("1.0", info_content)
    info_text.config(state="disabled")  # Disable text box to make it read-only

    # Navigation buttons
    tk.Button(root, text="Proceed to Scheduling", command=lambda: go_to_scheduling(root, client_data)).pack(pady=5)
    tk.Button(root, text="Back", command=lambda: build_main_window(root)).pack(pady=5)



def go_to_scheduling(root, client_data):
    """
    Transition to appointment scheduling window.
    """
    build_scheduling_window(root, client_data)

def build_scheduling_window(root, client_data):
    """
    Provide date and time selection for the appointment.
    """
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select an Appointment Date and Time", font=("Helvetica", 12)).pack(pady=10)

    # Simple dropdowns for date 
    # Placeholder for real calender widgit system
    tk.Label(root, text="Month:").pack(pady=2)
    month_var = tk.StringVar()
    month_var.set("January")
    tk.OptionMenu(root, month_var, "January", "February", "March", "April", "May", "June", "July", "Augest", "September", "October", "November", "Decemeber").pack()

    tk.Label(root, text="Day:").pack(pady=2)
    day_var = tk.StringVar()
    day_var.set("1")
    tk.OptionMenu(root, day_var, *[str(i) for i in range(1,32)]).pack()

    tk.Label(root, text="Year:").pack(pady=2)
    year_var = tk.StringVar()
    year_var.set("2024")
    tk.OptionMenu(root, year_var, "2024", "2025",).pack()

    # Time selection
    tk.Label(root, text="Time Slot:").pack(pady=2)
    time_var = tk.StringVar()
    time_var.set("11:00 AM")
    tk.OptionMenu(root, time_var, "11:00 AM", "2:00 PM", "4:00 PM").pack()

    # Buttons
    tk.Button(root, text="Review & Confirm", command=lambda: build_review_window(root, client_data, month_var, day_var, year_var, time_var)).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: build_offerings_window(root, client_data)).pack(pady=5)

def build_review_window(root, client_data, month_var, day_var, year_var, time_var):
    """
    Display all data for final review and allow submission.
    """
    for widget in root.winfo_children():
        widget.destroy()

    appointment_date = f"{month_var.get()} {day_var.get()}, {year_var.get()}"
    appointment_time = time_var.get()

    # Update client_data with appointment info
    client_data["appointment_date"] = appointment_date
    client_data["appointment_time"] = appointment_time

    tk.Label(root, text="Review Your Information", font=("Helvetica", 14)).pack(pady=10)
    tk.Label(root, text=f"Name: {client_data['name']}").pack(pady=2)
    tk.Label(root, text=f"Age: {client_data['age']}").pack(pady=2)
    tk.Label(root, text=f"Email: {client_data['email']}").pack(pady=2)
    tk.Label(root, text=f"Phone: {client_data['phone']}").pack(pady=2)
    tk.Label(root, text=f"Insurance Type: {client_data['insurance_type']}").pack(pady=2)
    tk.Label(root, text=f"Appointment Date: {client_data['appointment_date']}").pack(pady=2)
    tk.Label(root, text=f"Appointment Time: {client_data['appointment_time']}").pack(pady=2)

    # Buttons
    tk.Button(root, text="Submit Appointment", command=lambda: submit_appointment(root, client_data)).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: build_scheduling_window(root, client_data)).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

def submit_appointment(root, client_data):
    """
    Finalizes booking, displays confirmation, and simulates sending data to the broker.
    """
    messagebox.showinfo("Confirmation", "Your appointment has been scheduled!")
    print("Sending the following data to the broker:")
    for k, v in client_data.items():
        print(f"{k}: {v}")
    # Place holder for an integrated email system that would update a connected google calender

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Thank you! Your appointment has been sent to the broker.", font=("Helvetica", 12)).pack(pady=20)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

if __name__ == "__main__":
    main()
