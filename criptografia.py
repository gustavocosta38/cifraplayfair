
# 1 - CRIA UMA MATRIZ 5X5, A CHAVE EH FORNECIDA, LOGO APOS INTRODUZ A CHAVE NA MATRIZ
import numpy as np	
matriz = np.chararray((5,5))

for i in range(0,5):
	for j in range(0,5):
		matriz[i][j]="0"

chave = raw_input("Digite a chave: ")
add = np.chararray(len(chave))

j=len(chave)-2 
i =len(chave)-1
t =0
while i >= 0:
	while j >= 0:
		
		if chave[i] == chave[j]:
			t =1						 
		j =j-1	
	if t == 0:
		add[i] = chave[i]
	else:
		add[i] = 0	
	i = i - 1
	t =0
	j=i-1 				
x = 0
i = 0
j = 0

#2- ADICIONA O ALFABETO NA MATRIZ DE ACORDO COM AS LETRA Ja PRESENTES(LETRAS DA CHAVE)

while x < len(add):
	if add[x] != "0":
		matriz[i][j] = add[x]
		j = j + 1
		if j >= 5:
			j=0
			i= i + 1
	x = x + 1		


y = 97
count = 0
k =0
l=0
x =0
j=0
i = 0

while y < 122:
	if y== 121:
		y=122
	while ord(matriz[i][j]) != 48 and chr(y) != matriz[i][j]:
		j=j+1
		if j>=5:
			j=0
			i=i+1
	matriz[i][j] = chr(y)
	y=y+1
	i=0
	j=0
"""
FUNCAO PROCURAMATRIZ: 
 - RECEBE 1 PAR DE CARACTER
 - PROCURA AS POSICOES DENTRO DA MATRIZ
 - EH ADICIONADO NO ARQUIVO DE SAIDA O PAR DE CARACTER DE ACORDO COM AS REGRAS DA CIFRA PLAYFAIR
"""
def procuramatriz(a,b,matriz,arquivo,nomedoarquivoSaida):
	i =0 
	j =0
	t=0
	r=0
	k=0
	l=0
	while i < 5:
		while j < 5: 
			if matriz[i][j] == chr(a):
				k = i
				l = j	
			if matriz[i][j] == chr(b):
				t = i
				r = j
			j=j+1
		j=0
		i=i+1
	conteudo = arquivo.readlines()
	linha1 = k
	coluna1 = l
	linha2 = t
	coluna2 = r

	if 	linha1 == linha2:
		arquivo = open(nomedoarquivoSaida, 'w')
		if coluna1 + 1 == 5:
			coluna1 = 0;
		if coluna2 + 1 == 5:
			coluna2 = 0;	
		conteudo.append(matriz[linha1][coluna1+1])
		conteudo.append(matriz[linha2][coluna2+1])
		arquivo.writelines(conteudo)
		arquivo.close()

	elif coluna1 == coluna2:
		arquivo = open(nomedoarquivoSaida, 'w')
		if linha1 + 1 == 5:
			linha1 = 0;
		if linha2 + 1 == 5:
			linha2 = 0;
		conteudo.append(matriz[linha1+1][coluna1])
		conteudo.append(matriz[linha2+1][coluna2])
		arquivo.writelines(conteudo)
		arquivo.close()
	else:
		arquivo = open(nomedoarquivoSaida, 'w')
		conteudo.append(matriz[linha1][coluna2])
		conteudo.append(matriz[linha2][coluna1])
		arquivo.writelines(conteudo)
		arquivo.close()
