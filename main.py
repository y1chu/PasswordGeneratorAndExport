import random
import string
import tkinter as tk
from tkinter import messagebox


# function to generate the password
def generate_password():
    # getting the length of the password from the entry box
    length = int(length_entry.get())
    # getting the number of passwords to be generated from the entry box
    number_of_passwords = int(number_of_passwords_entry.get())
    # checking if the length of the password is less than 8
    if length < 8:
        # displaying an error message
        messagebox.showerror("Error", "The length of the password must be greater than 8")
    else:
        messagebox.showinfo("Password generated", "Password generated. See password.txt for output.")
        # opening the file to write the password
        with open("password.txt", "w") as file:
            # looping through the number of passwords to be generated
            for i in range(number_of_passwords):
                # generating the password
                password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
                # writing the password to the file
                file.write(password + "" + "\n")
                # displaying the password in the GUI window
                password_label.config(text=password)



# creating the GUI window
window = tk.Tk()
# setting the title of the GUI window
window.title("Password Generator")
# setting the size of the GUI window
window.geometry("500x300")
# setting the background color of the GUI window
window.config(bg="pink")

# creating the heading label
heading_label = tk.Label(window, text="Password Generator", font=("Arial", 20), bg="black", fg="white")
# placing the heading label
heading_label.pack(pady=10)

# creating the length label
length_label = tk.Label(window, text="Length of the password", font=("Arial", 15), bg="black", fg="white")
# placing the length label
length_label.pack(pady=10)

# creating the length entry box
length_entry = tk.Entry(window, font=("Arial", 15))
# placing the length entry box
length_entry.pack(pady=10)

# creating the number of passwords label
number_of_passwords_label = tk.Label(window, text="Number of passwords", font=("Arial", 15), bg="black", fg="white")
# placing the number of passwords label
number_of_passwords_label.pack(pady=10)

# creating the number of passwords entry box
number_of_passwords_entry = tk.Entry(window, font=("Arial", 15))
# placing the number of passwords entry box
number_of_passwords_entry.pack(pady=10)

# creating the generate button
generate_button = tk.Button(window, text="Generate", font=("Arial", 15), bg="black", fg="white",
                            command=generate_password)
# placing the generate button
generate_button.pack(pady=10)

# creating the password label
password_label = tk.Label(window, text="", font=("Arial", 15), bg="black", fg="white")
# placing the password label
password_label.pack(pady=10)

# running the GUI window
window.mainloop()
