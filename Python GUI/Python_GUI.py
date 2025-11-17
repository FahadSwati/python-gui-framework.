import os
import threading
import pyautogui
from datetime import datetime
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem as item

INTERVAL_MINUTES = 10
INTERVAL_SECONDS = INTERVAL_MINUTES * 60
SAVE_FOLDER = "screenshots"
os.makedirs(SAVE_FOLDER, exist_ok=True)

def take_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(SAVE_FOLDER, f"screenshot_{timestamp}.png")
    try:
        pyautogui.screenshot().save(filename)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Saved → {filename}")
    except Exception as e:
        print(f"Error: {e}")

stop_event = threading.Event()

def timer_loop():
    while not stop_event.is_set():
        take_screenshot()
        stop_event.wait(INTERVAL_SECONDS)

threading.Thread(target=timer_loop, daemon=True).start()
print(f"Timer STARTED – Every {INTERVAL_MINUTES} minutes")


def create_icon():
    img = Image.new("RGB", (64, 64), "#161b22")
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([10, 18, 54, 46], radius=8, fill="#238636")
    d.ellipse([28, 26, 48, 46], fill="#58a6ff", outline="#1f6feb", width=3)
    d.ellipse([32, 30, 44, 42], fill="white")
    return img

def on_quit(icon, item):
    stop_event.set()
    icon.stop()

menu = (
    item("Open Screenshots", lambda icon, item: os.startfile(os.path.abspath(SAVE_FOLDER))),
    item("Quit", on_quit),
)

global_icon = pystray.Icon("Screenshot Timer", create_icon(), "Screenshot Timer – Running", menu)
global_icon.visible = True   

if __name__ == "__main__":
    print("App started!")
    print(f"Saving to → {os.path.abspath(SAVE_FOLDER)}")
    global_icon.run()   