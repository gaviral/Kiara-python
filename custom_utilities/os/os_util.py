from custom_utilities.os.resources.WindowManager import WindowManager


def focus_my_browser():
    """
    Bring OS focus on my_browser
    [find_by_window_title("Google") -> bring os focus to it]
    TODO: code to remove this requirement
        POSSIBLE SOLUTION: get process ID of my_browser and use that identifier instead
    """
    w = WindowManager()
    w.find_window_wildcard("Google")
    w.set_foreground()
