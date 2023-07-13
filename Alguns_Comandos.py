VAR = 3.145
print(f"{VAR:.2f}")
palavra = 'python'
print(palavra[::-1])




'''SET'''
# Para removar elementos duplicados de uma lista, usa-se o comando 'set'.
tipo_set = {1,2,3,4} # Não podem ser acessados como as lista são acessadas, exemplo: tipo_set[0]  Não se pode fazer isso!
# Unindo dois set's
set1 = {1,2}
set2 = {3,4}
print(set1.union(set2))
# Atribuindo uma interseção entre dois set's
set1 = {1,2}
set2 = {2,3}
print(set1.intersection(set2))
# Atribuindo diferença entre dois set's
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.difference(set2)) # Retornará {1} O que tem em set1 que não tem em set2
print(set2.difference(set1)) # Retornará {4} O que tem em set2 que não tem em set1
# Atribuindo somente as diferenças
print(set1.symmetric_difference(set2)) # Retornará {1,4}
# Atribuindo se um set está contido em outro
conj1 = {1,2,3}
conj2 = {4,5,2,6,1,3,8}
print(conj1.issubset(conj2))
print(conj2.issubset(conj1))
# Ao contrário
print(conj1.issuperset(conj2))
print(conj1.issuperset(conj2))
# Adicionando elementos para dentro do set
set_add = {1,2,3,4}
set_add.add(13)
# Limpando valores do set
set_add.clear()
# Copiando valores do set
set_add.copy()
# Retirar um valor do set
conj = {1,2,3,4}
conj.discard(2)
# Retirando valor por valor
conj.pop() # Ele retira a partir da posição 0
# Remove
conj.remove(4)



arra = [1,2,1,3,1]
print(set(arra))

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0] )

print(list(range(10)))



'''LISTAS'''

lista_ = [1,2,3,4]

print(lista_[0:2])
print(lista_[0:3:2])
print(lista_[::])
print(lista_[::-1])

for indice, valores in enumerate(lista_):
    print(f'{indice} :{valores}')
print(id(lista_))

lista_.clear() # Limpa todos os valores da lista
lista_.copy() # Copia a lista

lis = ['vermelho','azul','verde','vermelho']
lis.count('vermelho') # Vai contar quantas vezes possui a palavra 'vermelho' na lista 'lis'
print(lista_.extend(lis)) # Adiciona os valores da lista 'lis' para a lista 'lista_'
lis.index('vermelho') # Retorna a posição da palavra 'vermelho' na lista 'lis'
lis.pop() # Remove 1 item da lista começando do final
lis.pop(0) # Remove 1 item que está na posição '0'
lis.remove('azul') # Remove o termo inserido
lis.reverse() # Altera a ordem da lista
lis.sort() # Ordena em ordem alfabética
lis.sort(reverse=True) # Ordena em ordem alfabética ao contrário
lis.sort(key=lambda x: len(x)) # Ordena do item com menor tamanho pro maior tamnho
lis.sort(key=lambda x: len(x), reverse=True) # Ordena do item com maior tamanho pro menor


'''Dicionários'''
dict1 = {'nome':'Calil','idade':22}
dict2 = dict(nome='Calil',idade=22)
print(dict2['nome']) # Mostrará o que está dentro da chave 'nome'
# Se quisermos adicionar um novo item ao dicionário
dict2['E-mail'] = 'ccmg@poli.br'

# Dicionários aninhados

Cadastro = {
    'calilcgomes@gmail.com':{"Nome":"Calil Cavalcante Muniz Gomes",
                             "Idade":22,
                             "Telefone":"81993638767"},
    'ccmg@poli.br':{"Nome":"Calil Cavalcante Muniz Gomes",
                             "Idade":22,
                             "Telefone":"81993638767"},
    'calil.gomes@upe.br':{"Nome":"Calil Cavalcante Muniz Gomes",
                             "Idade":22,
                             "Telefone":"81993638767"}
}

print(Cadastro['calil.gomes@upe.br']['Idade'])
# Como printar todos os itens
for chave in Cadastro:
    print(chave," ",Cadastro[chave])

for chave, valor in Cadastro.items():
    print(chave," ",valor)

