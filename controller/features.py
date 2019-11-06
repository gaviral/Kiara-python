import inspect
import sys
from time import sleep

from pyautogui import hotkey, press
from pyperclip import copy

from custom_utilities.os.os_util import print_all_windows, get_foreground_window, focus_my_browser, \
    get_foreground_window_class, focus
from features.google_speech_search import google_speech_search, my_browser, GOOGLE_URL, open_ik
from features.text_to_speech import say


# region Helper Functions

# @formatter:off
def new_file(): ctrl('n')
def paste(): ctrl('v')
# @formatter:on

# @formatter:off
def enter(): press('enter')
def space(): press('space')
def ctrl(x): hotkey('ctrl', x)
def alt(x): hotkey('alt', x)
def win(x): hotkey('win', x)
# @formatter:on

# endregion


def search_cmd_ctrlr(_first_word):
    if _first_word == 'search':
        try:
            google_speech_search()
        except:
            e = sys.exc_info()[0]
            say(e)


def print_fail(cause):
    print(
        f"""
        FAILED: {inspect.stack()[1].function}
        Cause: {cause}
        STACK: {inspect.stack()}
        """
    )


JET_BRAINS_IDES = {'PyCharm', 'webstorm'}
JET_BRAINS_IDE_CLASS_NAMES = {'SunAwtFrame'}
MICROSOFT_IDES = {'code'}
MICROSOFT_IDE_CLASS_NAMES = {
    'Chrome_WidgetWin_1'}  # careful 'Chrome_WidgetWin_1' is the class for both vscode & Google Chrome
SUPPORTED_IDES_OR_PROJECTS = JET_BRAINS_IDES.union(JET_BRAINS_IDE_CLASS_NAMES, MICROSOFT_IDE_CLASS_NAMES,
                                                   MICROSOFT_IDES, ['GoalNav'])


def open_git_extensions(project_or_ide=None, ide_class=None, show_error=True):
    ide_class, project_or_ide = get_project_ide_or_class(ide_class, project_or_ide)

    if project_or_ide not in SUPPORTED_IDES_OR_PROJECTS and show_error is False:
        print(f'Opened Git Extensions from {project_or_ide}')
        return

    if project_or_ide in JET_BRAINS_IDES or ide_class in JET_BRAINS_IDE_CLASS_NAMES:
        hotkey('alt', 'f12')
    elif project_or_ide in MICROSOFT_IDES or ide_class in MICROSOFT_IDE_CLASS_NAMES:
        hotkey('ctrl', 'shift', '`')

    sleep(1)

    insert_text('GitExtensions')
    enter()
    hotkey('alt', 'f12')
    sleep(1)
    # focus('- Git ')
    focus('- Git ', use_custom=True)


def find_all(_words):
    hotkey('ctrl', 'shift', 'f')
    insert_text(f'{" ".join(_words[2:])}')  # improve by using sentence
    enter()


def find(_words):
    ctrl('f')
    if len(_words) > 1:
        insert_text(f'{" ".join(_words[1:])}')  # improve by using sentence
        enter()


def go_to_line(w2):
    ctrl('g')
    insert_text(f'{w2}')
    enter()


def search_leetcode(w2):
    ctrl('t')
    ctrl('l')
    insert_text(f'https://leetcode.com/problemset/all/?search={w2}')
    enter()


def reload_kiara():
    focus('PyCharm')
    my_browser.get(GOOGLE_URL)
    focus_my_browser()
    hotkey('alt', 'f4')
    ctrl('f5')


def save_file():
    ctrl('s')


def open_website(url):
    my_browser.get(url)


def insert_text(type_txt):
    copy(type_txt)
    paste()


def features_controller(sentence, words):
    search_cmd_ctrlr(words[0])
    # type_ctrlr(words[0], sentence)
    keyboard_cmd_ctrlr(words[0], words, sentence)


def get_project_ide_or_class(ide_class, project_or_ide):
    if project_or_ide is None:
        project_or_ide = get_foreground_window()
    if ide_class is None:
        ide_class = get_foreground_window_class()
    if len(project_or_ide.split(" ")) > 1:
        project_or_ide = project_or_ide.split(" ")[-1]
    return ide_class, project_or_ide


