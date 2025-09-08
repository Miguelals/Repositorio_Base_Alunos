import pyautogui

pyautogui.PAUSE=1
#pyautogui.press()
pyautogui.hotkey('win','r')

pyautogui.write("chrome")
pyautogui.press("enter")


pyautogui.write("instagram.com")
pyautogui.press("enter")


pyautogui.countdown(3)

# pyautogui.click(116,272)
# pyautogui.write("")
# pyautogui.press("enter")

# pyautogui.click(140,204)
# pyautogui.write("s0uza_gl_")
# pyautogui.press("enter")

pyautogui.click(39,376)
pyautogui.write("")
pyautogui.press("enter")

def aperta_tab(qtd):
    for _ in range(qtd):
        pyautogui.press('tab')

    aperta_tab(10)
# pyautogui.mouseInfo()