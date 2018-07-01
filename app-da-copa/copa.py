# -*- coding: utf-8 -*-
import requests, sys
import datetime
import time


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

for jogosdachave in chavesetapa:

	rodada = rodada + 1

	print ('')
	
	jogos = jogosdachave.split('chave-jogo chave-1-jogos')

	del jogos[0]

	print ('-------------')

	print ("Rodada " + str(rodada))

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

		if len(auxplacar2[0]) > 0:
			print ('Placar: '),
			print (auxplacar2[0] + " x " + auxplacar2[1])
		

		print ('Dia: ' + dia)

		print ('Horario: '),
		print (horario)

		print ('Estadio: '),
		print (estadio)

		print ('')

		

		



	
	print ('-------------')

print ('')

