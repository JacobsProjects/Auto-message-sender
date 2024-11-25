import time
from datetime import datetime
import pyautogui
import colorama
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
    message = input(Fore.MAGENTA + "What message do you want to type? ")
    target_time = input(Fore.MAGENTA + "What time should I send it? (HH:MM 24hr format): ")
    return message, target_time

def is_time_to_send(target_time):
    current_time = datetime.now().strftime("%H:%M")
    if datetime.now().second % 5 == 0:
        print(Fore.MAGENTA + f"Waiting... Current time: {current_time}, Target time: {target_time}")
    return current_time == target_time
    
def send_message(message):
    print(Fore.MAGENTA + "\nTime matched! Starting to type message...")
    pyautogui.write(message, interval=0.1)
    pyautogui.keyDown('enter')
    print(Fore.MAGENTA + "Message sent! Press enter to close this!")

def main():
    message, target_time = get_message_details()
    print(Fore.MAGENTA + f"\nYour message '{message}' will send at {target_time}")
    print(Fore.MAGENTA + "Keep this window open and get ready to switch to your target window...")
    
    while True:
        if is_time_to_send(target_time):
            send_message(message)
            input()
            break
        time.sleep(1)  

if __name__ == "__main__":
    main()