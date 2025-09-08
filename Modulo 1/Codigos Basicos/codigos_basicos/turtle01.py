import turtle

t = turtle.Turtle()
t.speed(3)

def desenhar():
    encostar = t.pen()["pendown"]
    if encostar:
       t.penup()
       print("NÃO ENCOSTANDO")
    else: 
        t.pendown()
        print("ENCOSTANDO")

def engrossar_caneta():
    grossura_linha = t.pen()["pensize"]
    t.pensize(grossura_linha + 1)

def afinar_caneta():
    grossura_linha = t.pen()["pensize"]
    if grossura_linha - 1 >= 1:
        t.pensize(grossura_linha - 1)

def borracha():
    cor_fundo = tela.bgcolor()
    cor_caneta = t.pen()["pencolor"]

    if cor_caneta == cor_fundo:
        t.color("black")
        t.shape("classic")
        t.width(1)
    else:
        t.color(cor_fundo,"gray")
        t.width(5)

def mover_para_cima():
    y = t.ycor()
    t.sety(y + 10)

def mover_para_baixo():
    y = t.ycor()
    t.sety(y - 10)

def mover_para_direita():
    x = t.xcor()
    t.setx(x + 10)

def mover_para_esquerda():
    x = t.xcor()
    t.setx(x - 10)

def mover_diagonal_direita_cima():
    x = t.xcor()
    y = t.ycor()
    t.setposition((x+10, y+10))

def mover_diagonal_esquerda_baixo():
    x = t.xcor()
    y = t.ycor()
    t.setposition((x-10, y-10))

def mover_diagonal_esquerda_cima():
    x = t.xcor()
    y = t.ycor()
    t.setposition((x-10, y+10))

def mover_diagonal_direita_baixo():
    x = t.xcor()
    y = t.ycor()
    t.setposition((x+10, y-10))

seguidor = turtle.Turtle()
seguidor.color("green")
seguidor.shape("turtle")
seguidor.speed(1)
velocidade_seguidor = 5

def mover_seguidor():
    x_player = t.xcor()
    y_player = t.ycor()

    x_seguidor = seguidor.xcor()
    y_seguidor = seguidor.ycor()

    if abs(x_player - x_seguidor) > velocidade_seguidor:
       
        if x_player > x_seguidor:
            x_seguidor = x_seguidor + velocidade_seguidor
            
        else:
            x_seguidor = x_seguidor - velocidade_seguidor
        
    else:
        x_seguidor = x_player

    if abs(y_player - y_seguidor) > velocidade_seguidor:
        if y_player > y_seguidor:
            y_seguidor = y_seguidor + velocidade_seguidor
        else:
            y_seguidor = y_seguidor - velocidade_seguidor
    else:
        y_seguidor = y_player

    seguidor.setposition(x_seguidor,y_seguidor)
    
    tela.ontimer(mover_seguidor,100)

tela = turtle.Screen()
tela.listen()

tela.onkeypress(mover_para_cima,"1")
tela.onkeypress(mover_para_baixo,"2")
tela.onkeypress(mover_para_direita,"3")
tela.onkeypress(mover_para_esquerda,"4")
tela.onkeypress(mover_diagonal_direita_cima,"5")
tela.onkeypress(mover_diagonal_esquerda_baixo,"6")
tela.onkeypress(mover_diagonal_esquerda_cima,"7")
tela.onkeypress(mover_diagonal_direita_baixo,"8")

tela.onkeypress(desenhar,"p")
tela.onkeypress(borracha,"b")
tela.onkeypress(engrossar_caneta,"m")
tela.onkeypress(afinar_caneta,"n")
mover_seguidor()


tela.mainloop
turtle.done()
