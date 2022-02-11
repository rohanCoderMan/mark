import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import pyautogui
import os
import pyjokes
from PyDictionary import PyDictionary as dicti
import datetime
from playsound import playsound as ps


# os.startfile('.\\Mark.bat')
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',170)

def Say(Text):
    print("     ")
    print(f'Mark X: {Text}')
    engine.say(text=Text)#Says the text
    engine.runAndWait()#Waits for code to end
    print("     ")

def Listen():
    # print('listening....')
    r= sr.Recognizer()
    with sr.Microphone(0) as source: # Microphone(0) means the deafault mic
        r.pause_threshold = 1
        audio = r.listen(source,0 ,5) # Giving mic as source , then 
        #Timeout as 0 , and time limit as 5
        #(so that mark dosent stop listening as soon as he starts to listen....)

    try:
        # print('recognizing....')
        query = r.recognize_google(audio,language='en-in')
        print(f'you: {query}')
    except Exception as Error:
        return ''
    query = str(query)
    return query.lower()

def MainTasks():
    Say('Mark is online!!')
    def Music():
        Say("what is the name of the music")
        musicName = Listen()
        Say(f'Playing {musicName} on youtube')
        pywhatkit.playonyt(musicName)
    def OpenApps(query):
        Say('ok sir...')
        query = query.replace("mark","")
        query = query.replace("open","")
        pyautogui.hotkey('ctrl', 'esc')
        pyautogui.write(query, interval = 0.2)
        pyautogui.hotkey('enter')
    def ChromeAuto():
        # pyautogui.hotkey('')
        Say('Started chrome automation')
        while True:
            comm = Listen()
            if('new window' in comm):
                pyautogui.hotkey('ctrl','n')
            elif('new tab' in comm):
                pyautogui.hotkey('ctrl','t')
            elif('reopen' in comm):
                pyautogui.hotkey('ctrl','shift','t')
            elif('devloper' in comm):
                pyautogui.hotkey('ctrl','shift','i')
            elif('full screen' in comm):
                pyautogui.press('f11')
            elif('close' in comm):
                pyautogui.hotkey('ctrl','w')
            elif('exit' in comm):
                Say('closing chrome automation')
                break
    def YoutubeAuto():
        # pyautogui.hotkey('')
        Say('Started youtube automation')
        while True:
            comm = Listen()
            if('play' in comm or 'pause' in comm):
                pyautogui.press('k')
            elif('mute' in comm or 'unmute' in comm):
                pyautogui.press('m')
            elif('fullscreen' in comm):
                pyautogui.press('f11')
            elif('exit' in comm):
                Say('closing youtube automation')
                break

    while True:
        query = Listen()
        if("sleep" in query):
            Say("Okay sir....")
            Say('Just say Wake up to wake me up')
            Say('Mark is offline')
            break
        elif("hello" in query):
            Say("Hello sir!")
        elif('youtube search' in query):
            Say("Ok sir...")
            query = query.replace("mark","")
            query = query.replace("youtube","")
            query = query.replace("search","")
            Say(f"searching for{query}")
            url = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(url)
        elif('google search' in query):
            Say("Ok sir...")
            query = query.replace("mark","")
            query = query.replace("google","")
            query = query.replace("search","")
            Say(f"searching for{query}")
            pywhatkit.search(query)
        elif('website' in query):
            Say("Ok sir launching...")
            query = query.replace("mark","")
            query = query.replace("website","")
            query = query.replace("open","")
            query = query.replace("of","")
            web = f"https://www.{query}.com"
            webbrowser.open(web)
        elif('music' in query):
            Music()
        elif('wikipedia' in query):
            Say("Ok sir...")
            query = query.replace("mark","")
            query = query.replace("search","")
            query = query.replace("on","")
            query = query.replace("wikipedia","")
            query = query.replace("who is","")
            query = query.replace("about","")
            wiki = wikipedia.summary(query,2)
            Say(f'according to wikipidea:{wiki}')
        elif ('screenshot' in query):
            pyautogui.hotkey('win','down')
            pyautogui.hotkey('win','shift','s')
        elif('open' in query):
            OpenApps(query)  
        elif('chrome automation' in query or 'chrome tools'in query):
            ChromeAuto()
        elif('youtube automation' in query or 'youtube tools'in query):
            YoutubeAuto()
        elif('joke' in query):
            get = pyjokes.get_joke()
            Say(get)
        elif('hello' in query):
            Say('hello sir!')
        elif('where am i'in query):
            webbrowser.open('https://www.google.com/maps/')
        elif('meaning' in query):
            query = query.replace('what','')
            query = query.replace('is','')
            query = query.replace('the','')
            query = query.replace('meaning','')
            query = query.replace('of','')

            result = dicti.meaning(query)

            Say(f'the meaning of {query} is {result}')
        elif('synonym' in query):
            query = query.replace('what','')
            query = query.replace('is','')
            query = query.replace('the','')
            query = query.replace('synonym','')
            query = query.replace('of','')

            result = dicti.synonym(query)
            Say(f'the synonym of {query} is {result}')
        elif('antonym' in query):
            query = query.replace('what','')
            query = query.replace('is','')
            query = query.replace('the','')
            query = query.replace('antonym','')
            query = query.replace('of','')

            result = dicti.synonym(query)
            Say(f'the antonym of {query} is {result}')
        elif('alarm' in query):
            Say('enter the time (IN 24 hour)')
            time = input('enter the time: ')

            while True:
                timeAc = datetime.datetime.now()
                now = timeAc.strftime("%H:%M:%S")

                if now == time:
                    Say("alarm opening")
                    ps(".\\ringtone.mp3")
                elif now>time:
                    break
        elif('new window' in query):
                pyautogui.hotkey('ctrl','n')
        elif('new tab' in query):
                pyautogui.hotkey('ctrl','t')
        elif('reopen' in query):
                pyautogui.hotkey('ctrl','shift','t')
        elif('devloper' in query):
                pyautogui.hotkey('ctrl','shift','i')
        elif('full screen' in query):
                pyautogui.press('f11')
        elif('close' in query):
                pyautogui.hotkey('ctrl','w')
        elif('play' in query or 'pause' in query):
                pyautogui.press('k')
        elif('mute' in query or 'unmute' in query):
                pyautogui.press('m')
MainTasks()
