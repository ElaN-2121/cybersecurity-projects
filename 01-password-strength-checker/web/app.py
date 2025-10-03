import tkinter as tk
from tkinter import messagebox
from password_checker import overall_strength

def on_check():
    pw=entry.get()
    result=overall_strength(pw)
    messagebox.showinfo("Result",f"Password Strength: {result}")

root=tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter Password: ").pack(pady=5)
entry= tk.Entry(root, show="*") #hides password input:)
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=on_check).pack(pady=10)

root.mainloop()
