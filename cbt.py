import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
inputline=input("Enter the text:")
rate=engine.getProperty('rate')
engine.setProperty('rate',rate - 50)
engine.say(inputline)
engine.runAndWait()