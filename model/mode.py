NORMAL = ""

lang_mode: str


def set_lang_mode(s: str) -> None:
    global lang_mode
    lang_mode = s


def get_lang_mode() -> str:
    global lang_mode
    return lang_mode


ON = 1
OFF = 0
talk_mode: str


def set_talk_mode(s: str) -> None:
    global talk_mode
    talk_mode = s


def get_talk_mode() -> str:
    global talk_mode
    return talk_mode

