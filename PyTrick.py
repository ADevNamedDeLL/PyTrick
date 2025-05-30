import os
import shutil
import subprocess
import sys
import time

# Windows Startup folder path
STARTUP_FOLDER = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')

# Prank scripts folder containing your prank exe files
PRANKS_FOLDER = 'exe'

# Updated prank scripts with your filenames and descriptions
PRANK_SCRIPTS = [
    ("cricketmadness.exe", "Cricket sound madness"),
    ("fake_odor_alert.exe", "Fake odor alert popup"),
    ("ghostkeys.exe", "Invisible ghost key presses"),
    ("keyboardshort.exe", "Random keyboard shortcuts"),
    ("mousewiggle.exe", "Random mouse wiggle"),
    ("random_zoom.exe", "Screen random zoom in/out"),
    ("screenflicker.exe", "Screen flicker effect"),
    ("speakup.exe", "Random text-to-speech"),
    ("tinyvolumechange.exe", "Tiny volume changes"),
    ("typing_echo.exe", "Typing delay & echo"),
    ("usbghost.exe", "Fake USB disconnect ghost"),
    ("weird_beep.exe", "Weird random beeps"),
]

# ANSI escape codes for colors
class Colors:
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

def print_rainbow(text):
    # Print text cycling through rainbow colors
    rainbow_colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
    for i, ch in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        print(color + ch, end='')
    print(Colors.RESET)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    ascii_art = r"""
 /$$$$$$$         /$$$$$$$$        /$$           /$$      
| $$__  $$       |__  $$__/       |__/          | $$      
| $$  \ $$ /$$   /$$| $$  /$$$$$$  /$$  /$$$$$$$| $$   /$$
| $$$$$$$/| $$  | $$| $$ /$$__  $$| $$ /$$_____/| $$  /$$/
| $$____/ | $$  | $$| $$| $$  \__/| $$| $$      | $$$$$$/ 
| $$      | $$  | $$| $$| $$      | $$| $$      | $$_  $$ 
| $$      |  $$$$$$$| $$| $$      | $$|  $$$$$$$| $$ \  $$
|__/       \____  $$|__/|__/      |__/ \_______/|__/  \__/
           /$$  | $$                                      
          |  $$$$$$/                                      
           \______/                                       
"""
    print_rainbow(ascii_art)

def print_menu():
    print(f"{Colors.MAGENTA}1. Install pranks{Colors.RESET}")
    print(f"{Colors.MAGENTA}2. About{Colors.RESET}")
    print(f"{Colors.MAGENTA}0. Exit{Colors.RESET}")

def print_prank_list():
    print(f"{Colors.MAGENTA}Available prank scripts:{Colors.RESET}\n")
    # Print 2 per row
    for i in range(0, len(PRANK_SCRIPTS), 2):
        line = ""
        for j in range(2):
            idx = i + j
            if idx < len(PRANK_SCRIPTS):
                name, desc = PRANK_SCRIPTS[idx]
                entry = f"{idx+1}. {name[:-4]} : {desc}"
                line += f"{entry:<45}"
        print(line)
    print()
    print(f"{Colors.RED}Note: By installing a small amount of scripts, the prank can last longer.{Colors.RESET}\n")

def install_prank(index):
    script_name, desc = PRANK_SCRIPTS[index]
    source_path = os.path.join(PRANKS_FOLDER, script_name)
    if not os.path.exists(source_path):
        print(f"{Colors.RED}Error: {script_name} not found in '{PRANKS_FOLDER}'.{Colors.RESET}")
        return False
    dest_path = os.path.join(STARTUP_FOLDER, script_name)
    try:
        print(f"{Colors.YELLOW}Installing {script_name}...{Colors.RESET}")
        shutil.copy2(source_path, dest_path)
        time.sleep(0.5)  # Wait a bit for file system to catch up
        subprocess.Popen([dest_path], cwd=STARTUP_FOLDER)  # run without shell
        print(f"{Colors.GREEN}Installed and started {script_name} successfully.{Colors.RESET}")
        return True
    except Exception as e:
        print(f"{Colors.RED}Failed to install {script_name}: {e}{Colors.RESET}")
        return False

def main():
    clear_screen()
    print_header()

    while True:
        print_menu()
        choice = input(f"{Colors.WHITE}Choose an option: {Colors.RESET}").strip()

        if choice == '1':
            clear_screen()
            print_header()
            print_prank_list()
            selection = input(f"{Colors.WHITE}Enter prank script numbers to install (comma-separated): {Colors.RESET}").strip()
            selections = [s.strip() for s in selection.split(',') if s.strip().isdigit()]
            if not selections:
                print(f"{Colors.RED}No valid selection made.{Colors.RESET}")
                continue
            clear_screen()
            print_header()
            print(f"{Colors.MAGENTA}Installing selected prank scripts...{Colors.RESET}\n")
            for sel in selections:
                idx = int(sel) - 1
                if 0 <= idx < len(PRANK_SCRIPTS):
                    install_prank(idx)
                    time.sleep(1)
                else:
                    print(f"{Colors.RED}Invalid selection: {sel}{Colors.RESET}")
            print(f"\n{Colors.GREEN}Installation complete. Prank scripts added to Startup.{Colors.RESET}")
            input(f"{Colors.WHITE}Press Enter to return to menu...{Colors.RESET}")
            clear_screen()
            print_header()

        elif choice == '2':
            clear_screen()
            print_header()
            print(f"{Colors.MAGENTA}PyTrick - Prank Script Installer{Colors.RESET}")
            print("Created by DeLL's assistant.")
            print("Installs compiled prank scripts as startup executables.\n")
            input(f"{Colors.WHITE}Press Enter to return to menu...{Colors.RESET}")
            clear_screen()
            print_header()

        elif choice == '0':
            print(f"{Colors.GREEN}Goodbye!{Colors.RESET}")
            sys.exit()

        else:
            print(f"{Colors.RED}Invalid option. Try again.{Colors.RESET}")

if __name__ == "__main__":
    main()
