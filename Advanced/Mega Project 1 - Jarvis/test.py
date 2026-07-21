import pyttsx3

while True:
    input("Press Enter...")
    engine = pyttsx3.init("sapi5")
    engine.say("Yeah")
    engine.runAndWait()