# Importerer biblotek som brukes for språk gjennkjenning.

import speech_recognition as sr
import pyttsx

# Her startes pyttsx med en pyttsx.init(), denne modulen (pyttsx), lager ord utifra tekst.

engine = pyttsx.init()
engine.setProperty('rate', 70)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # Her brukes "google recognition" til å gjennkjenne ord
            value = r.recognize_google(audio)

            # Her trengs en operasjon for å printe unicode bokstaver til standard output
            if str is bytes: # Denne versionen av python bruker bytes istedenfor strings (python 2)
                print(u"You said {}".format(value).encode("utf-8"))
                engine.say('How are you today?')
                engine.runAndWait()
            else: # Denne versonen av Python bruker unicode istedenfor strings (Python 3)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    
except KeyboardInterrupt:
    pass