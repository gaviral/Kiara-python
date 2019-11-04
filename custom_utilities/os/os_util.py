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




def print_all_windows():
    w = WindowManager()
    w.list_all_windows()
