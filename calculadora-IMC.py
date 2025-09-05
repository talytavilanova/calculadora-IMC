def calcular_imc():
    print('🔎 Solicitando peso e altura para calcular o IMC!\n')

    try:
        peso = float(input('➡️ Qual seu peso (kg)? '))
        altura = float(input('➡️ Qual sua altura (m)? '))
        imc = peso / (altura ** 2)
    except ValueError:
        print("❌ Entrada inválida. Certifique-se de digitar números válidos.")
        return

    print('\n✅ IMC calculado: {:.1f}'.format(imc))

    if imc < 18.5:
        status = 'Abaixo do peso'
    elif 18.5 <= imc < 25:
        status = 'Peso normal'
    elif 25 <= imc < 30:
        status = 'Sobrepeso'
    elif 30 <= imc < 35:
        status = 'Obesidade grau I'
    elif 35 <= imc < 40:
        status = 'Obesidade grau II'
    else:
        status = 'Obesidade grau III'

    print(f'Seu status é: {status.upper()}')

if __name__ == "__main__":
    calcular_imc()
