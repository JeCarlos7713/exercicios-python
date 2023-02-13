# 11.1 - Um dicionário é um mapeamento
# Estrutura de dados que armazena chave e valor

#Criando dicionario com a função dict
dicionario = dict()

#Adicionando chave e valor ao dicionario
dicionario['a'] = "Teste"


#Criando dicionario com chaves e valores
dicionario_de_livros = {
    "livro1" : "Percy Jackson",
    "livro2" : "Jogos Vorazes",
    "Livro3" : "Pense em python",
    "livro5" : ""
}

print (dicionario_de_livros)

# Acessando valores do dicionário
print(dicionario_de_livros["livro1"])

#Erro ao não encontrar chave
print(dicionario_de_livros["livro4"])

#print(dicionario_de_livros.get())

#a função len obtém os números de chaves e valores existentes no dict
print(len(dicionario_de_livros))

#visualizando se tem alguma chave específica no dict
print("livro2" in dicionario_de_livros)

#values busca todos os valores do dict
valor_dicionario_livros = dicionario_de_livros.values()
print(valor_dicionario_livros)

#verificando se há um valor específico usando values e in
print('Percy Jackson' in valor_dicionario_livros)


#11.2 - Um dicionário como uma coleção de contadores

def histogram(string):
    d = dict() #monta um dicionário vazio
    for c in string: #se o caractere c não estiver no dicionario, cria o item com 1, se não incrementa com o valor já adicionado
        if c not in d:
            #print('String quebrada: ', c)
            d[c]=1
        else:
            d[c] += 1
    return d

nome_flamengo = histogram('Flamengo Campeão')

print(nome_flamengo)

#função usando .get() do python, que busca um valor da chave, e se não encontrar, retorna um valor padrão referenciado a ele
#sintaxe: dict.get('chave', 'valor_padrao')
# Onde dicionario é o nome do dicionário, chave é a chave que desejamos procurar no dicionário e valor_padrao é o valor que será retornado caso a chave não exista no dicionário.
#não precisamos de if else, pois o valor padrão é apresentado caso não encontre a chave, sem dar o keyError
#função com o .get, sem precisar do if else

def new_histogram(string):
    d = dict()
    for a in string:
        #print('String quebrada: ', a)
        d[a] = d.get(a, 0) + 1
    return d

novo_nome = new_histogram('Paleontólogo')

print(novo_nome)


# 11.3 - Loop e dicionários

#o for percorre cada chave e valor do dicionário, exemplo a função a seguir:

def print_hist(h):
    for c in sorted(h): #usar sorted para atravessar as chaves em ascendente
        print(c, h[c])

phrase_print = histogram('zoka')

print_hist(phrase_print)

#11.4 - Busca reversa