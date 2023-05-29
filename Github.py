import turtle
import random

t = turtle.Turtle()

#Desenho da forca
t.penup()
t.right(90)
t.forward(100)
t.left(90)
t.pendown()
t.backward(100)
t.forward(50)
t.left(90)
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)

#Desenho do boneco
def cabeca():
    t.penup()
    t.forward(50)
    t.left(90)
    t.pendown()
    t.circle(25)

def corpo():
    t.right(90)
    t.forward(50)

def bracoE():
    t.backward(50)
    t.left(45)
    t.forward(25)
    t.backward(25)
    t.right(45)

def bracoD():
    t.right(45)
    t.forward(25)
    t.backward(25)
    t.left(45)
    t.forward(50)

def pernaE():
    t.left(45)
    t.forward(50)
    t.backward(50)
    t.right(45)

def pernaD():
    t.right(45)
    t.forward(50)


#Criando a parte da palavra
print("""\n Bem vindo ao nosso jogo da Forca organizado pelos alunos:
- Arlindo Filho
- Fernanda
- Yasmin
Espero que se divirta""")
aleatorio = ['Amiga', 'Amor', 'Ave', 'Avião', 'Avó', 'Balão', 'Bebê', 'Bolo', 'Branco', 'Cama', 'Caneca', 'Celular', 'Céu', 'Clube', 'Copo', 'Doce', 'Elefante', 'Escola', 'Estojo', 'Faca', 'Foto', 'Garfo', 'Geleia', 'Girafa', 'Janela', 'Limonada', 'Mãe', 'Meia', 'Noite', 'Óculos', 'ônibus', 'Ovo', 'Pai', 'Pão', 'Parque', 'Passarinho', 'Peixe', 'Pijama', 'Rato', 'Umbigo']
palavra = random.choice(aleatorio)

quantidade_de_letras = len(palavra)


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digitadas = []
corretas = []
erros = 0
acertos = []
letras_certas = 0

while erros < 6:
  underlines = ''
  for letra in palavra:
    underlines += letra if letra in acertos else "_ "
  print(underlines)
  letra = input('Digite uma letra: ').lower().strip()
  if letra in alfabeto:
    if letra in digitadas:
        print('Você já digitou essa letra')
    else:
        if letra in palavra:
          acertos += letra
          letras_certas += 1
          if len(set(palavra)) == letras_certas:
            print('\nVocê venceu! 😄\n')
            print(f'A palavra é "{palavra}"!')
            break
        else:
            if erros == 0:
                cabeca()
            elif erros == 1:
                corpo()
            elif erros == 2:
                bracoE()
            elif erros == 3:
                bracoD()
            elif erros == 4:
                pernaE()
            elif erros == 5:
                pernaD()
            erros += 1
    digitadas.append(letra)
  else:
    print('Caractére inválido!')
    
if erros == 6:
  print('\nVocê perdeu 💀\n')
  print(f'\nA palavra era "{palavra}"\n')
