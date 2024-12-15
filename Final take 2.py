
# Import Modules
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def main():
    """
    Main function to run the application.
    """
    root = tk.Tk()
    root.title("Insurance Schedule Helper")
    root.geometry("300x400")

    # Start the application at the main window
    build_main_window(root)

    root.mainloop()


def build_main_window(root):
    """
    Build the main window for collecting user information.
    """
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Title label
    tk.Label(root, text="Welcome to the Insurance Schedule Helper", font=("Helvetica", 14)).pack(pady=10)

    # Name entry
    tk.Label(root, text="Enter Full Name:").pack(pady=5)
    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=5)

    # Age entry
    tk.Label(root, text="Enter Age:").pack(pady=5)
    age_entry = tk.Entry(root, width=10)
    age_entry.pack(pady=5)

    # Insurance type
    tk.Label(root, text="Select Insurance Type:").pack(pady=5)
    insurance_var = tk.StringVar(value="Life")

    # Radio buttons for insurance selection
    tk.Radiobutton(root, text="Life", variable=insurance_var, value="Life").pack(anchor="w")
    tk.Radiobutton(root, text="Health", variable=insurance_var, value="Health").pack(anchor="w")
    tk.Radiobutton(root, text="Accidental", variable=insurance_var, value="Accidental").pack(anchor="w")

    # Navigation buttons
    tk.Button(root, text="Next", command=lambda: go_to_next_window(root, name_entry, age_entry, insurance_var)).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack()


def go_to_next_window(root, name_entry, age_entry, insurance_var):
    """
    Transition to the next window (summary screen).
    """
    # user input
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    insurance_type = insurance_var.get()

    # Validate Name
    if not name:
        messagebox.showerror("Input Error", "Name cannot be empty!")
        return

    # Validate Age
    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Input Error", "Age must be a valid number!")
        return

    # Transition to the summary window
    build_summary_window(root, name, age, insurance_type)


def build_summary_window(root, name, age, insurance_type):
    """
    Build the summary window to show user details and transition to scheduling.
    """
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Display user information
    tk.Label(root, text="Summary of Information", font=("Helvetica", 14)).pack(pady=10)
    tk.Label(root, text=f"Name: {name}").pack(pady=5)
    tk.Label(root, text=f"Age: {age}").pack(pady=5)
    tk.Label(root, text=f"Selected Insurance: {insurance_type}").pack(pady=5)

    # Navigation buttons
    tk.Button(root, text="Proceed to Scheduling", command=lambda: build_scheduling_window(root, name, age, insurance_type)).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: build_main_window(root)).pack()


def build_scheduling_window(root, name, age, insurance_type):
    """
    Provide a simplified scheduling window and directly confirm the appointment.
    """
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Title
    tk.Label(root, text="Schedule Your Appointment", font=("Helvetica", 24)).pack(pady=10)

    # Month selection
    tk.Label(root, text="Select Month:").pack(pady=5)
    month_var = tk.StringVar(value="January")
    month_dropdown = tk.OptionMenu(root, month_var, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    month_dropdown.pack()

    # Day selection
    tk.Label(root, text="Select Day:").pack(pady=5)
    day_var = tk.StringVar(value="1")
    day_dropdown = tk.OptionMenu(root, day_var, *[str(i) for i in range(1, 32)])
    day_dropdown.pack()

    # Time selection
    tk.Label(root, text="Select Time:").pack(pady=5)
    time_var = tk.StringVar(value="9:00 AM")
    time_dropdown = tk.OptionMenu(root, time_var, "9:00 AM", "11:00 AM", "2:00 PM", "4:00 PM")
    time_dropdown.pack()

    # Confirm Button
    def confirm():
        for widget in root.winfo_children():
            widget.destroy()

        # Display confirmation message
        tk.Label(root, text="Appointment Confirmed!", font=("Helvetica", 14)).pack(pady=10)
        tk.Label(root, text=f"Thank you, {name}!").pack(pady=5)
        tk.Label(root, text=f"Age: {age}").pack(pady=5)
        tk.Label(root, text=f"Insurance Type: {insurance_type}").pack(pady=5)
        tk.Label(root, text=f"Appointment Date: {month_var.get()} {day_var.get()}, Time: {time_var.get()}").pack(pady=10)

        # Exit Button
        exit_button = tk.Button(root, text="Exit", command=root.destroy)
        exit_button.pack(pady=10)

    confirm_button = tk.Button(root, text="Confirm Appointment", command=confirm)
    confirm_button.pack(pady=10)

    # Back Button
    back_button = tk.Button(root, text="Back", command=lambda: build_summary_window(root, name, age, insurance_type))
    back_button.pack(pady=5)



if __name__ == "__main__":
    main()
