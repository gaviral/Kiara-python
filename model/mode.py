NORMAL = ""

lang_mode: str


def set_lang_mode(s: str) -> None:
    global lang_mode
    lang_mode = s


def get_lang_mode() -> str:
    global lang_mode
    return lang_mode


####################################
ON = True
OFF = False

talk_mode: str


def set_talk_mode(s: str) -> None:
    global talk_mode
    talk_mode = s


def get_talk_mode():
    global talk_mode
    return talk_mode


####################################
feeling_lucky_mode: bool


def get_feeling_lucky_mode():
    global feeling_lucky_mode
    return feeling_lucky_mode


def set_feeling_lucky_mode(_bool):
    global feeling_lucky_mode
    feeling_lucky_mode = _bool
