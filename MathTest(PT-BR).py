import random
import tkinter
import time


def questionário():
    questões_certas = 0
    a1 = random.randint(0, 100)
    b1 = random.randint(0,100)
    pergunta1 = f'Qual o resultado da soma dos números {a1} e {b1}?'
    print(pergunta1)
    resultado_input1 = int(input(''))
    if resultado_input1 == (a1 + b1):
        questões_certas = questões_certas + 1
        print('Você acertou!')
    else:
        print('Você infelizmente errou! Quem sabe da próxima vez!')
    a2 = random.randint(0, 100)
    b2 = random.randint(0, 100)
    pergunta2 = f'Qual o resultado da soma dos números {a2} e {b2}?'
    print(pergunta2)
    resultado_input2 = int(input(''))
    if resultado_input2 == (a2 + b2):
        questões_certas = questões_certas + 1
        print('Você acertou!')
    else:
        print('Você infelizmente errou! Quem sabe da próxima vez!')
    acertos = 0
    a3 = random.randint(0, 100)
    b3 = random.randint(0, 100)
    pergunta3 = f'Qual o resultado da soma dos números {a3} e {b3}?'
    print(pergunta3)
    resultado_input3 = int(input(''))
    if resultado_input3 == (a3 + b3):
        questões_certas = questões_certas + 1
        print('Você acertou!')
    else:
        print('Você infelizmente errou! Quem sabe da próxima vez!')
    acertos = 0
    a4 = random.randint(0, 100)
    b4 = random.randint(0, 100)
    pergunta4 = f'Qual o resultado da soma dos números {a4} e {b4}?'
    print(pergunta4)
    resultado_input4 = int(input(''))
    if resultado_input4 == (a4 + b4):
        questões_certas = questões_certas + 1
        print('Você acertou!')
    else:
        print('Você infelizmente errou! Quem sabe da próxima vez!')
    acertos = 0
    a5 = random.randint(0, 100)
    b5 = random.randint(0, 100)
    pergunta5 = f'Qual o resultado da soma dos números {a5} e {b5}?'
    print(pergunta5)
    resultado_input5 = int(input(''))
    if resultado_input5 == (a5 + b5):
        questões_certas = questões_certas + 1
        print('Você acertou!')
    else:
        print('Você infelizmente errou! Quem sabe da próxima vez!')

    time.sleep(3)

    def resultado_final():
        print(f'As perguntas do questionário foram: \n'
              f'{pergunta1} \n'
              f'{pergunta2} \n'
              f'{pergunta3} \n'
              f'{pergunta4} \n'
              f'{pergunta5} \n')
        time.sleep(3)
        print(f'As respostas corretas foram: \n'
              f'{resultado_input1} \n'
              f'{resultado_input2} \n'
              f'{resultado_input3} \n'
              f'{resultado_input4} \n'
              f'{resultado_input5} \n')
        time.sleep(2)
        print('E o seu resultado foi...')
        if questões_certas == 0:
            print('Você não acertou nenhuma questão! Que pena, mas é hora de treinar mais!')
        elif 0 < questões_certas < 2:
            print('Você acertou entre 0 e 2 questões, tem que melhorar, mas já é um começo!')
        elif questões_certas == 3:
            print('Você acertou 3 questões, está na média mas dá pra melhorar!')
        elif questões_certas == 4:
            print('Você acertou 4 questões, está ótimo mas vá em busca da perfeição!')
        elif questões_certas == 5:
            print('Você acertou 5 questões, perfeito!')
    resultado_final()
questionário()
