import speech_recognition as  sr

def recognize_speech(language):
    # create a recognizer object
    r = sr.Recognizer()

    # use the default system microphone as the audio source
    with sr.Microphone() as source:
        # adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        print(f"Speak now in {language}...")
        return

        

