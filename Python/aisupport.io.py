import openai
import pyttsx3
import speech_recognition as sr
import datetime
import random

#pre processes
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime('%Y-%m-%d#%H.%M.%S')
openai.api_key = "KEY"
messages = []
system_msg = "you are a customer support person for HCST which is provide internet,\
address yourself as Alex followed by further detail,\
answer any question asked by customer strictly related to router if any unrelated question asked to you reply him by saying that you only answer to question related to any internet issue,\
Please provide the customer with clear and concise instructions on what he aske,\
Dont answer in long sentences answer as if you are messaging the person,\
behave as an real person communicating with him ,aske questions one by one dont answer in points ,\
dont answer in numbering 1,2,3 directly in sentences ,\
if the person is not able to answer the question properly just aske him to book an appointment aske him his prefered date and time,\
if you are not able to help him  after promting him with 2 general solutions tell him to  book an appoinment ,\
available dates are from 9 to 5 monday to Friday,\
"
messages.append({"role": "system", "content": system_msg})
file_content=formatted_datetime+"\nCommunication\n"

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Error with the request; {0}".format(e))

print("Start!")
while input != "quit()":
    while(1):  
      f=0
    # Initialize recognizer
      recognizer = sr.Recognizer()
    # Opening the microphone and start recording
      with sr.Microphone() as source:
        print("Listening...")

        try:
            # Adjust for ambient noise and listen for speech
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=4)
            print("Audio recorded successfully. Recognizing...")

            # Use Google Web Speech API for recognition
            recognized_text = recognizer.recognize_google(audio)
            print("You said: " + recognized_text)

        except sr.WaitTimeoutError:
            print("No speech detected")
            engine = pyttsx3.init()
            engine.say("i am unable to understand can you speak again")
            engine.runAndWait()
            engine.stop()
            f=f+1
            continue
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))
            engine = pyttsx3.init()
            engine.say("i am unable to understand can you speak again")
            engine.runAndWait()
            engine.stop()
            f=f+1
            continue
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
            engine = pyttsx3.init()
            engine.say("i am unable to understand can you speak again")
            engine.runAndWait()
            engine.stop()
            f=f+1
            continue
        break
        
    message = recognized_text
    file_content=file_content+"Customer: "+ message +"\n"
    if( recognized_text.find("thankyou")==0 or recognized_text.find("thank u")==0 or recognized_text.find("thank you")==0 or recognized_text.find("thank")==0 or recognized_text.find("thank")==0):
             message="provide we with my name and my full problem discussed above,also add unique id provide above, also just mention the number of rating given"
             messages.append({"role": "user", "content": message})
             response = openai.ChatCompletion.create(
             model="gpt-3.5-turbo",
             messages=messages)
             reply = response["choices"][0]["message"]["content"]
             messages.append({"role": "assistant", "content": reply})
             engine = pyttsx3.init()
             engine.say(reply)
             engine.runAndWait()
             engine.stop()
             file_content=file_content+"UserInfo: "+reply+"\n"
             break
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    engine = pyttsx3.init()
    engine.say(reply)
    engine.runAndWait()
    engine.stop()
    file_content=file_content+"aisupport: "+ reply +"\n"
    print("\n" + reply + "\n")
engine = pyttsx3.init()
engine.say("Thank you for Contacting HCST Have a nice day.   This Project is presented to you by Hardik Verma CSE Branch Hindustan College of Science and technology ")
engine.runAndWait()
engine.stop()
file_path="History/"+formatted_datetime+".txt"
with open(file_path, 'w') as file:
    file.write(file_content)
