import sys

from pyautogui import hotkey, press
from pyperclip import copy

from custom_utilities.os.os_util import focus_my_browser, focus, print_all_windows, open_git_extensions
from features.google_speech_search import google_speech_search, my_browser, GOOGLE_URL
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


# TYPE_HOTWORDS = {'type', 'add'}
#
#
# def type_ctrlr(_first_word, _sentence):
#     if _first_word in TYPE_HOTWORDS:
#         copy(_sentence)
#         paste()


def keyboard_cmd_ctrlr(_first_word, _words, _sentence):
    # TODO: make context aware
    if "new file" in _sentence:
        hotkey('ctrl', 'n')

    elif "save" in _sentence:
        hotkey('ctrl', 's')

    elif "reload" == _first_word:
        # TODO: bring forward IDE
        # TODO: bringForwardIDE()
        # until then assumption is: last focus is on IDE
        my_browser.get(GOOGLE_URL)
        focus_my_browser()
        hotkey('alt', 'f4')
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

    elif _words[0] == "find" and _words[1] == "all":
        hotkey('ctrl', 'shift', 'f')
        copy(f'{" ".join(_words[2:])}')
        hotkey('ctrl', "v")

    elif _first_word == "find":
        hotkey('ctrl', 'f')
        copy(f'{" ".join(_words[1:])}')
        hotkey('ctrl', "v")

    elif _first_word == "type":
        copy(f'{" ".join(_words[1:])}')
        hotkey('ctrl', 'v')

    elif 'all' in _words and 'windows' in _words:
        print_all_windows()

    # code mode#######################
    elif _first_word == "press":
        key = _words[1] if len(_words) > 1 else ""
        copy(f'press(\'{key}\')')
        hotkey('ctrl', 'v')

    elif _first_word == "alt" or _first_word == "ctrl" or _first_word == "control":
        if _first_word == "control":
            _first_word = "ctrl"
        copy(f'hotkey(\'{_first_word}\',\'{_words[1]}\')\n')
        hotkey('ctrl', 'v')

    elif ("get" in _words or "git" in _words) and "extensions" in _words:
        if "charm" in _words or "pycharm" in _words:
            open_git_extensions("PyCharm")
        elif "storm" in _words or "webstorm" in _words:
            open_git_extensions("PyCharm")
        else:
            open_git_extensions()
    # end of code mode#######################

    # elif _first_word == "commit":
    #     # decide which open project
    #     # open gitextensions
    #     commandLine = openCommandLine(project_path)
    #     commandLine.run("GitExtensions .")
    #
    #     if editor is VS_CODE:
    #         hotkey('ctrl', 'v')
    #     elif editor is INTELLIJ:
    #         hotkey('alt', 'f12')
    #
    #     pass

    # custom script
    elif "testing" == _first_word:
        focus("GoalNav")
        # open_git_extensions()
        pass


def features_controller(sentence, words):
    search_ctrlr(words[0])
    # type_ctrlr(words[0], sentence)
    keyboard_cmd_ctrlr(words[0], words, sentence)
