import os
from random import random
import pyttsx3

localvoice = pyttsx3.init()
def menu ():
    menu_choice = {
        1: 'Nhập từ phím',
        2: 'Import file từ vứng ( từ vựng|nghĩa từ ): '
    }
    for x, y in menu_choice.items():
        print(x, '=>', y)
    choice = input('Enter the number of choices: ').strip()
    return int(choice)


def more_functions ():
    menu_choice = {
        1: 'Check ghi nhớ',
        2: 'Check từ'
    }
    for x, y in menu_choice.items():
        print(x, '=>', y)
    choice = input('Enter the number of chocies: ').strip()
    return int(choice)

def checkList (listchar):
    os.system('cls')
    print('Co cai nit ma nhin ket qua:))')
    length = len(listchar)
    print('Có', length, 'từ nên hãy cố nhớ nhé')
    yourChar = {}
    for x in range(length):
        gram = input('[' + str(x+1) + '] => Từng vựng: ')
        trans = input('[' + str(x+1) + '] => Nghĩa từ: ')
        yourChar[gram] = trans
    score = 0
    for x in listchar:
        for a, b in yourChar.items():
            if x['char'] == a:
                if b in x['trans'] or b == x['trans']:
                    score += 1
    print('Your score is: ', str(score) + '/' + str(length))

def checkTu (listchar):
    repeat = int(input('Muốn lặp bao nhiêu lần: '))
    askMode = input('Việt sang Anh ghi N, Anh sang Việt ghi A: ').lower()
    for x in range(repeat):
        os.system('cls')
        print('Số lần: ' + str(x))
        if askMode == 'n':
            for x in listchar:
                trans = x['trans']
                print(trans + ' = ', end='')
                
                check = input().lower()
                if x['char'].lower() == check:
                    localvoice.say(check)
                    localvoice.runAndWait()
                    print('Đúng')
        else:
            for x in listchar:
                char = x['char']
                localvoice.say(char)
                localvoice.runAndWait()
                print(char + ' = ', end='')
                check = input().lower()
def getFirstCharList (listchar):
    listReturn = []
    for x in listchar:
        listReturn.append(x['char'][0])
    return listReturn
    
def sortChar (listchar):
    getFirstList = getFirstCharList(listchar)
    listCharHidden = []
    listSpam = {}
    for x in getFirstList:
        for y in listchar:
            if y['char'][0] == x and y['char'] not in listCharHidden:
                print(y['char'] + ': ' + y['trans'])
                listCharHidden.append(y['char'])
                if x in listSpam:
                    listSpam[x]['amount'] += 1
                    listClone = list(listSpam[x]['char'])
                    listClone.append(y['char'])
                    listSpam[x]['char'] = tuple(listClone)
                else:
                    listSpam[x] = {'amount': 0, 'char': (y['char'],)}
    for x, y in listSpam.items():
        print(x, '=', str(y['amount']+1) , ' ' , str(y['char']))


choice = menu()
listGram = []
if choice == 1:
    length = int(input('Nhập số từ vựng: '))
    for x in range(1, length + 1):
        listGram.append({
            'char': input('[' + str(x) + '] Từ vựng = '),
            'trans': input('[' + str(x) + '] Nghĩa từ = ')
        })
elif choice == 2:
    file_name = input('Enter the file name: ')
    with open(file_name, 'r', 10000, 'utf-8') as f:
        lines = f.readlines()
        for x in lines:
            split_the_char = x.split('|')
            char = split_the_char[0]
            trans = split_the_char[1]
            listGram.append({
                'char': char,
                'trans': trans
            })
sortChar(listGram)
ask = input('Do you want use the more function? (y/n): ').lower()
if ask == 'y':
    choice = more_functions()
    if choice == 1:
        checkList(listGram)
    elif choice == 2:
        checkTu(listGram)
