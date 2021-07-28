import pyttsx3
import speech_recognition as sr
import wikipedia,webbrowser,os
import datetime
import smtplib

email = {
    'User1':'User1@gmail.com',
    'User2': 'User2@gmail.com',
    'User3': 'User3@gmail.com'
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voice')
engine.setProperty('voice',voices[0])
engine. setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour<12):
        speak("Good Morning Sir")
    elif(hour<=17):
        speak("Good afternoon Sir")
    else:
        speak("Good evening Sir")

    speak("I am Jarvis, How can I help you")

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening now...")
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        #print("Recognizing ... ")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Please say again")
        return ("None")    
    return query

def sendEmail(mailto, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremailaddress@gmail.com','your-password')
    server.sendmail('youremailaddress@gmail.com',mailto,content)
    server.close()


def main():
    speak("Hello")
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching Wikipedia")
        query=query.replace('wikipedia','')
        result=wikipedia.summary(query,sentences=2)
        print(result)
        speak(result)
    elif 'google' in query or 'chrome' in query:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = 'https://google.com/'
        webbrowser.get(chrome_path).open(url) 
    elif 'youtube' in query:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = 'https://youtube.com/'
        webbrowser.get(chrome_path).open(url)
    elif 'time' in query:
        strTime=datetime.datetime.now().strftime("%I:%M")
        if(datetime.datetime.now().hour >12):
            strTime+="PM"
        else:
            strTime+="AM"
        speak(strTime)
    elif 'email' in query:
        if 'rahul' in query:
            mailto=email['rahul'] 
        elif 'papa' in query:
            mailto=email['papa']   
        elif 'mummy' in query:
            mailto=email['mummy'] 
        try:
            speak("What should be the subject")
            subject = takeCommand();
            speak("What should be the message")
            content = takeCommand();

            content = 'Subject: {}\n\n{}'.format(subject, content)
            sendEmail(mailto, content) 
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Please try again")        

if __name__ == "__main__":
    main()