"""
FUNCAO PASSAPALAVRA
 - RECEBE UMA PALAVRA, VERIFICA SE EH IMPAR E SE SIM ADICIONA X NO FINAL, VERIFICA SE POSSUI 
 LETRAS REPETIDADES EM 1 PAR DE CARACTER E SE SIM ADICIONA X 
"""
def passapalavra(palavra,i,matriz,nomedoarquivoSaida):
	if i%2 != 0 :
		add = np.chararray(i+1)
		add[i] = "x"
	else:
		add = np.chararray(i)
	k = 0
	while k < i:
		add[k] =palavra[k]	
		k = k + 1	
	k = 0
	while k < i:
		if palavra[k] == palavra[k+1]:
			add[k+1] = "x"	
		k = k + 2	
	j = 0	
	while j < i:
		arquivo = open(nomedoarquivoSaida, 'r')
		procuramatriz(ord(add[j]),ord(add[j+1]),matriz,arquivo,nomedoarquivoSaida)
		j = j+2

#FUNCAO DE TRATAMENTO DE CARACTER DE ACORDO COM A TABELA ASCII
def tratamentoCaracter(line):
	#TRATAMENTO DE CARACTER ESPECIAL DA LETRA U	
	if ord(line) == 129 or ord(line) == 150 or ord(line) == 151 or ord(line) == 154 or ord(line) == 163 or ord(line) == 233 or ord(line) == 234 or ord(line) == 235:
		line = chr(117)
	#TRATAMENTO DE CARACTER ESPECIAL DA LETRA I	
	if ord(line) == 139 or ord(line) == 140 or ord(line) == 141 or ord(line) == 161 or ord(line) == 213 or ord(line) == 214 or ord(line) == 215 or ord(line) == 216:
		line = chr(105)
	#TRATAMENTO DE CARACTER ESPECIAL DA LETRA O	
	if ord(line) == 147 or ord(line) == 148 or ord(line) == 149 or ord(line) == 162 or ord(line) == 224 or ord(line) == 226 or ord(line) == 227 or ord(line) == 228 or ord(line) == 229 :
		line = chr(111)
	#TRATAMENTO DE CARACTER ESPECIAL DA LETRA E	
	if ord(line) == 130 or ord(line) == 136 or ord(line) == 137 or ord(line) == 138 or ord(line) == 144 or ord(line) == 210 or ord(line) == 211 or ord(line) == 212:
		line = chr(101)
	#TRATAMENTO DE CARACTER ESPECIAL DA LETRA A	
	if ord(line) >= 131 and ord(line) <= 134  or ord(line) == 198 or ord(line) == 199 or ord(line) == 160 or ord(line) == 181 or ord(line) == 182 or ord(line) == 183 or ord(line) == 198 or ord(line) == 199 :
		line = chr(97)
	#TRATAMENTO DE CARACTER ESPECIAL DA LETRA C	
	if ord(line) == 135 or ord(line) == 128:
		line = chr(99)
	#TRATAMENTO DE CARACTER MAIUSCULO	
	if ord(line) >= 65 and ord(line) <= 90:
		line = ord(line) + 32
		line = chr(line)
	if ord(line) >= 97 and ord(line) <= 122:
		return line
	


nomedoarquivoEntrada = raw_input("Digite o nome do arquivo .txt a ser criptografado: ")
nomedoarquivoSaida = raw_input("Digite o nome do arquivo .txt de saida: ")

"""
APOS FAZER A LEITURA DO ARQUIVO DE ENTRADA, EH PASSADO PALAVRAS PARA A FUNCAO PASSAPALAVRA
QUE EH RESPONSAVEL POR DAR CONTINUIDADE AO PROCESSO
"""
arquivo = open(nomedoarquivoEntrada, 'r')
unica_string = arquivo.read()
i = 0
ah = 0
palavra = np.chararray(50)
for line in unica_string:
	if line == " ":
		ah = 1		
	if ah == 0 :
		line = tratamentoCaracter(line)
		palavra[i] = line
		i = i + 1
	else:
		passapalavra(palavra,i,matriz,nomedoarquivoSaida)
		while i > 0:
			palavra[i] = "0"
			i = i - 1
		ah = 0	
if ah ==0:
	passapalavra(palavra,i,matriz,nomedoarquivoSaida)
arquivo.close()	
