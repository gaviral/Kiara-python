import speech_recognition as sr

WAIT_UNTIL_BOOL_ANSWER = None


def get_text_from_speech(_ptl=3):
    text = ''
    r = sr.Recognizer()
    with sr.Microphone() as audio_source:
        audio = r.listen(audio_source, phrase_time_limit=_ptl)

        try:
            text = r.recognize_google(audio)
            print(f'Avi : {text}')
        except sr.UnknownValueError:
            print('DEBUG: speechrecognition.UnknownValueError')
            pass

    return text


def str_to_bool_char(_str):
    return "n" if "no" in _str else "y"


def get_voice_input(bool_answer=False):
    _s = get_text_from_speech(_ptl=WAIT_UNTIL_BOOL_ANSWER)
    _s = str_to_bool_char(_s) if bool_answer else _s
    return _s
