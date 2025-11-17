# Screenshot Automation Tool  
**Auto Screenshot Every 10 Minutes | Windows System Tray App**

### What This App Does
Automatically takes a **full-screen screenshot every 10 minutes** and saves it with a clear timestamp.  
Runs silently in the background with a **tiny green camera icon** in the Windows system tray (taskbar).  
No pop-ups, no visible window — completely clean and professional.

---

### Features
- Takes screenshot every **10 minutes** (exact timing)  
- Saves in `screenshots/` folder with format:  
  `screenshot_2025-11-17_21-30-00.png`  
- green camera icon in system tray 
  
  

---

### Tech Stack (Only 4 Packages)
| Package      | Purpose                          |
|--------------|----------------------------------|
| `pyautogui`  | Captures the screen              |
| `Pillow`     | Saves images                     |
| `pystray`    | Shows permanent tray icon        |
| `threading`  | Runs timer in background         |

---

