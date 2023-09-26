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
