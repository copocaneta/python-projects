# -*- coding: utf-8 -*-
import requests, sys
import datetime
import time
import operator
from operator import itemgetter
import datetime as dt


# Data e hora

def dataehora():

	print ('')
	print ("Data e hora: " + datetime.datetime.now().strftime("%d-%m-%y %H:%M"))
	print ('')

# Pegando conteúdo

def pegarconteudo(url):
	aux = requests.get(url,headers={"content-type":"text"})
	return str(aux.content)


dataehora()


conteudo = pegarconteudo('https://globoesporte.globo.com/futebol/copa-do-mundo/')
aux = conteudo.split('tabela-navegacao-seletor tabela-navegacao-seletor-ativo')[1]
meio = aux.split('class="tabela-feed"')[0]
titulo = meio.replace('<','>').split('>')[1]

chavesetapa = meio.split('class="chave-jogo-espacador chave-jogo-com-chave-posterior"')

print ('Fase Atual: '),
print (titulo)


del chavesetapa[0]



rodada = 0

listadejogos = []

for jogosdachave in chavesetapa:

	rodada = rodada + 1

	
		

	print ('')
	
	jogos = jogosdachave.split('chave-jogo chave-1-jogos')

	del jogos[0]

	print ('-------------')

	print ("Rodada " + str(rodada))

	print ('')

	# print (type(jogos))

	# auxPartidasPorDia = jogos.replace('<span class="placar-jogo-informacoes-local">','<div class="placar-jogo-informacoes">').split('<div class="placar-jogo-informacoes">')[1]

	# print (auxPartidasPorDia)




	for partidas in jogos:


		print ('-------------')
		print ('Jogo:'), 
		infojogo = partidas.split('<meta itemprop="name" content="') [1]

		jogo = infojogo.split('">')[0]
		
		auxdia = infojogo.split('placar-jogo-informacoes">')[1]
		dia = auxdia.split('<span class="placar-jogo-informacoes-local">')[0]
		estadio = infojogo.replace('<span class="placar-jogo-informacoes-local">', '</span>').split('</span>')[1]
		horario = infojogo.replace('<meta itemprop="startDate" content="', '">').split('">')[2]

		auxplacar = partidas.split('<span class="placar-jogo-equipes-placar-mandante">')[1]
		auxplacar2 = auxplacar.replace('</span> <span class="tabela-icone tabela-icone-versus"></span> <span class="placar-jogo-equipes-placar-visitante">', '</span>').split('</span>')

		print (jogo)

		placar = ""

		if len(auxplacar2[0]) > 0:
			print ('Placar: '),
			print (auxplacar2[0] + " x " + auxplacar2[1])
			placar = str(auxplacar2[0]) + " x " + str(auxplacar2[1])
		

		print ('Dia: ' + dia)

		print ('Horario: '),
		print (horario)

		print ('Estadio: '),
		print (estadio)

		print ('')

		dataarrumada = dia[4:-1].strip()

		
		dataproptyhon = dt.datetime.strptime(dataarrumada, "%d/%m/%Y")
		dataproptyhon = dataproptyhon.date()

		dadosparadicionario = { "Jogo" : jogo, "Placar" : placar, "Dia" : dataarrumada, "Horário" : horario, "Estádio": estadio}
		listadejogos.append([dadosparadicionario])
		
#		if rodada is 1:
#			dadosparadicionario = { "Jogo" : jogo, "Placar" : placar, "Dia" : dia[4:-1], "Horário" : horario, "Estádio": estadio}
#			listadejogos = { "Jogo" : jogo, "Placar" : placar, "Dia" : dia[4:-1], "Horário" : horario, "Estádio": estadio}
#			listadejogos.append([dadosparadicionario])
#
#		elif rodada > "1":
#			dadosparadicionario = { "Jogo" : jogo, "Placar" : placar, "Dia" : dia[4:-1], "Horário" : horario, "Estádio": estadio}
#			listadejogos.append([dadosparadicionario])




	
	print ('-------------')

print ('')

# print sorted(listadejogos, key=itemgetter('Dia'))

#teste = listadejogos.sort(key=operator.itemgetter('Dia'))

#listadejogos.sort(key=lambda item:item['Dia'], reverse=True)

# listadejogos.sort(key=itemgetter('Dia'), reverse=True)


#print (teste)


print ('')


for linha in listadejogos:
	print (linha)
	
# print (list(listadejogos))
