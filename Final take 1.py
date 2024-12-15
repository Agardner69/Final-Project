import tkinter as tk
from PIL import Image, ImageTk 

def main():
    root = tk.Tk()
    root.title("Insurance Helper")
    root.geometry("200x400")
    build_main_window(root)
    root.mainloop()

def build_main_window(root):
    # Title
    title = tk.Label(root, text="Insurance Scheduler")
    title.pack()

    # Name Entry
    tk.Label(root, text="Name:").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    # Age Entry
    tk.Label(root, text="Age:").pack()
    age_entry = tk.Entry(root)
    age_entry.pack()

    # Insurance Type Buttons
    tk.Label(root, text="Select Insurance:").pack()
    insurance_var = tk.StringVar()
    insurance_var.set("Life")  # Default selection

    life_radio = tk.Radiobutton(root, text="Life", variable=insurance_var, value="Life")
    life_radio.pack()
    health_radio = tk.Radiobutton(root, text="Health", variable=insurance_var, value="Health")
    health_radio.pack()
    accident_radio = tk.Radiobutton(root, text="Accidental", variable=insurance_var, value="Accidental")
    accident_radio.pack()

    # Next Button
    next_button = tk.Button(root, text="Next", command=lambda: go_to_next_window(root, name_entry, age_entry, insurance_var))
    next_button.pack()

def go_to_next_window(root, name_entry, age_entry, insurance_var):
    # Clears the screen 
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"You selected: {insurance_var.get()}").pack()

    if insurance_var.get() == "Life":
        info = "Life insurance is important!"
        # Image loading 
        try:
            img = ImageTk.PhotoImage(Image.open("Life_Insurance.png"))
            img_label = tk.Label(root, image=img)
            img_label.pack()
        except:
            tk.Label(root, text="[Life Insurance Image]").pack()
    elif insurance_var.get() == "Health":
        info = "Health insurance keeps you healthy!"
    elif insurance_var.get() == "Accidental":
        info = "Accidental insurance protects from accidents!"
    else:
        info = "Unknown insurance type."

    tk.Label(root, text=info).pack()

    tk.Button(root, text="Back", command=lambda: build_main_window(root)).pack()

if __name__ == "__main__":
    main()
