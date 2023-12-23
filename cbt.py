import pyttsx3
def voice(inp):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate - 50)
    engine.say(inp)
    engine.runAndWait()