from time import sleep
import pyautogui
from textblob import TextBlob
from parser_yandex_music import Parser_Yandex_Music

# add your yandex account for parser
YANDEX_MAIL = "*****@yandex.com"
password = "*****************"

CHROME_ICON = (215, 1055)
CHROME_URL = (410, 70)
# add your full link to vk music
VK_MUSIC_LINK = "https://vk.com/audios240917398"
SEARCH = (901, 406)
ADD_TRACK = (1462, 525)
SWITCH_LANGUAGE_step1 = (1732, 1059)
SWITCH_LANGUAGE_RUS = (1817, 834)
SWITCH_LANGUAGE_ENG = (1835, 919)

#used to determine the location of the cursor
screenWidth, screenHeight = pyautogui.size()
x, y = pyautogui.position()
print(x, y)

def openBrowser():
    print("Opening browser Google Chrome")
    pyautogui.click(CHROME_ICON)
    sleep(1)

def addtrack(track):
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
    while start == None:
        if start == None:
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

def fix_layout(s):
    eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
    rus_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
    trans_table = dict(zip(rus_chars, eng_chars ))
    return ''.join([trans_table.get(c, c) for c in s])

data = Parser_Yandex_Music(YANDEX_MAIL, password)
all_tracks = data.parsing_all_tracks()

openBrowser()
for track in all_tracks[::-1]:
    language = TextBlob(track).detect_language()
    if language == "ru":
        pyautogui.moveTo(SWITCH_LANGUAGE_step1)
        pyautogui.click(SWITCH_LANGUAGE_step1)
        pyautogui.moveTo(SWITCH_LANGUAGE_RUS)
        pyautogui.click(SWITCH_LANGUAGE_RUS)
        track = fix_layout(track)
        addtrack(track)
        continue
    else:
        pyautogui.moveTo(SWITCH_LANGUAGE_step1)
        pyautogui.click(SWITCH_LANGUAGE_step1)
        pyautogui.moveTo(SWITCH_LANGUAGE_ENG)
        pyautogui.click(SWITCH_LANGUAGE_ENG)
        addtrack(track)
    sleep(1)