# Limpando dicionários
dici = {'nome':'Calil',
        'idade':22}
dici.clear()
# Copiando dicionários
dici.copy()
dici = {'nome':'Calil',
        'idade':22}
# Método para excluir somente os valores das chaves
dici.fromkeys(['nome','telefone']) # Retira os valores das chaves e deixa os títulos
dici.fromkeys(['nome','telefone'],'Valor') # Coloca o item 'Valor' para as duas chaves do dicionário
# Get
print(dici.get('nome'))
# Items
dici.items()
# Pop
dici.pop('nome')
# Popitem
dici.popitem()
# Adicionando items dentro do dicionário
# Se adicionar um valor que já existe no dicionário, ele não fará nada
dici.setdefault("nome",'Calil') 
dici.setdefault("idade",22)
print(dici)

# Update

Cadastro: dict = {
    'calilcgomes@gmail.com':{"Nome":"Calil Cavalcante Muniz Gomes",
                             "Idade":22,
                             "Telefone":"81993638767"},
    'ccmg@poli.br':{"Nome":"Calil Cavalcante Muniz Gomes",
                             "Idade":22,
                             "Telefone":"81993638767"},
    'calil.gomes@upe.br':{"Nome":"Calil Cavalcante Muniz Gomes",
                             "Idade":22,
                             "Telefone":"81993638767"}
}

Cadastro.update({'ccmg@poli.br':{"Nome":"Calil"}}) # Na chave 'ccmg@poli.br', ele atualizará a chave para o novo parâmetros colocado na funão update, que é o  {'ccmg@poli.br':{"Nome":"Calil"}}

# Values
print(Cadastro.values())

# Verificação se uma chave existe ou não
print('ghg@gmail.com' in Cadastro) # Retornará False
print('ccmg@poli.br' in Cadastro) # Retornará True

# Removendo valores no dicionário
del Cadastro['ccmg@poli.br']['Nome'] # Remove apenas o telefone da chave ccmg@poli.br
del Cadastro['calil.gomes@upe.br'] # Remove tudo referente à chave calil.gomes@upe.br

# Funções
def Func1(*args) -> tuple:
    #text = "\n".join(args) # Vai separar por uma linha cada valor passado no argumento
    return args #text
print(Func1('oi','lápis'))


def kwargs(dat,*args,**kwargs):
    texto = '\n'.join(args)
    meta = '\n'.join([f'{chave.title()}:{valor}' for chave, valor in kwargs.items()])
    mensagem = f'{dat}\n\n{texto}\n\n{meta}'
    print(mensagem)

kwargs('2022','olá,olá','calil','idade')


# Positional only
# Todos os parâmetros declarados antes da '/' não precisam ser declarados
def criar_dict(modelo, ano,/,marca, motor)->dict:
    dicionario = {
        'Modelo':modelo,
        'Ano':ano,
        'Marca':marca,
        'Motor':motor
    }
    return dicionario
print(criar_dict('Esportivo','2022',marca='Fiat',motor='V6')) # Caso fosse declarado modelo='Esportivo' e ano='2022' iria dar erro
# Keyword only
# Os parêmetros declarados depois do * precisam terem seus nomes declarados quando o método/função for chamado
def criar_dict2(*,modelo, ano,marca, motor)->dict:
    dicionario = {
        'Modelo':modelo,
        'Ano':ano,
        'Marca':marca,
        'Motor':motor
    }
    return dicionario
print(criar_dict2(modelo='Esportivo',ano='2022',marca='Fiat',motor='V6')) 

#Keyword and positional only

def criar_dict3(modelo,/, ano,*,marca,motor)->dict:
    dicionario = {
        'Modelo':modelo,
        'Ano':ano,
        'Marca':marca,
        'Motor':motor
    }
    return dicionario
print(criar_dict3('Esportivo', ano='2022', marca='Fiat', motor='V6'))

# Usando uma função dentro de outra função
def soma(a,b):
    return a + b

def exibir(a,b,func):
    resultado = func(a,b)
    return resultado

print(exibir(2,3,soma))

# Usando a permissão de acesso 'global' para acessar variáveis de fora da função

num = 2000
def acrescentar(bonus):
    global num
    num = num + bonusr
    return num
acrescentar(412)