import time
from datetime import datetime
import pyautogui
import colorama
import psutil
import win32gui
import win32con
from colorama import Fore

colorama.init()

def get_message_details():
    print(rf"""{colorama.Fore.MAGENTA}
                                                            
    _         _                           _
   / \  _   _| |_ ___  ___  ___ _ __   __|  _ __ ___   ___ ___ ___  __ _  __ _  ___
  / _ \| | | | __/ _ \/ __|/ _ | '_ \ / _` | '_ ` _ \ / _ / __/ __|/ _` |/ _` |/ _ \
 / ___ | |_| | || (_) \__ |  __| | | | (_| | | | | | |  __\__ \__ | (_| | (_| |  __/
/_/   \_\__,_|\__\___/|___/\___|_| |_|\__,_|_| |_| |_|\___|___|___/\__,_|\__, |\___|
                                                                         |___/
                                                                    coded by jagob
     """)
    app_to_focus = input(Fore.MAGENTA + "What application do you want to focus, (leave blank if none)? e.g Discord.exe> ")
    message = input(Fore.MAGENTA + "What message do you want to type?> ")
    target_time = input(Fore.MAGENTA + "What time should I send it? (HH:MM 24hr format)> ")
    return app_to_focus, message, target_time

def find_window_handle(window_title):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and window_title.lower() in win32gui.GetWindowText(hwnd).lower():
            hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds[0] if hwnds else None

def focus_app(app_to_focus):
    if not app_to_focus:
        return True
    
    app_running = False
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == app_to_focus.lower():
            app_running = True
            break
    
    if not app_running:
        print(Fore.RED + f"Error: {app_to_focus} is not running!")
        return False
    
    window_title = app_to_focus.replace('.exe', '')
    
    try:
        hwnd = find_window_handle(window_title)
        if hwnd:
            if win32gui.IsIconic(hwnd):
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            
            win32gui.SetForegroundWindow(hwnd)
            return True
        else:
            print(Fore.RED + f"Error: Could not find window for {app_to_focus}")
            return False
    except Exception as e:
        print(Fore.RED + f"Error focusing window: {str(e)}")
        return False

def is_time_to_send(target_time):
    current_time = datetime.now().strftime("%H:%M")
    if datetime.now().second % 5 == 0:
        print(Fore.MAGENTA + f"Waiting... Current time: {current_time}, Target time: {target_time}")
    return current_time == target_time

def send_message(message):
    print(Fore.MAGENTA + "\nTime matched! Starting to type message...")
    pyautogui.write(message, interval=0.1)
    pyautogui.press('enter')
    print(Fore.MAGENTA + "Message sent! Press enter to close this!")

def main():
    app_to_focus, message, target_time = get_message_details()
    print(Fore.MAGENTA + f"\nYour message '{message}' will send at {target_time}")
    print(Fore.MAGENTA + "Keep this window open...")
    
    message_sent = False
    while True:
        if is_time_to_send(target_time) and not message_sent:
            if focus_app(app_to_focus):
                time.sleep(0.5)  
                send_message(message)
                message_sent = True
            else:
                print(Fore.RED + "Failed to focus application. Please try again.")
                break
        
        if message_sent:
            input()  
            break
            
        time.sleep(1)

if __name__ == "__main__":
    main()