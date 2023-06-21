import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()


engine = pyttsx3.init()

voices =engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()  
def user_commands(): 
    try:
        with sr.Microphone() as source:
            print("Start Speaking!!") 
            voice= listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()  
            if 'alexa' in commamd :
                command = command.replace('alexa', '')
                print(command)
    except:
            pass 
            return command

def run_alexa():
    command = user_commands()
    if 'play' in command :       
        print(command)
        song = command.replace('play', '')
        #print('New command is '+ song)
        engine_talk('Playing '+ song)
        pywhatkit.playonyt(song) 
    if 'time' in command : 
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is '+ time )
    else :
        engine_talk('I could not hear you properly ') 


run_alexa() 
        
    
