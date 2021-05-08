import pyttsx3
sent = input("What to speak??---->")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
# V = input("Type something----->")
if __name__ == "__main__":
    speak(sent)
    # speak(V)