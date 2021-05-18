import json
from difflib import get_close_matches
import pyttsx3
#import speech_recognition as sr

data = json.load(open("C:\\Users\\K555L\\Downloads\\python reqs\\original\\data.json"))
print("\t\t\t\t DICTIONARY")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
      engine.say(audio)
      engine.runAndWait()
      
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        speak("Did you mean %s instead?  yes or no: " % get_close_matches(w, data.keys())[0])
        yn = input("Did you mean %s instead?  yes or no: " % get_close_matches(w, data.keys())[0])
        if yn.lower() == "y" or yn.lower()=="yes" or yn.lower()=="s":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower() == "n" or yn.lower()=="no" or yn.lower()=="nah":
            return "Sorry , The word doesn't exist. Please double check it."
        else:
            return "I didn't understand your entry."
    else:
        return "Sorry , The word doesn't exist. Please double check it."
end=False
while end==False:
    speak("What do you wish to search for? : ")
    word = input("What do you wish to search for? : ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
            speak(item)
    else:
        print(output)
        speak(output)
    speak("Do you wish to search for another word  ?  yes or no : ")
    end=input("Do you wish to search for another word  ? yes or no : ")
    if end.lower()=="y" or end.lower()=="yes" or end.lower()=="s":
        print("Great!!!")
        speak("Great!!!")
        end=False
    elif end.lower()=="n" or end.lower()=="no":
        print("Thank you for using the dictionary , Bye !")
        speak("Thank you for using the dictionary , Bye !")
        end=True
    else:
        end=True
