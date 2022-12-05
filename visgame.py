from tkinter import *
import random
import time

optionsen = 'truth ninja plain alarm giant force punch berry twins broad paper pulse furry drink viola larva chess queen stove dolor spawn pants guide troop kazoo vixen colon truck first drama rider rifle login chaos water paint trade level bunch sound hotel earth photo troop scout viola yeast river fanny stage serum jelly right skirt drill dozen medal cloth cycle count trunk fence story blush blind spank blast punch haste sleep piano horst glory plume dance frock thing ferry staff share glass cloth guard spark bench demon share toque class siege quota vault ranch faith shame spade robot chick larva thyme swath river fiber inbox skunk facet layer fairy koala patty wheat slang filth woman award truth modem riser stove'
optionsru = 'дождь гроза вихрь алиби алкаш аллах актив акула акциз акция банан банда'
optionsua = ''

symbolswin = []
symbols = []
option = '' 
letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
lettersmassive = []

for i in letters:
    print(i)
    lettersmassive.append(i)

print(lettersmassive) 

yazikhi = []

root = Tk()
root.geometry('300x430')
root.title('Game')
root.resizable(width=False, height=False)

def lang(l):
    global yazikhi
    if len(yazikhi) == 0:
        if l == 'en':
            txt2['text'] = 'Six mistakes to lose'
            txt1['text'] = '"Viselyca" Guess word of 5 letters'
            yazikhi.append('en')
            optionsall = list(optionsen.split(' '))
            option = (random.choice(optionsall))
            print(option)
            for i in option:
                symbolswin.append(i)
                print(symbolswin)
            return True

        elif l == 'ru':
            txt2['text'] = '6 ошибок и проиграешь!'
            txt1['text'] = '"Виселица" Угадай слово\nВсего 5 букв'
            yazikhi.append('ru')
            optionsall = list(optionsru.split(' '))
            option = (random.choice(optionsall))
            option.lower()
            print(option)
            for i in option:
                symbolswin.append(i)
                print(len(symbolswin))
            return True
        else:
            txt2['text'] = 'Choose a language!'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = ''
            txt2['bg'] = 'white'
            return True
    else:
        if l == 'en':
            txt2['text'] = 'Сan not change language'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = 'Six mistakes to lose!'
            txt2['bg'] = 'white'
            return True
        elif l == 'ru':
            txt2['text'] = f'Нельзя менять язык'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '6 ошибок и проиграешь'
            txt2['bg'] = 'white'
            return True       
        print('ohh')

def checkdubla(sym, l):
    if not sym in symbols:
        symbols.append(sym)
        return False
    else:
        if l[0] == 'en':
            txt2['text'] = f'Letter "{sym}" already was'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = 'Six mistakes to lose!'
            txt2['bg'] = 'white'
            return True
        elif l[0] == 'ru':                  
            txt2['text'] = f'Буква "{sym}" уже была'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '6 ошибок и проиграешь'
            txt2['bg'] = 'white'
            return True

player_answer = Entry(root, bg='#C9C9C9')
player_answer.place(y=260, x=90)
mistakescore = 0
bot_score = Label(root, text=f'{mistakescore}', font='Arial, 50')
bot_score.pack()
txt2 = Label(root, text='', font='Arial, 13')
txt2.place(x=67, y=400)
txt1 = Label(root, text='Choose language: EN or RU', font='Arial, 13')
txt1.pack()
txt3 = Label(root, text='', font='ARIAL, 17')
txt3.place(x=73, y=215)

def guesslet():
    global mistakescore
    valsymbol = player_answer.get()
    valsymbolower = valsymbol.lower()

    if lang(valsymbolower) == True: 
        print('false!')
        return 'false!'
    
    if not valsymbolower in lettersmassive:
        print(yazikhi[0])
        if yazikhi[0] == 'ru':
            txt2['text'] = 'Только 1 рус буква!'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '6 ошибок и проиграешь'
            txt2['bg'] = 'white'
            return 'xuinya'
        if yazikhi[0] == 'en':
            txt2['text'] = 'Only 1 eng letter'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = 'Six mistakes to lose!'
            txt2['bg'] = 'white'
            return 'xyi'

    if checkdubla(valsymbolower, yazikhi) == True:
        print('noo')
        return 'xyi'

    if valsymbolower in symbolswin:
        for index, letter in enumerate(symbolswin):            
            if letter == valsymbolower:
                if index == 0:
                    num1['text'] = letter
                if index == 1:
                    num2['text'] = letter
                if index == 2:
                    num3['text'] = letter
                if index == 3:
                    num4['text'] = letter
                if index == 4:
                    num5['text'] = letter

        if num1['text'] != '_':
            if num2['text'] != '_':
                if num3['text'] != '_':
                    if num4['text'] != '_':
                        if num5['text'] != '_':
                            print('yes')
                            txt2['text'] = 'Ты выиграл!!!'
                            txt2['bg'] = 'blue'
                            entry_button['state'] = DISABLED

    else:
        mistakescore += 1
        bot_score['bg'] = 'red'
        bot_score['text'] = mistakescore
        if mistakescore == 6:
            txt2['text'] = 'Ты проиграл!'
            txt2['bg'] = 'red'
            entry_button['state'] = DISABLED
            print(option)
            txt3['text'] = f'{symbolswin[0]} {symbolswin[1]} {symbolswin[2]} {symbolswin[3]} {symbolswin[4]}'
            print(symbolswin)                                
                

entry_button = Button(root,command=guesslet, text='Ввести',font='Arial, 20')
entry_button.place(x=80, y=300, width=150)
num1 = Label(root, text='_', font='Arial, 50')
num1.place(x=30, y=130)
num2 = Label(root, text='_', font='Arial, 50')
num2.place(x=75, y=130)
num3 = Label(root, text='_', font='Arial, 50')
num3.place(x=120, y=130)
num4 = Label(root, text='_', font='Arial, 50')
num4.place(x=165, y=130)
num5 = Label(root, text='_', font='Arial, 50')
num5.place(x=210, y=130)

root.mainloop()