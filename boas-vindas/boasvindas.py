# -*- coding: utf-8 -*-
import requests
import datetime
import time

# Data e hora

def dataehora():

	print ('')
	print ("Data e hora: " + datetime.datetime.now().strftime("%d-%m-%y-%H:%M"))
	print ('')

# Pegando conteúdo

def pegarconteudo(url):
	aux = requests.get(url,headers={"content-type":"text"})
	return str(aux.content)
	

# Temperatura e Condição do céu

def clima():

	aux = pegarconteudo("https://climaagora.com.br/")

	meio = aux.split('col-xs-5 col-sm-5 col-md-5 col-lg-5 xxb')

	partecomtemperatura = meio[1].split('col-xs-2 col-sm-2 col-md-2 col-lg-2 b')


	divs = partecomtemperatura[0].replace('<','>').split('>')

	temperaturahoje = str(divs[1]).strip()

	print('A temperatura atual em São Paulo é ' + temperaturahoje + ' graus celsius.'),



	partecondicao_ceu = partecomtemperatura[1].split('col-xs-7 col-sm-7 col-md-7 col-lg-7 b')

	partecondicao_ceu_divs = partecondicao_ceu[1].split("div")

	condicao_ceu = partecondicao_ceu_divs[0].replace('<','>').split('>')

	condicao_ceu = str(condicao_ceu[1]).strip()

	print (condicao_ceu + ".")

	print ('')

# 10 filmes mais assistidos no imdb em 2018

def top10filmesimdb():
	print ("Filmes mais assistidos em 2018 de acordo com a lista de popularidade do IMDB:")

	conteudo = pegarconteudo("https://www.imdb.com/search/title?year=2018&title_type=feature&view=simple")

	comeco = conteudo.split('lister-list')

	meio = comeco[1].split('class="nav"')[0]

	divs = meio.split('lister-item mode-simple')
	del divs[0]

	contador=0

	for div in divs:

		if contador is 5:
			break
		
		links = div.split('<a href')

		titulo1 = links[2].replace('<','>').split('>')[1]

		contador = contador + 1

		print (str(contador) + " - " + titulo1)

	print ("")

# Noticias principais de sao paulo do g1

def top10noticiasg1sp():
	conteudo = pegarconteudo("http://g1.globo.com/sao-paulo/")

	aux = conteudo.split('class="bastian-page"')
	meio = aux[1].split('load-more gui-color-primary-bg')[0]
	divs = meio.split('feed-post-body-title gui-color-primary gui-color-hover')

	del divs[0]

	contador=0

	print ('Principais notícias da cidade de São Paulo hoje:')

	for div in divs:
		
		if contador is 5:
			break
		
		contador = contador + 1
		links = div.split('<a href=')
		titulo1 = links[1].replace('<','>').split('>')[1]
		linktemp = links[1].replace('<','>').split('>')[0]
		link = linktemp.split('class')[0]

		#titulo2 = links[1].replace('<','>').split('>')
		print ("--------------------------------------------------------")
		print (str(contador) + " - " + titulo1)
		print ("Link: " + link)

	print ("--------------------------------------------------------")
	print ("")	

# Noticias da Copa do Mundo do UOL 

def top4noticiascopauol():
	conteudo = pegarconteudo("https://esporte.uol.com.br/futebol/copa-do-mundo/")

	aux = conteudo.split('class="row"')
	meio = aux[3].split("</section")[0]
	h3s = meio.split('<h3 class="thumb-title">')
	del h3s[0]
	contador=0
	print ('Principais notícias da Copa do Mundo da Rússia:')
	for h3 in h3s:
		contador = contador + 1
		titulo = h3.split("</h3>")[0]
		print ("--------------------------------------------------------")
		print (str(contador) + " - " + titulo + ".")
	print ("--------------------------------------------------------")

# Chamando funções:

dataehora()
 
clima()

top10filmesimdb()

top10noticiasg1sp()

top4noticiascopauol()















