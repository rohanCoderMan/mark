import os
import speech_recognition as sr

def Listen():


    r= sr.Recognizer()
    with sr.Microphone(0) as source: # Microphone(0) means the deafault mic
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source,0 ,2) # Giving mic as source , then 
        #Timeout as 0 , and time limit as 2 
        #(so that mark dosent stop listening as soon as he starts to listen....)

    try:
        print("recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f'you: {query}')
    except Exception as Error:
        return ''
    query = str(query)
    return query.lower()
while True:
    wake_Up = Listen()

    if 'wake up' in wake_Up:
        os.startfile('.\\Mark.py')
    else:
        print('sleeping....')