import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...Speak now")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=10)
            command = recognizer.recognize_google(audio).lower()
            print(f"you said: {command}")
            return command
        except sr.WaitTimeoutError:
            print("No speech detected. try again.")
            return ""
        
def run_assistant():
    command = listen()

    if "play" in command:
        song = command.replace("play","").strip()
        speak(f"Playing {song} on Youtube")
        pywhatkit.playonyt(song)

    elif "play" in command:
        current_time = datetime.datetime.now().strftime("%I:%M:P")
        speak(f"The current time is {current_time}")
    elif "exit" in command or "stop" in command:
        speak("GoodBye! Have a great day")
        exit()

    else:
        speak("I did not understand. Please Try again.")

while True:
    run_assistant()