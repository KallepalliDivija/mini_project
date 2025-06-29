import tkinter as tk
from tkinter import PhotoImage
from take_image import take_images
from train_model import train_model
from recognize import recognize_faces
import os
from datetime import datetime

def view_attendance():
    path = f"Attendance/Attendance_{datetime.now().strftime('%Y-%m-%d')}.csv"
    if os.path.exists(path):
        os.system(f"notepad.exe {path}")
    else:
        print("No attendance file found for today.")

def take_images_prompt():
    prompt = tk.Toplevel()
    prompt.title("Register Student")
    prompt.geometry("400x200")
    prompt.configure(bg="black")

    tk.Label(prompt, text="Enrollment No:", font=("Arial", 12), bg="black", fg="white").pack(pady=5)
    enroll = tk.Entry(prompt, font=("Arial", 12))
    enroll.pack()

    tk.Label(prompt, text="Name:", font=("Arial", 12), bg="black", fg="white").pack(pady=5)
    name = tk.Entry(prompt, font=("Arial", 12))
    name.pack()

    tk.Button(prompt, text="Capture", font=("Arial", 12), bg="green", fg="white",
              command=lambda: [take_images(enroll.get(), name.get()), prompt.destroy()]).pack(pady=15)

def main():
    window = tk.Tk()
    window.title("NGIT Pratyaksha")
    window.geometry("1000x700")
    window.configure(bg="#1e293b")
    window.resizable(False, False)

    # Header with Logo
    logo_img = PhotoImage(file="icons/pratyaksha-logo.png")
    logo_label = tk.Label(window, image=logo_img, bg="#1e293b")
    logo_label.pack(pady=(20, 10))

    heading = tk.Label(window, text="Face Recognition Attendance System", font=("Helvetica", 20, "bold"),
                       bg="#1e293b", fg="#e0f2fe")
    heading.pack(pady=10)

    # Buttons Frame
    button_frame = tk.Frame(window, bg="#1e293b")
    button_frame.pack(pady=30)

    # Load Button Icons
    register_img = PhotoImage(file="icons/register.png")
    verify_img = PhotoImage(file="icons/verifyy.png")
    attendance_img = PhotoImage(file="icons/attendance.png")

    # Register Student
    tk.Button(button_frame, image=register_img, text="Register", compound="top",
              font=("Arial", 12), bg="#334155", fg="white", bd=0,
              command=take_images_prompt).grid(row=0, column=0, padx=40)

    # Take Attendance
    tk.Button(button_frame, image=verify_img, text="Take Attendance", compound="top",
              font=("Arial", 12), bg="#334155", fg="white", bd=0,
              command=recognize_faces).grid(row=0, column=1, padx=40)

    # View Attendance
    tk.Button(button_frame, image=attendance_img, text="View Attendance", compound="top",
              font=("Arial", 12), bg="#334155", fg="white", bd=0,
              command=view_attendance).grid(row=0, column=2, padx=40)

    # Train Model Button
    tk.Button(window, text="Train Model", font=("Arial", 12), bg="#38bdf8", fg="black",
              command=train_model).pack(pady=(10, 5))

    # Exit Button
    tk.Button(window, text="EXIT", font=("Arial", 12, "bold"),
              bg="#f43f5e", fg="white", width=15,
              command=window.destroy).pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
