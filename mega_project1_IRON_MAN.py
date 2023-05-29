import datetime
import pyttsx3
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[1].id)
engine.setProperty('voices', voices[0 ].id);pa = "abcd"
def speak(audio):
    print('JARVIS : ', audio)
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning Sir !")
    elif (hour >= 12 and hour < 17):
        speak("Good Afternoon Sir !")
    elif (hour >=17 and hour < 19):
        speak('Good Evening Sir !')
    else:
        speak("Good Night Sir !")

    speak("I Am JARVIS ! Just Rather A Very Intelligent System. ")
    speak("I am created by Arpan Nath...Currently Working As My Master's Artificial Intelligence System And His Good Friend ")

def working():
    speak('I am just a Baby and i have a lot to learn in the coming days')
    speak('just for now , i can automate the following thing !')
    speak('To open the google only if you sentence contain "open google"')
    speak('To open the youtube only if you sentence contain "open youtube"')
    speak('To open the stackoverflow only if you sentence contain "open stackoverflow"')
    speak('To play music only if you sentence contain "play music"')
    speak('To say the exact time only if your sentence contain "time"')
    speak('To to search and speak everything in wikipedia only if you sentence contain "wikipedia"')
    speak('i know this is not much...but i promise to learn more')


def security():
    # speak('Your Name Sir ?')
    # n = takecommand()
    speak('Please ! Say The Passcode To Activate Me !')
    p = takecommand()
    # p = input("Here : ")
    if p.lower() == pa:
        speak('Welcome Sir ! To the World Of Technology !')
        working()
        speak("How May I help U ??")
    else:
        speak("Sorry ! But Currently You Don't Have The Authorization ")
        speak("Good Bye ! Sir")
        exit()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listning ...')
        r.pause_threshold = 1
        # r.energy_threshold=100
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print('recognishing...')
        query = r.recognize_google(audio, language="en-in")
        print(f'User : {query}')
    except:
        speak('Sorry ! I am Still Developing Myself')
        speak("Please Say That Again ")
        return 'None'
    return query
if __name__ == '__main__':
    wishme()
    security()

    query = takecommand().lower()
    if 1:
        if "wikipedia" in query:
            speak('Searcing Wikipidea...')
            query = query.replace('wikipidea', " ")
            results = wikipedia.summary(query, sentences=2)
            speak('Acording To Wikipidea ')
            # print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('Opening Youtube In Microsoft Edge')
            webbrowser.open('youtube.com')
        elif 'open stackoverflow' in query:
            speak('Opening StackOverflow In microsoft Edge')
            webbrowser.open('stackoverflow.com')
        elif 'open google' in query:
            speak('Opening Google In Microsoft Egde')
            webbrowser.open('google.com')
        elif 'play music' in query:
            speak('Playing Music')
            music_dir = "C:\\Study\\Musics"
            songs = os.listdir(music_dir)
            rand = random.randint(1, 10)
            os.startfile(os.path.join(music_dir, songs[rand]))
        elif 'time' in query:
            t = datetime.datetime.now().strftime("%H hours %M minutes %S seconds.")
            speak(f'Now, The Time is :{t}')
        elif 'quit' in query:
            speak('Thank U sir ! For Using Me ! Sorry if I had Bored You ! See You Next Time')
            speak('You Are Now Exiting The Tech World')
            speak('Bye Bye ')
            exit()
        else:
            speak('Sorry ! I cant Understand You ! I am Still Developing !')
