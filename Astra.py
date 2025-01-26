''' 
Name: "SAM", "SR", "ASTRA" , "ARIS" "JARVIS".

To run without any sys_log 

python3 Aris.py 2>/dev/null     ## For Linux (Ubantu)
python jarvis.py 2>$null        ## For Windows (10,11)
python3 Aris.py 2>/dev/null     ## For Mac (os)

Email app passowrd for jarvis:
**** YOUR - PASSWORD ****

'''

# ------------------------------------------------ #

# Imporing Librarys

import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import sys
import smtplib

import ctypes

try:
    # Suppress ALSA warnings
    asound = ctypes.CDLL('libasound.so')
    asound.snd_lib_error_set_handler(None)
except Exception:
    pass

# ------------------------------------------------ #

# CODE START

# Initialize pyttsx3 with 'espeak' for Ubuntu
engine = pyttsx3.init('espeak')

# Get and set voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[24].id)  # Set voice (adjust index as needed)
engine.setProperty('rate', 126)           # Set speech rate
engine.setProperty('volume', 1.0)         # Set volume (max: 1.0)

# ------------------------------------------------------ #

# Define the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# ------------------------------------------------------- # 

# Wish Me function
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning SR")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon SR")
    else:
        speak("Good Evening SR")
    speak("Hi, I am Astra. How can I assist you today ?")

# ------------------------------------------------------- #


# Function to get the current time
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

# Function to get the current date
def get_date():
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

# ------------------------------------------------------------ #


# Taking Command function
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=2) # Adjust for ambient noise
        r.pause_threshold = 0.5  # Reduce pause threshold
        audio = r.listen(source)

    try:
        print("Processing your voice input...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, could you repeat that, please?")
        return "None"
    return query

# ---------------------------------------------------------------- #

# Function to sent E-mail

def send_mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('windows.to.linux.01@gmail.com','Your - Password')
    server.sendmail('windows.to.linux.01@gmail.com', to, content)
    server.close()

# ---------------------------------------------------------------- #


# Function to close a specific application

def close_app(app_name):
    try:
        os.system(f"killall {app_name}")  # Close the specific app
        speak(f"{app_name} has been closed.")
    except Exception as e:
        speak(f"Sorry, I could not close {app_name}.")
        print(e)

# ---------------------------------------------------------------- #


# Main execution
if __name__ == "__main__":
    wishme()

    while True:
        query = takecommand().lower()

        # Logic for executing tasks

        if 'wikipedia' in query:
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "tell about you" in query:
            speak("I'm, Astra made by S.R an"
            "A.I. assistant called Aris or Sam.")

        elif "time" in query:
            current_time = get_time()
            speak(f"The current time is {current_time}")

        elif "date" in query:
            current_date = get_date()
            speak(f"Today's date is {current_date}")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com/")

        elif 'close google' in query:
            speak("Closing Google")
            close_app("google")
 
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com/")


        # -------------------------------------------------------------- #
        # elif 'close youtube' in query:                                 #
        #     speak("Closing YouTube")                                   #
        #     close_app("YouTube")                                       #
                
        # elif 'open github' in query:                                   #
        #     speak("Opening GitHub")                                    #
        #     webbrowser.open("https://github.com/sameerraj-13")         #

        # elif 'close github' in query:                                  #    
        #     speak("Closing GitHub")                                    #
        #     close_app("GitHub")                                        # 
        # -------------------------------------------------------------- #


        elif 'open my website' in query:
            speak("Opening your website")
            webbrowser.open("https://sameerraj-13.github.io/Exhibition-Website/")

        elif 'open mail' in query:
            speak("Opening Mail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        # elif 'close mail' in query:
        #     speak("Closing Mail")
        #     webbrowser.close("https://mail.google.com/mail/u/0/#inbox")

        elif 'open gpt' in query:
            speak("Opening GPT")
            webbrowser.open("https://chatgpt.com/")

        # elif 'close gpt' in query:
        #     speak("Closing GPT")
        #     webbrowser.close("https://chatgpt.com/")

        elif 'open calculator' in query:
            speak("Opening Calculator")
            webbrowser.open("https://sameerraj-13.github.io/Calculator/")

        
        # elif 'close calculator' in query:
        #     speak("Closing Calculator")
        #     webbrowser.close("https://sameerraj-13.github.io/Calculator/")


    # ---------------------------------------------------------------------- #


     # Opeing application from system using 'OS' module or library

        elif 'open code' in query:
            speak("Opening VS Code")
            codepath = os.popen("which code").read().strip()
            if codepath:
                os.system(codepath)
            else:
                speak("VS Code is not installed or not added to your PATH.")

        elif 'close code' in query:
                speak("Closing VS code")
                close_app("code")

    # ---------------------------------------------------------------------- #

        # To Send E - Mail

        elif 'send email' in query:
            try:
                speak("What is your message?")
                content = takecommand()
                to = "sameerraj552155@gmail.com" 
                send_mail(to, content)
                speak("Email has been sent successfully, SR!")
            except Exception as e:
                print(e)
                speak("Oops! Email could not be sent. Please try again.")

        elif "stop" in query or "bye" in query:
            speak("Goodbye, SR Have a great day!")
            sys.exit()
          # break 

                 # both excepted as well as sys.exit()

     # ---------------------------------------------------------------- #

        else:
            speak("Sorry, I didn't understand that. Please say again.")

     # ---------------------------------------------------------------- #


# CODE ENDED



