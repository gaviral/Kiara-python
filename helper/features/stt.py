import speech_recognition as sr


def stt():
    text = ''
    r = sr.Recognizer()
    with sr.Microphone() as audio_source:
        audio = r.listen(audio_source, phrase_time_limit=3)

        try:
            text = r.recognize_google(audio)
            print(f'Avi : {text}')
        except sr.UnknownValueError:
            print('DEBUG: speechrecognition.UnknownValueError')
            pass

    return text