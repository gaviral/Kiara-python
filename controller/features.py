import sys

from pyautogui import hotkey, press
from pyperclip import paste, copy

from features.google_speech_search import google_speech_search
from features.text_to_speech import say

SEARCH_HOTWORDS = {'search', 'versus', 'difference', 'when', 'why', 'how', 'Which', 'what', 'who', 'where', 'whether',
                   'is',
                   'does', 'do'}

attempt = 0


def search_ctrlr(_first_word):
    if _first_word == "search":
        try:
            google_speech_search()
        except:
            e = sys.exc_info()[0]
            say(e)


TYPE_HOTWORDS = {'type', 'add'}


def type_ctrlr(_first_word, _sentence):
    if _first_word in TYPE_HOTWORDS:
        copy(_sentence)
        paste()


def keyboard_cmd_ctrlr(_first_word, _words, _sentence):
    if "new file" in _sentence:
        hotkey('ctrl', 'n')
    elif "save" in _sentence:
        hotkey('ctrl', 's')
    elif "reload" in _sentence:
        hotkey('ctrl', 'f5')
    elif _first_word == "code":
        # TODO: move this code to open in my_browser
        hotkey('ctrl', 't')
        copy(f'https://leetcode.com/problemset/all/?search={_words[1]}')
        hotkey('ctrl', 'l')
        hotkey('ctrl', 'v')
        press('enter')

    elif _first_word == "line":
        # code-editor: go to line __
        # TODO: Refactor out
        # TODO: only when in vscode/intelliJ
        copy(f'{_words[1]}')
        hotkey('ctrl', 'g')
        hotkey('ctrl', 'v')
        press('enter')

        # custom script
    elif "script" in _sentence:
        for i in range(6, 13):
            for j in range(0,10):
                press('up')
                press('f2')
                press('left')
                press('del')
                press('del')
                press(f'{i}')
                press('enter')

        # press('enter')
    elif _first_word == "commit":
        # Last open projects
        # Get the last working project window
        # (Think if a confirmation logic is needed)
        # Commit command in the apt project directory
        pass

        pass


def features_controller(sentence, words):
    search_ctrlr(words[0])
    type_ctrlr(words[0], sentence)
    keyboard_cmd_ctrlr(words[0], words, sentence)
