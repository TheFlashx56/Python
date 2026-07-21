import time
import subprocess
import pyautogui
from clean_messege import parse_chat
# Coordinates
P1 = (478, 219)
P2 = (1342, 684)

print("Starting in 3 seconds...")
time.sleep(3)

# Select the text
pyautogui.moveTo(*P1, duration=0.2)
pyautogui.mouseDown()
pyautogui.moveTo(*P2, duration=0.5)
pyautogui.mouseUp()

time.sleep(0.2)

# Copy
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

# Read clipboard using xclip
try:
    selected_text = subprocess.check_output(
        ["xclip", "-selection", "clipboard", "-o"],
        text=True
    )
except Exception as e:
    print("Clipboard error:", e)
    selected_text = ""

print("Copied Text:")
print(selected_text)
print(f"\nLength: {len(selected_text)}")

cleaned_text=parse_chat(selected_text)


with open("whatsapp.txt", "w", encoding="utf-8") as f:
    for m in cleaned_text:
        f.write(f"[{m['time']}] {m['sender']}: {m['message']}\n\n")