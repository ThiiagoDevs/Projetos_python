import pyautogui
import time

digite = input('Mensagem do boot: ')
message = digite
n = int(input('Quantidade de mensagem: '))
time.sleep(4)

for i in range(n):
    pyautogui.typewrite(message + '\n')
    time.sleep(10)
