#-*- coding: UTF-8 -*-
print('Diga a veocidade do seu carro, que eu direi ce foi multado')
car = float(input('Digita a velocidade: '))
if car > 80:
    vel= (car-80)*5
    print('Você foi multado, o valor da multa é: ', vel)
els