import cv2
import mediapipe as mp
import pyautogui
import pygetwindow as gw
import time
import threading
import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
import psutil


def set_window_always_on_top(window_name):
    while True:
        try:
            window = gw.getWindowsWithTitle(window_name)[0]
            window.activate()
            window.alwaysOnTop = True
            break
        except IndexError:
            time.sleep(0.1)


def show_error_message(message):
    error_window = Toplevel(root)
    error_window.title("Error")
    error_label = tk.Label(error_window, text=message, fg="red", font=("Helvetica", 12))
    error_label.pack(pady=10, padx=10)
    ok_button = tk.Button(error_window, text="OK", command=error_window.destroy, font=("Helvetica", 12, "bold"), padx=10, pady=5)
    ok_button.pack(pady=10)
    error_window.transient(root)
    error_window.grab_set()
    root.wait_window(error_window)



root.mainloop()
