# Astra AI Assistant

### `Astra (AI Personal Assistant)`

Astra (Commonly called named `SAM, SR, ARIS, or JARVIS`) is a voice-controlled AI personal assistant designed to perform various tasks like opening/closing applications, fetching information, telling the date and time, sending emails, and more. This assistant can be enhanced with additional features in the future.

---

## **Features**

### **General Commands**
- **Greetings and Assistance:** Astra greets the user based on the time of the day and offers assistance.
- **Time and Date:** Provides the current time and date on request.
- **Wikipedia Search:** Searches Wikipedia and reads a summary.

### **Web Commands**
- **Open Websites:** Opens common websites like Google, YouTube, Gmail, GitHub, etc.
- **Close Websites:** Closes specific websites (future functionality).
- **Access Personal Projects:** Opens personal GitHub repositories and project links.

### **System Commands**
- **Open Applications:** Launches local applications like VS Code using the OS module.
- **Close Applications:** Terminates running applications with the `killall` command.

### **Email Functionality**
- Sends emails through Gmail using SMTP. Requires app password authentication.

### **Error Handling**
- Suppresses warnings (e.g., ALSA library warnings).
- Handles unrecognized voice input gracefully.

### **Future Enhancements**
- Advanced AI-based natural language processing.
- Integration with additional APIs (e.g., calendar, weather, or stock market APIs).
- Improved support for closing web pages and adding more dynamic web interactions.
- Cross-platform compatibility and packaged executables for easier deployment.

---

## **How to Run**

### **Dependencies**
Install the required libraries using pip:
```bash
pip install pyttsx3 SpeechRecognition wikipedia smtplib
```

### **Run the Program**
To run Astra, execute the following commands based on your operating system:

#### **Linux (Ubuntu):**
```bash
python3 Aris.py 2>/dev/null
```

#### **Windows (10/11):**
```bash
python jarvis.py 2>$null
```

#### **macOS:**
```bash
python3 Aris.py 2>/dev/null
```

---

## **Code Overview**

### **Key Sections**
- **Initialization:** Sets up pyttsx3 for voice output and ALSA warning suppression.
- **Functions:**
  - `speak(audio)`: Converts text to speech.
  - `wishme()`: Greets the user based on the time of the day.
  - `get_time()`: Returns the current time.
  - `get_date()`: Returns the current date.
  - `takecommand()`: Captures and processes user voice input.
  - `send_mail(to, content)`: Sends emails via SMTP.
  - `close_app(app_name)`: Closes a running application.
- **Main Logic:** Continuously listens for user commands and executes the corresponding functionality.

### **Highlights**
- Modular design with clear separation of logic into functions.
- Dynamic and customizable settings (e.g., voice, speed, volume).

---

## **Customizable Parameters**
- **Voice Settings:** Modify `engine.setProperty()` to adjust voice index, speed, and volume.
- **Email Settings:** Replace `Your - Password` with your Gmail app password.
- **Application Commands:** Add new commands for opening/closing apps in the `if-elif` structure.

---

## **Contributing**
If you’d like to contribute, feel free to:
- Add new features or optimize the code.
- Report issues or suggest enhancements via the GitHub issues page.

---

## **License**
This project is open-source and licensed under the MIT License.

---

## **GitHub Profile**

- **GitHub:** [Profile] [https://github.com/sameerraj-13]

---

> _This assistant is a work in progress, and new features will be added regularly._

--- 

```
Thank You!
Team,
```
`SR`


