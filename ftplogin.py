import ftplib
import tkinter as tk
from tkinter import messagebox

# Function to handle login button click event
def login():
    server = server_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Attempt to connect to the FTP server and login
    try:
        ftp = ftplib.FTP(server)
        ftp.login(username, password)

        # Do whatever you need to do on the FTP server here
        # For example, change to a specific directory:
        #ftp.cwd('/path/to/directory')

        # Close the FTP connection when you're done
        ftp.quit()
        
        # Show a success message with additional information
        success_msg = f'Successfully connected to {server} as {username}\nFTP server is alive and accessible'
        messagebox.showinfo('FTP Login - Success', success_msg)
        
    except ftplib.all_errors as e:
        # Show an error message if the login fails
        error_msg = f'Failed to connect to {server} as {username}\nError message: {str(e)}'
        messagebox.showerror('FTP Login - Error', error_msg)

# Create the UI window
root = tk.Tk()
root.title('FTP Login - Simple FTP Client')
root.geometry('400x200')  # Set the window size

# Create labels and entry fields for the server, username, and password
server_label = tk.Label(root, text='FTP Server:')
server_label.pack()
server_entry = tk.Entry(root, width=30)
server_entry.pack()

username_label = tk.Label(root, text='Username:')
username_label.pack()
username_entry = tk.Entry(root, width=30)
username_entry.pack()

password_label = tk.Label(root, text='Password:')
password_label.pack()
password_entry = tk.Entry(root, show='*', width=30)
password_entry.pack()

# Create a login button
login_button = tk.Button(root, text='Login', command=login, width=10)
login_button.pack(pady=10)

# Start the UI event loop
root.mainloop()
