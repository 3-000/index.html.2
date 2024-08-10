import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            speak("Sorry, my speech service is down.")
            return None

# Simple ethical decision-making framework
def ethical_decision_making(command):
    if "help" in command:
        return "Helping others is usually a good ethical choice. How can I assist?"
    elif "harm" in command or "hurt" in command:
        return "It is important to avoid causing harm. Consider a different approach."
    elif "privacy" in command:
        return "Respecting privacy is crucial. Ensure you have consent before proceeding."
    elif "fair" in command or "unfair" in command:
        return "Fairness is important. Make sure everyone is treated equally."
    else:
        return "I'm not sure about this decision. Please consider the ethical implications."

# Main function
def main():
    speak("Hello, I am your ethical decision-making assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            response = ethical_decision_making(command)
            print(response)
            speak(response)
        if command == "exit" or command == "quit":
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
