import requests
from sympy import im
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

import urllib3
urllib3.disable_warnings()



r = requests.get('https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena', headers=headers, verify=False)

##################### Pegando o texto dentro do código completo da página ####################
meuHTML = str(r.content)
posInicial = meuHTML.find('listaDezenas') + 31
posFinal = meuHTML.find(']', posInicial) + 1

Numeros = meuHTML[posInicial:posFinal]
#print(Numeros)

##################### Usando o formato JSON ##################################################
import json

ConteudoJson = json.loads(r.content)

#print(ConteudoJson["dezenasSorteadasOrdemSorteio"])

Numero1 = ConteudoJson["listaDezenas"][0]
Numero2 = ConteudoJson["listaDezenas"][1]
Numero3 = ConteudoJson["listaDezenas"][2]
Numero4 = ConteudoJson["listaDezenas"][3]
Numero5 = ConteudoJson["listaDezenas"][4]
Numero6 = ConteudoJson["listaDezenas"][5]
megasena_6_acertos = ConteudoJson["listaRateioPremio"][0]
megasena_5_acertos = ConteudoJson["listaRateioPremio"][1]
megasena_4_acertos = ConteudoJson["listaRateioPremio"][2]


print(ConteudoJson["tipoJogo"])
print(('Números sorteados:'), Numero1, Numero2, Numero3, Numero4, Numero5, Numero6)

print(('Número do Jogo:'), ConteudoJson["numero"])
print(('Data do Jogo:'), ConteudoJson["dataApuracao"])

print(('Número de ganhadores 6 dezenas:'), megasena_6_acertos["numeroDeGanhadores"])
print('Valor do prêmio R$: {:.2f}'.format(megasena_6_acertos["valorPremio"]))

print(('Número de ganhadores 5 dezenas:'), megasena_5_acertos["numeroDeGanhadores"])
print('Valor do prêmio R$: {:.2f}'.format(megasena_5_acertos["valorPremio"]))

print(('Número de ganhadores 4 dezenas:'), megasena_4_acertos["numeroDeGanhadores"])
print('Valor do prêmio R$: {:.2f}'.format(megasena_4_acertos["valorPremio"]))

#print(('Valor estimado para o próximo prêmio R$:'), ConteudoJson["valorEstimadoProximoConcurso"])
print('Valor estimado para o próximo prêmio R$ {:.2f}'.format(ConteudoJson["valorEstimadoProximoConcurso"]))

l1 = [Numero1, Numero2, Numero3, Numero4, Numero5, Numero6]
l2 = ['01', '04', '09', '11', '22', '27']
    
print("Dezenas que acertei no jogo 1:", set(l1) & set(l2))

Qtd1 = len(set(l1) & set(l2))

print(('Quantidade de dezenas acertadas no jogo 1:'), Qtd1, ('Dezena(s)'))