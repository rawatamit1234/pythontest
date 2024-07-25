import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Can you please repeat?")
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
    
    return None

# Function to interact based on voice commands
def run_jarvis():
    speak("Hello! I'm Amit Singh rawat. How can I help you today?")

    while True:
        query = listen()

        if query:
            if 'hello' in query:
                speak("Hello! How are you?")
            elif 'your name' in query:
                speak("My name is Jarvis.")
            elif 'goodbye' in query:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I can't do that yet.")

if __name__ == "__main__":
    run_jarvis()
