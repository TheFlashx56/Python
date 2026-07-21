import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary 





engine = pyttsx3.init()
# Initialize
r = sr.Recognizer()
def speak(text): 
    engine.say(text) 
    engine.runAndWait()
  
speak('Initializing Jarvis')

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "code " in c.lower():
        song=c.lower()
        link = musiclibrary.music[song]
        webbrowser.open(link)
    else:
        speak("Command Not Detected.")
while True:
    print("Recognizing....")
    try:
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
        print(word)
        if "jarvis" in word.lower():
            print("Wake word detected")
            speak("Ya")
            with sr.Microphone() as source:
                print("Jarvis is Active....")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                
                processCommand(command)
                
    except Exception as e:
       print("Error {0}",format(e)) 