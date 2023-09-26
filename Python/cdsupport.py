import datetime
import speech_recognition as sr

recognizer = sr.Recognizer()

    # Open the microphone and start recording
with sr.Microphone() as source:
    print("Listening...")

    try:
            # Adjust for ambient noise and listen for speech
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5)
            print("Audio recorded successfully. Recognizing...")

            # Use Google Web Speech API for recognition
            recognized_text = recognizer.recognize_google(audio)
            print("You said: " + recognized_text)

    except sr.WaitTimeoutError:
            print("No speech detected")
    except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))
    except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
rt=recognized_text
if rt=="five star " or rt=="5 star ":
   r=5
elif rt=="four star " or rt=="4 star ":
   r=4
elif rt=="three star " or rt=="3 star ":
   r=3
elif rt=="two star " or rt=="2 star " :
   r=2
elif rt=="one star " or rt=="1 star " :
   r=1
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime('%Y-%m-%d#%H.%M.%S')
file_content="HEllo is this working\nHardik"
if(r=="1"):
   file_path="1 star/"+formatted_datetime+".txt"
elif(r=="2"):
   file_path="2 star/"+formatted_datetime+".txt"
elif(r=="3"):
   file_path="3 star/"+formatted_datetime+".txt"
elif(r=="4"):
   file_path="4 star/"+formatted_datetime+".txt"
elif(r=="5"):
   file_path="5 star/"+formatted_datetime+".txt"
with open(file_path, 'w') as file:
    file.write(file_content)
