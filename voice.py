import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    """Function to convert text to speech"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to capture voice input from the user"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Request error from Google Speech Recognition service.")
        speak("Request error from the speech recognition service.")
        return None

def respond_to_command(command):
    """Function to respond to specific commands"""
    if command is None:
        return

    if "hello" in command:
        response = "Hello! How can I help you today?"
        print(response)
        speak(response)

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {current_time}"
        print(response)
        speak(response)

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        response = f"Today's date is {current_date}"
        print(response)
        speak(response)

    elif "search for" in command:
        query = command.replace("search for", "").strip()
        url = f"https://www.google.com/search?q={query}"
        response = f"Searching the web for {query}"
        print(response)
        speak(response)
        webbrowser.open(url)

    else:
        response = "I'm not sure how to respond to that."
        print(response)
        speak(response)

if __name__ == "__main__":
    speak("Voice Assistant is ready.")
    while True:
        user_command = listen()
        if user_command:
            if "exit" in user_command or "quit" in user_command:
                speak("Goodbye!")
                break
            respond_to_command(user_command)
