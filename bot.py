from time import sleep
import pyautogui
from textblob import TextBlob
from parser_yandex_music import YandexMusicParser

# add your Yandex mail, password and full link to your VK music page
YANDEX_MAIL = "*@yandex.com"
PASSWORD = "*"
VK_MUSIC_LINK = "https://vk.com/audios240917398"

CHROME_ICON = (215, 1055)
CHROME_URL = (410, 70)
SEARCH = (901, 406)
ADD_TRACK = (1462, 525)
SWITCH_LANGUAGE_step1 = (1732, 1059)
SWITCH_LANGUAGE_RUS = (1817, 834)
SWITCH_LANGUAGE_ENG = (1835, 919)

# used to determine the location of the cursor
screenWidth, screenHeight = pyautogui.size()
x, y = pyautogui.position()
print(x, y)

def open_browser():
    print("Opening Google Chrome browser")
    pyautogui.click(CHROME_ICON)
    sleep(1)

def add_track(track):
    sleep(1)
    pyautogui.click(SEARCH)
    sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    sleep(1)
    pyautogui.keyDown('backspace')
    sleep(1)
    pyautogui.typewrite(track)
    sleep(1)
    pyautogui.keyDown('enter')
    sleep(1)
    start = None
    count = 5
    while not start:
        if not start:
            start = pyautogui.locateCenterOnScreen('images/pattern_screenshot.png')
        count -= 1
        if count == 0:
            break
        break
    pyautogui.moveTo(start)
    x, y = pyautogui.position()
    print(x, y)
    ADD_TRACK = (x + 417, y + 74)
    pyautogui.moveTo(ADD_TRACK)
    pyautogui.click(ADD_TRACK)
    sleep(1)

def fix_layout(track_name):
    eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
    rus_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
    trans_table = dict(zip(rus_chars, eng_chars))
    return ''.join([trans_table.get(c, c) for c in track_name])

def main():
    data = YandexMusicParser(YANDEX_MAIL, PASSWORD)
    all_tracks_names = data.parsing_all_tracks()

    open_browser()
    for track_name in all_tracks_names[::-1]:
        language = TextBlob(track).detect_language()
        if language == "ru":
            pyautogui.moveTo(SWITCH_LANGUAGE_step1)
            pyautogui.click(SWITCH_LANGUAGE_step1)
            pyautogui.moveTo(SWITCH_LANGUAGE_RUS)
            pyautogui.click(SWITCH_LANGUAGE_RUS)
            track_name = fix_layout(track_name)
            add_track(track_name)
            continue
        else:
            pyautogui.moveTo(SWITCH_LANGUAGE_step1)
            pyautogui.click(SWITCH_LANGUAGE_step1)
            pyautogui.moveTo(SWITCH_LANGUAGE_ENG)
            pyautogui.click(SWITCH_LANGUAGE_ENG)
            add_track(track)
        sleep(1)
        
main()
        
