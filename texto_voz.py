import pyttsx3
def texto_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    engine.stop()