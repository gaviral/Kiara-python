from pyautogui import hotkey, press
from pyperclip import copy

from custom_utilities.os.resources.WindowManager import WindowManager


def focus(s):
    w = WindowManager()
    w.custom_find_window_wildcard(s)
    w.set_foreground()


def focus_my_browser():
    """
    Bring OS focus on my_browser
    [find_by_window_title("Google") -> bring os focus to it]
    TODO: code to remove this requirement
        POSSIBLE SOLUTION: get process ID of my_browser and use that identifier instead
    """
    focus("Google")


def get_foreground_window():
    w = WindowManager()
    return w.get_foreground_window()


def get_foreground_window_class():
    w = WindowManager()
    return w.get_foreground_window_class()


JET_BRAINS_IDES_OR_CLASS_NAMES = {'PyCharm', 'SunAwtFrame'}
MICROSOFT_IDES_OR_CLASS_NAMES = {'code'}
SUPPORTED_IDES_OR_PROJECTS = JET_BRAINS_IDES_OR_CLASS_NAMES.union(MICROSOFT_IDES_OR_CLASS_NAMES).union(['GoalNav'])


def open_git_extensions(project_or_ide=None):
    if project_or_ide is None:
        project_or_ide = get_foreground_window()

    print(project_or_ide)
    if len(project_or_ide.split(" ")) > 1:
        project_or_ide = project_or_ide.split(" ")[-1]

    if project_or_ide not in SUPPORTED_IDES_OR_PROJECTS:
        print(f'{project_or_ide} is not a supported IDE')
        return

    if project_or_ide in JET_BRAINS_IDES_OR_CLASS_NAMES:
        hotkey('alt', 'f12')
    elif project_or_ide in MICROSOFT_IDES_OR_CLASS_NAMES:
        hotkey('ctrl', 'shift', '`')

    copy('GitExtensions')
    hotkey('ctrl', 'v')
    press('enter')


def print_all_windows():
    w = WindowManager()
    w.list_all_windows()
