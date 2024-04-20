# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= INTERACTIVE HELP =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# Você pode pedir ajuda sobre a finalidade das funções e como elas funcionam, você precisa apenas
# ir para o python console e escrever 'help()', ai logo em seguida escreva a função cuja
# qual você tem duvidas, assim aparecendo a explicação.
# PS: Aqui no VSC você tem que digitar python no python console antes de todos os paçõs a cima

# A outra maneira de ver o docstring de uma função, que é usar o print na função
# que você quer junto com isso:
# print(input.__doc__)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= DOCSTRINGS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=


# O que cacetes são docstrings?
# É uma string de documentaçõa, ou seja, um manual explicando sobre uma função

# Toda função tem sua propria string, mas sabendo que nós mesmos podemos fazer funções, surge outra dúvida
# Nossas funções tem instruções de como usa-las?
# Não, se você fazer uma função e usar o help para ela, tera pouquissimas informações,
# pórem, você pode fazer uma docstring para sua função

# Como faço a docstring da minha função?
# É simples, você colocoa 3 aspás duplas, dá 'enter', escreve as instruições da sua função
# e fecha tudo com 3 aspás duplas


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ARGUMENTOS OPCIONAIS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# É usado para dar alguns argumentos opcionais, caso não se tenha garantia que tudo será respondido
# Para ficar mais didático vamo usar de exemplo a função soma:
def soma(a,b,c):
    s = a + b + c
    print(f'A soma é igual a {s}')
soma(1,2,3)

# Ela é usada para somar 3 números, poré se forem colocados somente 2 números, ela ira dar erro
# mas usando um argumento opcional, isso se resolve dessa meneira
def soma(a,b,c=0):
    s = a + b + c
    print(f'A soma é igual a {s}')
soma(1,2,3)

# Agora ela pode somar tanto 3 números, quanto somente 2
# E para deixar ela mais limpa(creio eu), nesse caso é só colocar todas as váriaveis iguais a 0
def soma(a=0,b=0,c=0):
    s = a + b + c
    print(f'A soma é igual a {s}')
soma(1,2,3)

# Agora ao invés de dar erro caso nenhum número for informado, ela vai dar resultado 0


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ESCOPO DE VÁRIAVEIS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# Escopo Global: É quando

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= RETORNO DE RESULTADOS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
