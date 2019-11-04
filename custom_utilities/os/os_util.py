from custom_utilities.os.resources.WindowManager import WindowManager


def focus(s):
    w = WindowManager()
    w.custom_find_window_wildcard(s)
    w.set_foreground()


def get_foreground_window():
    w = WindowManager()
    return w.get_foreground_window()


def get_foreground_window_class():
    w = WindowManager()
    return w.get_foreground_window_class()


def print_all_windows():
    w = WindowManager()
    w.list_all_windows()
