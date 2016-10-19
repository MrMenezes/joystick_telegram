from telegame import Telegame
import telepot
import serial
import struct
import pyautogui
import time

com = ['down','left','right','a']
p1dict = {'down': 'S','left': 'A','right': 'D','a': 'G'}
p2dict =  {'down': 'down','left': 'left','right': 'right','a': 'L'}


game = Telegame('281998070:AAFtmfn_AvM9nALccETBI3NkOnf4maR1L5I')
p1 = dict()
p2 = dict()


@game.private_command(com)
def cmd(msg):
    command = msg['text'][1:] 
    #send(command)
    if msg['chat']['id'] in p1:
        print(msg['chat']['username'] + ' Player 1: ' + str(command))
        pyautogui.keyDown(p1dict[command])
        time.sleep(0.2)
        pyautogui.keyUp(p1dict[command])
    elif msg['chat']['id'] in p2:
        print(msg['chat']['username'] + ' Player 2: ' + str(command))
        pyautogui.keyDown(p2dict[command])
        time.sleep(0.2)
        pyautogui.keyUp(p2dict[command]) 

from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

@game.private_command('key')
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    game.sendMessage(chat_id, 'Activate keyboard',
                    reply_markup=ReplyKeyboardMarkup(
                        keyboard=[                           
                            [KeyboardButton(text="/left"), KeyboardButton(text="/right"),KeyboardButton(text="/a"),KeyboardButton(text="/a")],
                             [KeyboardButton(text="/p1"),KeyboardButton(text="/down"),KeyboardButton(text="/p2"),KeyboardButton(text="/a"),KeyboardButton(text="/a")],
                        ]
                    ))

@game.private_command('p1')
def p1add(msg):
    if not msg['chat']['id'] in p2:
        p1[msg['chat']['id']] = ""
        print(msg['chat']['username'] + ' Player 1')
@game.private_command('p2')
def p2add(msg):
    if not msg['chat']['id'] in p1:
        p2[msg['chat']['id']] = ""
        print(msg['chat']['username'] + ' Player 2')
@game.private_command('p1cls')
def p1cls(msg):
    p1 = dict()
@game.private_command('p2cls')
def p2cls(msg):
    p2 = dict()

game.start()

 
