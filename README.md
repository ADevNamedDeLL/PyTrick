# 🎭 PyTrick ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

**PyTrick** is a stealthy collection of Windows prank scripts designed to surprise users with subtle, random mischief. From ghost keystrokes to flickering screens and fake alerts, it's the ultimate prank toolkit for developers with a sense of humor.

---

## ✨ Features

- 👻 Ghost typing and mouse movement
- 🧨 Random screen zoom, flicker, and volume changes
- 🔊 TTS-based speech and random beeps
- 🔌 Fake USB alerts and system notifications
- 🧠 Randomized intervals (5–180 minutes)
- 🚫 Auto startup support and easy uninstaller
- 🔒 Fully stealthy: runs without visible console
- 🧰 Easy to build and deploy

---

## 📥 Install (from Release)

1. Go to the [Releases](https://github.com/ADevNamedDeLL/PyTrick/releases/tag/main_) page.
2. Download desired prank `.exe` files or the uninstaller:
   - `cricketmadness.exe`, `ghostkeys.exe`, etc.
3. Move prank executables to the Windows Startup folder:
4. Restart your PC to activate the prank.

✔️ Pranks run silently on startup with random delays.

---

## 🏗️ Build From Source

### 1. Clone the repository
```bash
git clone https://github.com/YourUsername/PyTrick.git
cd PyTrick
```
### 2. Clone the repository
Install dependencies
``` bash
pip install -r requirements.txt
```
### 3. Build executables
Use PyInstaller to generate a stealthy `.exe` 
``` bash
pyinstaller --noconsole --onefile script_name.py
```
Replace script_name.py with any prank script or the PyTrick_uninstaller.py.

The output .exe will be in the dist/ directory.

---
## 🔧 Uninstalling Pranks

Run the generated `PyTrick_uninstaller.exe`:

- Scans for known prank executables
- Kills active prank processes
- Removes prank files from Startup

---

## 🧪 Included Pranks

- `cricketmadness.exe` — Annoying sound loops
- `ghostkeys.exe` — Random fake keystrokes
- `mousewiggle.exe` — Slight mouse movements
- `typing_echo.exe` — Echoes typed characters
- `screenflicker.exe` — Brief screen flashes
- `random_zoom.exe` — Zooms screen briefly
- `speakup.exe` — Random TTS messages
- `weird_beep.exe` — Beeping sounds
- `usbghost.exe` — Fake USB connect/disconnect popups
- `fake_odor_alert.exe` — Ridiculous alert boxes
- ...and more!

Each prank is modular and can be built/used independently.

---

## ⚠️ Disclaimer

PyTrick is intended for **educational and entertainment** purposes only.

## 💡 Author

**A Dev Named DeLL**  
