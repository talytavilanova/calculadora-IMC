print ('Solicitando peso e altura para calcular o IMC!')
peso = float(input('Qual seu peso em (Kg)?'))
altura = float(input('Qual sua altura em (m)?'))
imc = peso/(altura**2)
print('O IMC calculado é de {:.1f}'.format(imc))
if imc < 18.5:
 print('Seu status é ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
 print('Seu status é PESO IDEAL!')
elif 25 <= imc < 30:
 print('Seu status é SOBREPESO!')
elif 30 <= imc < 40:
 print('Seu status é PESO IDEAL!')
elif imc >= 40:
 print('Seu status é PESO IDEAL!')
