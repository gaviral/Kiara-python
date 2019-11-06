from custom_utilities.os.resources.WindowManager import WindowManager


def get_window_handler(s):
    w = WindowManager()
    w.find_window_wildcard(s)
    return w


def custom_get_window_handler(s):
    w = WindowManager()
    w.custom_find_window_wildcard(s)
    return w


def focus(s, use_custom=False):
    w = custom_get_window_handler(s) if use_custom else get_window_handler(s)
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


def focus_my_browser():
    """
    Bring OS focus on my_browser
    [find_by_window_title("Google") -> bring os focus to it]
    TODO: code to remove this requirement
        POSSIBLE SOLUTION: get process ID of my_browser and use that identifier instead
    """
    focus("Google")
