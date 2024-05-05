import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk
import threading
import pywhatkit

def schedule_message():
    recipient = recipient_entry.get()
    message = message_entry.get()
    time = time_entry.get()

    # Parse the scheduled time from the entry field
    try:
        schedule_time = datetime.strptime(time, "%Y-%m-%d %H:%M")
    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter the time in the format YYYY-MM-DD HH:MM")
        return

    # Calculate delay in seconds
    delay = (schedule_time - datetime.now()).total_seconds()
    if delay < 0:
        messagebox.showerror("Invalid Time", "Scheduled time must be in the future.")
        return

    # Schedule the message using threading
    try:
        threading.Timer(delay, send_message, args=[recipient, message]).start()
        messagebox.showinfo("Scheduled", f"Message scheduled to send at {time}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to schedule message: {e}")


def send_message(recipient, message):
    try:
        # Use pywhatkit to send the message
        pywhatkit.sendwhatmsg_instantly(recipient, message)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send message: {e}")


# Set up the Tkinter GUI
root = tk.Tk()
root.title("WhatsApp Message Scheduler")
root.geometry("1360x690")
root.resizable(width=False, height=False)
logo = r"C:\python programes\WhatAPP\logo.ico"
try:
    root.iconbitmap(logo)
except tk.TclError as e:
    print(f"Error setting icon: {e}")

# Customize the background image and use it as the background
bg_image_path = r"C:\python programes\WhatAPP\img.jpg" 
try:
    bg_image = Image.open(bg_image_path)
    bg_photo_image = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(root, image=bg_photo_image)
    background_label.place(relwidth=1, relheight=1)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load background image: {e}")

# Create labels, entries, and buttons, and place them on top of the background
heading_label = tk.Label(root, text="WhatsApp Message Scheduler", font=("Helvetica", 24, 'bold'), width=45, fg="#FFFFFF", bg='black', relief="raised", bd=5)
heading_label.place(x=0, y=0)
phone_number_label = tk.Label(root, text="Phone Number:", font=("Helvetica", 18), fg="#FFFFFF", bg="DarkOrange")
phone_number_label.place(x=50, y=100)

recipient_entry = tk.Entry(root, font=("Helvetica", 18), relief="groove", bd=3)
recipient_entry.place(x=50, y=150, width=400)

message_label = tk.Label(root, text="Message:", font=("Helvetica", 18), fg="#FFFFFF", bg="DarkOrange")
message_label.place(x=50, y=250)

message_entry = tk.Entry(root, font=("Helvetica", 18), relief="groove", bd=3)
message_entry.place(x=50, y=300, width=400)

time_label = tk.Label(root, text="Scheduled Time (YYYY-MM-DD HH:MM):", font=("Helvetica", 18), fg="#FFFFFF", bg="DarkOrange")
time_label.place(x=50, y=400)

time_entry = tk.Entry(root, font=("Helvetica", 18), relief="groove", bd=3)
time_entry.place(x=50, y=450, width=400)

schedule_button = tk.Button(root, text="Schedule Message", font=("Helvetica", 18, 'bold'), bg="Green", fg="white", command=schedule_message)
schedule_button.place(x=100, y=550)

root.mainloop()
