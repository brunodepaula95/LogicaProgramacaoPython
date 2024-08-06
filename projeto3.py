#Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e ecom base nessa velocidade diga se ele tomou uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir " levou multa leve", caso esteja entre 11 a 20km  acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima"

velocidade = int(input('Digite sua velocidade'))
velocidade_maxima = 80

if velocidade <= velocidade_maxima:
    print('Não levou multa')

elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Levou multa leve')

elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Levou multa grave')

elif velocidade > velocidade_maxima + 20:
    print('Levou multa gravissima')