import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get the current time
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

# Function to get the current date
def get_date():
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

# Function to listen to the user's command and recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {command}")
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""
        return command.lower()

# Main function to run the assistant
def run_jarvis():
    speak("Hello, I am Jarvis. How can I help you today?")
    while True:
        command = listen()
        if "time" in command:
            current_time = get_time()
            speak(f"The current time is {current_time}")
        elif "date" in command:
            current_date = get_date()
            speak(f"Today's date is {current_date}")
        elif "stop" in command or "bye" in command:
            speak("Goodbye!")
            break
        else:
            speak("I can only tell you the time and date for now. Please ask accordingly.")

# Run the assistant
run_jarvis()