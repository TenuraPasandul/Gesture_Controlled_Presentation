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
def show_success_message(message):
    success_window = Toplevel(root)
    success_window.title("Success")
    success_label = tk.Label(success_window, text=message, fg="green", font=("Helvetica", 12))
    success_label.pack(pady=10, padx=10)
    ok_button = tk.Button(success_window, text="OK", command=success_window.destroy, font=("Helvetica", 12, "bold"), padx=10, pady=5)
    ok_button.pack(pady=10)
    success_window.transient(root)
    success_window.grab_set()
    root.wait_window(success_window)


def start_virtual_mouse():

    is_powerpoint_running = False
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() in ['powerpnt.exe', 'powerpoint', 'powerpnt']:
            is_powerpoint_running = True
            break

    if not is_powerpoint_running:
        show_error_message("Running program is not PowerPoint application")
        return

    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils

    window_name = 'Hand Gesture Controlling'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 600, 450)

    screen_width, screen_height = pyautogui.size()
    frame_width, frame_height = 600, 450
    cv2.moveWindow(window_name, 0, screen_height - frame_height)

    boundary_line_y = 300

    thread = threading.Thread(target=set_window_always_on_top, args=(window_name,))
    thread.start()



root.mainloop()
