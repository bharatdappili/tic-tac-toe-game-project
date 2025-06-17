from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title('Tic-Tac-Toe_game')
Players = ['Srikanth', 'uday kiran']
turn = '1st'
count = 0

messa = True

def disable_all_buttons():
    for k in Buttons:
        k.config(state=DISABLED)

def checkifwon():
    global winner, count, messa
    winner = False
    win_index = []
    for x in Players:
        for i in range(9):
            if i == 0 or i == 3 or i == 6:
                if Buttons[i]['text'] == x and Buttons[i+1]['text'] == x and Buttons[i+2]['text'] == x:
                    win_index = [i, i+1, i+2]
                    winner = True
            if i == 0 or i == 1 or i == 2:
                if Buttons[i]['text'] == x and Buttons[i+3]['text']==x and Buttons[i+6]['text'] == x:
                    win_index = [i, i + 3, i + 6]
                    winner = True
            if i == 0:
                if Buttons[i]['text'] == x and Buttons[i+4]['text'] ==x and Buttons[i+8]['text'] == x:
                    win_index = [i, i + 4, i + 8]
                    winner = True
            if i == 2:
                if Buttons[i]['text'] == x and Buttons[i+2]['text'] ==x and Buttons[i+4]['text'] == x:
                    win_index = [i, i + 2, i + 4]
                    winner = True
        if winner == True:
            for k in win_index:
                Buttons[k].config(highlightbackground='Red')
            b = f'Congratulations {x}, you won!'
            root.update()
            time.sleep(1)
            messagebox.showinfo("Tic-Tac-Toe", b)
            next_round = messagebox.askquestion("Tic-Tac-Toe", " Want to Play Another Round? ")
            if next_round == 'yes':
                count = 0
                for k in Buttons:
                    k['text'] = ' '
                    k.config(highlightbackground='Yellow')
            elif next_round == 'no':
                disable_all_buttons()
                exit()
            break
        elif winner == False and count == 9:
            root.update()
            time.sleep(1)
            next_round = messagebox.askquestion("Tic-Tac-Toe", 'It is a Tie No one wins \n Want to play another Round?')
            if next_round == 'yes':
                for k in Buttons:
                    k['text'] = ' '
                break
            elif next_round == 'no':
                disable_all_buttons()
                root.quit()

def click(b):
    global turn, count
    b = b.widget
    txt = b['text']
    if txt == ' ' and turn == '1st':
        b['text'] = Players[0]
        count += 1
        turn = '2nd'
        checkifwon()
    elif txt == ' ' and turn == '2nd':
        b['text'] = Players[1]
        count += 1
        turn = '1st'
        checkifwon()

buttons = [f'b{i}' for i in range(1, 10)]
Buttons = []
for k in buttons:
    globals()[k] = Button(root, text=' ', width=20, height=10, highlightbackground='yellow')
    Buttons.append(globals()[k])
    globals()[k].bind('<Button-1>', click)

row = 0
column = 0
for i in range(9):
    Buttons[i].grid(row=row, column=column)
    column += 1
    if i == 2 or i == 5:
        row += 1
        column = 0
root.mainloop()
