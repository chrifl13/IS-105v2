import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 100)

voices = engine.getProperty('voices')
print len(voices)
for voice in voices:
    print "Using voice:", repr(voice)
    engine.setProperty('voice', voice.id)
    engine.say("Bla bla bla ?")
    engine.say("A B C D E F G H I J K L M")
    engine.say("N O P Q R S T U V W X Y Z")
    engine.say("0 1 2 3 4 5 6 7 8 9")
    engine.say("")
    engine.say("Sunday Monday Tuesday Wednesday Thursday Friday Saturday")
    engine.say("Violet Indigo Blue Green Yellow Orange Red")
    engine.say("Apple Banana Cherry Date Guava")
engine.runAndWait()