def open_commit_window():
    if 'Git' not in get_foreground_window().split(" "):
        print_fail(cause=f'Not in GitExtensions window')

    ctrl('space')


def press_commit_button():
    if 'Git' not in get_foreground_window().split(" "):
        print_fail(cause=f'Not in GitExtensions\'s commit window')

    hotkey('alt', 'c')


def commit():
    press_commit_button()
    open_git_extensions(show_error=False)
    sleep(2)
    open_commit_window()


def change_playback_vlc(faster):
    press('f')
    alt('l')
    press('e')
    press('f' if faster else 'w')
    press('f')


def keyboard_cmd_ctrlr(_first_word, _words, _sentence):
    # @formatter:off
    def is_text_in(x, y): return x in y
    def is_text(x, y): return x == y
    def in_s(x): return is_text_in(x, _sentence)                            # check _sentence
    def in_w(x): return is_text_in(x, _words)                               # check _words
    def w1(x): return is_text(x, _first_word)                               # check first word
    def w2(x): return is_text(x, _words[1]) if len(_words) > 1 else False   # check second word (if it exists)
    # @formatter:on

    if in_s('new file'):
        new_file()

    elif w1('reload'):
        reload_kiara()

    elif w1('line'):
        go_to_line(w2)

    elif w1('find'):
        find(_words)

    elif w1('find') and w2('all'):
        find_all(_words)

    elif w1('type') or w1('dictate') or (w1('start') and (w2('typing') or w2('dictating'))):
        insert_text(f'{" ".join(_words[1:])}') if w1('type') else win('h')

    elif w1('code'):
        search_leetcode(w2)

    elif w1('open') and w2('ik'):
        open_ik()

    # region code commands
    elif w1("press"):
        key = _words[1] if len(_words) > 1 else ""
        insert_text(f'press(\'{key}\')')

    elif w1('alt') or w1('ctrl') or w1("control"):
        _first_word = "ctrl" if w1("control") else _first_word  # todo: implement correction dictionary
        key1, key2 = _words[0].split('-', 2) if '-' in _first_word else _words[0], _words[1]
        insert_text(f'hotkey(\'{key1}\', \'{key2}\')\n')

    elif w1("sleep"):
        # todo: implement correction dictionary
        seconds = '1' if w2('one') else '2' if w2('to') else _words if len(_words) > 1 else ""
        insert_text(f'sleep({seconds})')

    elif w1("first") and w2("word"):
        # TODO: check if in kiara and a IDE
        insert_text(f"""elif w1(\'{" ".join(_words[2:])}\'):\n\t""") if len(_words) > 2 else None

    elif "if" in _words and "in" in _words and "words" in _words:
        insert_text(f'elif in_w(\'{_words[1]}\'):\n\t')
    # endregion

    # region GitExtensions commands
    elif (in_w("get") or in_w("git")) and in_w("extensions"):
        if in_w("charm") or in_w("pycharm"):
            open_git_extensions("PyCharm")
        elif in_w("storm") or in_w("webstorm"):
            open_git_extensions("webstorm")
        else:
            open_git_extensions()

    elif w1('commit') or ((w1('git') or w1('get')) and w2('commit')):
        commit()
    # endregion

    # YouTube commands
    elif w1('play') or w1('pause'):
        space()
    # endregion

    elif w1('history'):
        ctrl('h')

    # region vlc commands
    elif w1('fast') or w1('faster'):
        change_playback_vlc(faster=True)

    elif w1('slow') or w1('slower'):
        change_playback_vlc(faster=False)
    # endregion

    elif 'all' in _words and 'windows' in _words:
        print_all_windows()

    # region custom script
    elif "testing" == _first_word:
        pass
    # endregion

# todo:
#  1. write regression tests
#  2. write conditions for:
#       save_file()
#  3. could replace w1/w2 and so on with regex
#  4. commands
#       git:
#           push
#       popcorn-time
#       shutdown


# SEARCH_HOTWORDS = {'search', 'versus', 'difference', 'when', 'why', 'how', 'Which', 'what', 'who', 'where', 'whether',
#                    'is',
#                    'does', 'do'}

# TYPE_HOTWORDS = {'type', 'add'}
#

#
# def type_ctrlr(_first_word, _sentence):
#     if _first_word in TYPE_HOTWORDS:
#         copy(_sentence)
#         paste()
