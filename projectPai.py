import pyttsx3
import datetime as dt
import speech_recognition as sr
import pyautogui
import time
import pyjokes
import pywhatkit
import calendar
import wikipedia as wp
import webbrowser as wb
import os

engine =  pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    time = int(dt.datetime.now().hour)

    if time >= 0 and time< 5:
        speak("Hello,Sir.")
    elif time >= 5 and time< 12:
        speak("Good morning,Sir.")
    elif time >= 12 and time< 18:
        speak("Good afternoon, Sir.")
    else:
        speak("Good evening,sir.")
    speak("I'm Pai. How can I help you?")

def listen_to_user():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)
        print("Speak something...")
        r.pause_threshold = 0.9 
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        command = r.recognize_google(audio,language='en')
        print(f"User said: {command}\n")
        
    except Exception as e:     
        print("Say that again please...")        
        return "None"    
    return command

def close_window():
    try: 
        if 'y' in command:
            pyautogui.moveTo(1885,10)
            pyautogui.click()
        else:
            speak('ok')
            pyautogui.moveTo(1000,500)
    except Exception as e:
        speak('opp!error')

if __name__ == "__main__":
    greet()
    said = True
    while said:
        command = listen_to_user().lower()
        if ('go to' in command or 'open' in command) and 'settings' in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('settings')
            pyautogui.press('enter')
        elif ('go to' in command or 'open' in command) and 'gallery' in command or 'photo' in command or 'image' in command or 'pic' in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('photo')
            pyautogui.press('enter')

        elif ('go to' in command or 'open' in command) and 'word' in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('word')
            pyautogui.press('enter')
            time.sleep(8)

        elif ('go to' in command or 'open' in command) and ('power' in command and 'point' in command) or 'presentation' in command or 'ppt' in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('ppt')
            pyautogui.press('enter')
            time.sleep(5)

        elif ('go to' in command or 'open' in command) and 'file' in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('file')
            pyautogui.press('enter')
            time.sleep(2)


        elif ('go to' in command or 'open' in command) and 'edge' in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('microsoft edge')
            pyautogui.press('enter')
            time.sleep(3)

        elif ('go to' in command or 'open' in command) and 'wps' in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('wps office')
            pyautogui.press('enter')
            time.sleep(5)

        elif ('go to' in command or 'open' in command) and 'command'  in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('command promt')
            pyautogui.press('enter')
            time.sleep(3)
        
        elif ('go to' in command or 'open' in command) and 'wechat'  in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('wechat')
            pyautogui.press('enter')
            time.sleep(3)

        elif ('go to' in command or 'open' in command) and 'whats' and 'app' in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('whatsapp')
            pyautogui.press('enter')
            time.sleep(8)
            
        elif ('go to' in command or 'open' in command) and 'photo' and'shop' in command or 'adobe' in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('photoshop')
            pyautogui.press('enter')
            time.sleep(10)
        
        elif ('go to' in command or 'open' in command) and ('ding' in command and 'talk'  in command) or ("dingtalk" in command):
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('dingtalk')
            pyautogui.press('enter')
            time.sleep(3)
            
        elif ('go to' in command or 'open' in command) and 'note' and 'pad' in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('notepad')
            pyautogui.press('enter')
            time.sleep(2)
        elif ('go to' in command or 'open' in command) and ("visual studio" in command) or ("vs code" in command):
            pyautogui.moveTo(250,1200)
            pyautogui.click()
            time.sleep(1)
            pyautogui.write("visual studio code")
            pyautogui.press('enter')
            time.sleep(2)

        elif ('go to' in command or 'open' in command) and "youtube" in command:
            speak("Opening YouTube")
            wb.open("youtube.com")
            time.sleep(5)

        elif ('go to' in command or 'open' in command) and "google" in command:
            speak("Opening Google")
            wb.open("google.com")
            time.sleep(5)

        elif ('go to' in command or 'open' in command) and "facebook" in command:
            speak("Opening Facebook")
            wb.open("facebook.com")
            time.sleep(5)

        elif ('go to' in command or 'open' in command) and 'spread' and 'sheet' in command or 'excel'  in command:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('excel')
            pyautogui.press('enter')
            time.sleep(5)

        elif ('go to' in command or 'open' in command) and ('tencent' in command) or ('voov meeting' in command):
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('Voov Meeting')
            pyautogui.press('enter')
        
        elif 'day before today' in command or 'date before today' in command or 'yesterday' in command or 'previous day' in command:
            ytd = dt.date.today() + dt.timedelta(days= -1)
            print(f"yesterday was,{ytd}")
            speak(f"yesterday was,{ytd}")
        elif ('tomorrow' in command and 'date' in command) or 'what is tomorrow' in command or (('day' in command or 'date' in command) and 'after today' in command):
            td = dt.date.today() + dt.timedelta(days=1)
            print(f"tomorrow is,{td}")
            speak(f"tomorrow is,{td}")
        elif 'month' in command or ('current' in command and 'month' in command):
            current_date = dt.date.today()
            m = current_date.month
            month = calendar.month_name[m]
            print(f'Current month is {month}')
            speak(f'Current month is {month}')

        elif 'date' in command or ('today' in command and 'date' in command) or 'what is today' in command or ('current' in command and 'date' in command):
            current_date = dt.date.today()           
            print(f"Today's date is {current_date}")
            speak(f'Todays date is {current_date}')
            
        elif 'year' in command or ('current' in command and 'year' in command):
            current_date = dt.date.today()
            yr = current_date.year
            print(f'Current year is {yr}')
            speak(f'Current year is {yr}')

        elif 'quit' in command or 'stop' in command or 'exit' in command:
            speak('Ok, Thank you Sir. It was a pleasure to assist you.')
            said = False
        elif "play" in command:
            command = command.replace("play", "")
            speak("Playing "+command)
            pywhatkit.playonyt(command)
            time.sleep(10)

        elif 'close' in command and ('click' in command or 'window' in command):
            pyautogui.moveTo(1885,10)
            speak('Should I close this window?')
            command = listen_to_user().lower()
            close_window()

        elif 'notification' in command and ('show' in command or 'click' in command or 'open' in command or 'close' in command or 'on' in command or 'off' in command or 'icon' in command or 'pc' in command or 'laptop' in command):
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
        elif 'turn' and 'night' in command:
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1840,1000)
            pyautogui.click()
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
        elif 'joke' in command:
            x = pyjokes.get_joke()
            print(x)
            speak(x)

        elif "calculat" in command:
            os.system("calc")
            time.sleep(2)
            
        elif 'screenshot' in command:
            speak('Please go on the screen whose screenshot you want to take, after 5 seconds I will take screenshot')
            time.sleep(4)
            speak('Taking screenshot....3........2.........1.......')
            pyautogui.screenshot('ss_pai.png') 
            speak('The screenshot is saved as ss_pai.png')

        elif ('increase' in command or 'turn up' in command) and ('volume' in command or 'sound' in command):
            pyautogui.press('volumeup')
            print('volume increased') 

        elif ('decrease' in command or 'turn up' in command)and ('volume' in command or 'sound' in command):
            pyautogui.press('volumedown')
            print('volume decreased')

        elif 'capslock' in command or ('caps' in command and 'lock' in command):
            pyautogui.press('capslock')
        elif "thank" in command:
            speak("My pleasure, Sir.")

        elif 'mute' in command:
            pyautogui.press('volumemute')

        elif 'search' in command and ('bar' in command or 'pc' in command or 'laptop' in command or 'app' in command):
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            speak('What do you want to search?')
            command = listen_to_user().lower() 
            pyautogui.write(f'{command}')
            pyautogui.press('enter')

        elif 'google map' in command:
            wb.open('https://www.google.com/maps')
            time.sleep(5)

        elif 'translate' in command or ('let' in command and 'translat' in command and 'open' in command):
            wb.open('https://translate.google.co.in')
            time.sleep(5)

        elif 'weather' in command:            
            wb.open('https://www.weather.com')
            time.sleep(3)
            speak('Click on search city and enter the city name, whose weather conditions you want to know.')
            time.sleep(5)

        elif 'wikipedia' in command:
            print('Searching on Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wp.summary(command, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'information about ' in command or 'informtion of ' in command:
            try:
                print('Searching wikipedia...')
                command = command.replace("information about","")
                results = wp.summary(command, sentences=2)
                print(results)
                speak(results)
            except Exception as e:
                speak('I unable to answer your question.')
        elif 'tell' in command:
            try:
                print('Searching on wikipedia...')
                command = command.replace("tell me about ","")
                results = wp.summary(command, sentences=2)
                print(results)
                speak(results)
            except Exception as e:
                speak('I am unable to answer your question.')
        elif 'who is' in command:
            try:
                print('Searching on wikipedia...')
                command = command.replace("who is ","")
                results = wp.summary(command, sentences=2)
                print(results)
                speak(results)
            except Exception as e:
                speak("opps. I can't find your answer")
        elif 'what is' in command:
            try:
                print('Searching on wikipedia...')
                command = command.replace("what is ","")
                results = wp.summary(command, sentences=2)
                print(results)
                speak(results)
            except Exception as e:
                speak("opps.I can't find your answer")

        elif 'where' in command:
            try:
                url = "https://www.google.co.in/search?q=" +(str(command))+ "&oq="+(str(command))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU" 
                wb.open_new(url)
                time.sleep(2)
            except Exception as e:
                speak('Sorry, I am unable to answer it.')
                print(e)

        elif 'who are you' in command:
            speak("i am pi, an virtual assistant build to make your task easy and faster on your computer")
        else:
            pass     