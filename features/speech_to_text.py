import speech_recognition as sr

WAIT_UNTIL_BOOL_ANSWER = None


def get_text_from_speech(_timeout=0.5):
    text = ''
    r = sr.Recognizer()
    with sr.Microphone() as audio_source:

        try:
            audio = r.listen(audio_source, timeout=_timeout)
            text = r.recognize_google(audio)
            print(f'Avi : {text}')
        except sr.WaitTimeoutError:
            # print('DEBUG: speechrecognition.WaitTimeoutError')
            pass
        except sr.UnknownValueError:
            # print('DEBUG: speechrecognition.UnknownValueError')
            pass

    return text


def str_to_bool_char(_str):
    return "n" if "no" in _str else "y"


def get_voice_input(bool_answer=False):
    _s = get_text_from_speech(_timeout=WAIT_UNTIL_BOOL_ANSWER)
    _s = str_to_bool_char(_s) if bool_answer else _s
    return _s
