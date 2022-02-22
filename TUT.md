# MAKING A ASSISTANT


## setting up a method to say something 🔊

we will use pyttsx3 to setup the voice

```shell
pip install pyttsx3
```

```python
import pyttsx3
```

### Step 1 - setting up the voice engine

```python
engine = pyttsx3.init('sapi5') 
```

### Step 2 - get all voices from pyttsx3 and saving them in a variable called voices

```python
voices = engine.getProperty('voices') 

```

### Step 3 - settting up a single voice from the list we got in step 1

```python
engine.setProperty('voices',voices[0].id)
```

### Step 4 - setting speaking rate to 80 wpm

```python
engine.setProperty('rate',170)
```

### Step 5 - create a function called *Say* that takes *text* as a parameter

```python
def Say(text):
```

### Step 6 - writtin the code to speak AND print the text in the function only

```python
    print(f'Assistant: {Text}')
    engine.say(text=Text)#Says the text
    engine.runAndWait()#Waits for code to end
```

### Step 7 - test the voice of the bot -

```python
Say('Hello world!')
```

Good job! you just got a voice in your assistant!!!!!!!

## Setting up a method to listen 👂

### Step 1 - setting up!

we will use speech_recognition to setup the voice

```shell
pip install speechrecognition
```

we will also need pyaudio

```shell
pip install pyaudio
```

Lets import these modules in our code (pyaudio is preimported in the speech recognition module)

```python
import speech_recognition as sr
```

### Step 2 - Lets make a instance of the recognizer called _r_  in a function called _Listen_ !!

```python
def Listen:
	r= sr.Recognizer()
```

### Step 3 - lets use speech recognition and r to use the mic

```python
    with sr.Microphone(0) as source: # Microphone(0) means the deafault mic
        r.pause_threshold = 1 #eliminating last 1 second from audio file recorded
        audio = r.listen(source,0 ,5) # Giving mic as source , then 
        #Timeout as 0 , and time limit as 5
        #(so that our assistant dosent stop listening as soon as he starts to listen....)
```

### Step 4 - send recorded audio to google to change it to a text form, if no text is returned (means user didnt say anything)then return no text , if there is text , we will return it ...

```python
    try:
        # print('recognizing....')
        query = r.recognize_google(audio,language='en-in')
        print(f'you: {query}')
    except Exception as Error:
        return ''
    query = str(query)
    return query.lower()
```

### Step 5 - test the listening method

```python
Say('You said' + Listen())
```

When you run the code you will have to say something (like hello) and the robot will tell you what you said!!( it will only record for 5 seconds , and it wont be very accurate , after all , it is just code , not a real human!!)

## making a brain 🤯🧠

NOTE:in the begining , this brain will be dumb , but soon itll be smart enough to help you do most tasks without touching the keyboard or mouse

### 1- make a function called brain

```python
def Brain():
```

### 2- say a welcome / hello message

```python

Say('All systems are online')
```

### 3 - make a infinite loop

```python
while True:
```

### 4 - listen to the user on each run -

```python
	query = Listen()
```

### 5 - make a if statment looking for a ceartain word ( like hello ) in query

```python
if('hello' in query):

```

### 5.1 - do something when the if statement is true

```python
	Say('hello sir!')
```

### 5.2 - test 

```python
Brain()
```

run the code , say hello and watch the bot say hello back!!!!🤯🤯🤯🤯🤯 

### 6 - add in more AND MORE FEATURES 😎😎😎

(will add more soon!)
