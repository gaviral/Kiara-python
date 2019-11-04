import re

import win32gui


class WindowManager:
    """Encapsulates some calls to the winapi for window management
    source: https://stackoverflow.com/questions/2090464/python-window-activation
    credits: luc (https://stackoverflow.com/users/117092/luc)
    """

    def __init__(self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _custom_window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None and win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), win32gui.GetWindowText(hwnd))

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            # print(f'hwnd: {hwnd}')
            self._handle = hwnd

    def _custom_focus_window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if wildcard in str(win32gui.GetWindowText(hwnd)):
            print(f'hwnd: {hwnd}')
            self._handle = hwnd

    def list_all_windows(self):
        """list_all_windows"""
        self._handle = None
        win32gui.EnumWindows(self._custom_window_enum_callback, "kiara")

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def custom_find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._custom_focus_window_enum_callback, wildcard)


    def get_foreground_window(self):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())

    def get_foreground_window_class(self):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        return win32gui.GetClassName(win32gui.GetForegroundWindow())

    def set_foreground(self):
        """put the window in the foreground"""
        if self._handle is not None:
            win32gui.SetForegroundWindow(self._handle)
