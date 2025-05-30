import os
import time
import psutil

class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

def print_logo():
    rainbow = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    logo_lines = [
        r"    /$$$$$$$         /$$$$$$$$        /$$           /$$      ",
        r"  | $$__  $$       |__  $$__/       |__/          | $$      ",
        r"  | $$  \ $$ /$$   /$$| $$  /$$$$$$  /$$  /$$$$$$$| $$   /$$",
        r"  | $$$$$$$/| $$  | $$| $$ /$$__  $$| $$ /$$_____/| $$  /$$/",
        r"  | $$____/ | $$  | $$| $$| $$  \__/| $$| $$      | $$$$$$/    Uninstaller",
        r"  | $$      | $$  | $$| $$| $$      | $$| $$      | $$_  $$ ",
        r"  | $$      |  $$$$$$$| $$| $$      | $$|  $$$$$$$| $$ \  $$",
        r"  |__/       \____  $$|__/|__/      |__/ \_______/|__/  \__/",
        r"             /$$  | $$                                      ",
        r"            |  $$$$$$/                                      ",
        r"             \______/                                       "
    ]
    for i, line in enumerate(logo_lines):
        print(rainbow[i % len(rainbow)] + line + Colors.RESET)


# ========== Config ==========
PRANK_NAMES = [
    "cricketmadness.exe", "fake_odor_alert.exe", "ghostkeys.exe", "keyboardshort.exe",
    "mousewiggle.exe", "random_zoom.exe", "screenflicker.exe", "speakup.exe",
    "tinyvolumechange.exe", "typing_echo.exe", "usbghost.exe", "weird_beep.exe"
]

STARTUP_FOLDER = os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup")

# ========== Kill Process ==========
def kill_process_by_name(name):
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and proc.info['name'].lower() == name.lower():
                proc.kill()
                print(f"{Colors.YELLOW}Killed {name}{Colors.RESET}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

# ========== Uninstall ==========
def uninstall_all():
    print(f"{Colors.MAGENTA}\n[Uninstalling PyTrick Pranks]\n{Colors.RESET}")
    time.sleep(0.3)
    found = False

    for prank in PRANK_NAMES:
        path = os.path.join(STARTUP_FOLDER, prank)
        if os.path.exists(path):
            found = True
            try:
                print(f"{Colors.YELLOW}Removing {prank}...{Colors.RESET}")
                kill_process_by_name(prank)
                os.remove(path)
                print(f"{Colors.GREEN}Uninstalled {prank}{Colors.RESET}")
                time.sleep(0.1)
            except Exception as e:
                print(f"{Colors.RED}Failed to remove {prank}: {e}{Colors.RESET}")

    if not found:
        print(f"{Colors.RED}No prank executables found in Startup folder.{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}\nAll selected pranks removed successfully!{Colors.RESET}")

if __name__ == "__main__":
    os.system("color")  # Enable ANSI colors in Windows
    print_logo()
    uninstall_all()
    input(f"\n{Colors.WHITE}Press Enter to exit...{Colors.RESET}")
