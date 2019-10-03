import os

import playsound
import speech_recognition as sr
from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

ON = 1
OFF = 0
talk_mode = ON

NO_LANG = ""
PYTHON = "python"
REACT = "react"
lang_mode = NO_LANG

SEARCH_WORDS = ['search', 'when', 'why', 'how', 'Which', 'what', 'whose', 'who', 'where', 'whether', 'is', 'does', 'do']

SUCCESS = 0
UNRECOGNIZED_COMMAND_ERROR = -1

SEARCH_TAB_URL = "https://www.google.com/search?q="
NEW = 2

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
TEST_FILE = f"{os.getcwd()}\\__test_arena\\interviewPrep\\ik\\Trees\\dft.py"



def get_text():
    r = sr.Recognizer()
    text = ''
    with sr.Microphone() as audio_source:
        audio = r.listen(audio_source, phrase_time_limit=3)

        try:
            text = r.recognize_google(audio)
            print(f'Avi : {text}')
        except sr.UnknownValueError:
            # print('DEBUG: speechrecognition.UnknownValueError')
            pass

    return text


###############


def play_mp3(mp3_file):
    playsound.playsound(mp3_file, True)


#############


def create_mp3(words, file):
    gTTS(text=words, lang='en', slow=False).save(file)


def remove_mp3(file):
    os.remove(file)


###########

def say(words, file='tts.mp3'):
    print(f'Kiara: {words}')
    create_mp3(words, file)
    play_mp3(file)
    remove_mp3(file)


###########

chrome_handler: WebDriver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')


def handle_command(mode, cmd_str):
    global lang_mode

    words = cmd_str.split(' ', 1)

    first_word = words[0]
    rest_words = words[1:][0] if len(words) > 1 else None

    if first_word in SEARCH_WORDS:
        extracted_s_text = rest_words if first_word == "search" else cmd_str
        search_text = f'{lang_mode} {extracted_s_text}'
        search_url = f'{SEARCH_TAB_URL} {search_text}'
        chrome_handler.get(search_url)
        print(f'searched: {search_text}')

    elif "mode" in cmd_str:
        if "python" in cmd_str:
            lang_mode = PYTHON
        elif "react" in cmd_str:
            lang_mode = REACT
        elif "no" in cmd_str or "normal" in cmd_str:
            lang_mode = NO_LANG
        print(f'Language Mode: {lang_mode}')
    else:
        print(f'Sorry, I don\'t understand this command: {cmd_str}')
        # say(f'Sorry, I don\'t understand this command: {words}')
        return UNRECOGNIZED_COMMAND_ERROR
    return SUCCESS


def handle_talk_mode(mode, words):
    stop_talking_commands = ['stop talking', 'pause']
    start_talking_commands = ['start talking', 'you can talk now', 'play']

    if words in stop_talking_commands:
        say("ok! I'll stop talking")
        return OFF

    elif words in start_talking_commands:
        say("Alright, I'll talk now")
        return ON

    else:
        ret_code = handle_command(mode, words)

        if ret_code == -1:
            # do something
            pass

    return mode


if __name__ == '__main__':

    say('Hey let\'s go!')

    while True:
        text = get_text()
        stop_listening_commands = ['stop listening', 'bye']

        if text == '':
            continue

        if text in stop_listening_commands:
            say('okay then! Bye.')
            break

        # print(f'\nDEBUG: talk_mode={talk_mode}')
        if talk_mode == ON:
            # say(text)  # echo back those words
            pass

        talk_mode = handle_talk_mode(talk_mode, text)
