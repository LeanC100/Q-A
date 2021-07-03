import os
import pathlib

started = 1
quited = 0

file_answers = 'answers.txt'
file_questions = 'questions.txt'

point = 0

def start():
    question = open(file_questions, 'r')
    answer = open(file_answers, 'r')
    point = 0
    for line in question:
        os.system('cls')
        ok= False
        print(line)
        print('')
        op1, op2, op3, op4 = answer.readline().split('|')

        op_correct = opCorrect(op1, op2, op3, op4)

        print(f'{op1}\n{op2}\n{op3}\n{op4}')
        print()
        op_selected = input('Select a option: ')

        # El bucle While seguira hasta que el usuario coloque una de las 4 optiones validas
        while not ok: 
            try:
                op_selected = int(op_selected)
            except ValueError:
                op_selected = -1

            if op_selected == 1 or op_selected == 2 or op_selected == 3 or op_selected == 4:
                ok=True
                if op_correct == op_selected:
                    print('Very Good!!!')
                    point+=1
                else:
                    print('Hoooo you chose the wrong option ')
                input('Press a botton for continues')
            else:
                print('You a option valid,plase')
                op_selected = input('Select a option: ')
                
        os.system('cls')
    print('Congratulations!!!!!')
    print(f'You got {point}')
    input('Press for return menu')

def opCorrect(op1,op2,op3,op4):
    op_correct = 0

    if op1[-1] == ' ':
        op_correct = 1
    elif op2[-1] == ' ':
        op_correct = 2
    elif op3[-1] == ' ':
        op_correct = 3
    elif op4[-1] == ' ':
        op_correct = 4
    
    return op_correct


def menu():
    continues= True
    while continues:
        print('HI!!! Wecome to Q&A')
        print(f'''
    {started}- Start
    {quited}- Quit    
        ''')
        op = input('Select a option: ')
        try:
            op = int(op)
        except ValueError:
            op = -1
        if op == started:
            start()
        elif op == quited:
            continues = False
        else:
            print('Option no valid')
            print('Please, Select other option')
        print('')

def main ():
    os.system('cls')

    menu()

if __name__ == '__main__':
    main()
