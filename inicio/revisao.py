import pprint

print("Hello, World!")
print("This is my first Python script.")
print("I am learning Python programming.")

# PythonFlix
name = "Top Gun: Maverick"

# Métodos de string
print("Top" in name)  # Verifica se "Top" está no nome do filme
print(name.lower())  # Converte o nome do filme para minúsculas
print(name.upper())  # Converte o nome do filme para maiúsculas
print(name.replace("Top", "Bottom"))  # Substitui "Top" por "Bottom" no nome do filme
print(name.split(":"))  # Divide o nome do filme em uma lista usando ":" como delimitador
print(name.center(30, '*'))  # Centraliza o nome do filme em uma string de 30 caracteres, preenchendo com '*'
print(name.strip())  # Remove espaços em branco do início e do fim do nome do filme
print(name.capitalize())  # Capitaliza o nome do filme (primeira letra maiúscula, resto minúsculo)
print(name.find("Maverick"))  # Encontra a posição da substring "Maverick" no nome do filme
print(name[:4])  # Acessa os primeiros 4 caracteres do nome do filme
print(name[4:])  # Acessa os caracteres do nome do filme a partir do índice 4
print(name[::2])  # Busca toda a string de 2 em 2
print(name[::-1])  # Inverte a string do nome do filme
print(name[1::2]) # Busca toda a string de 1 em 1, começando do segundo caractere


year = 2022
noteMovie = 8.5
planIncluded = True

#  Saber os tipos de dados
print("Tipo de dado do nome:", type(name))
print("Tipo de dado do ano:", type(year))
print("Tipo de dado da nota do filme:", type(noteMovie))
print("Tipo de dado do plano incluído:", type(planIncluded))

# Utilizando inputs 
# name = input("Please enter the movie name: ")
# year = int(input("Please enter the release year: "))
# noteMovie = float(input("Please enter the movie rating: "))
# planIncluded = input("Is the movie included in the plan? (yes/no): ").lower()[0] == 'y'
# print(f"""
#     Movie Details:
#     Name: {name}
#     Year: {year}
#     Rating: {noteMovie}
#     Included in Plan: {planIncluded}
# """)

# Operadores Aritméticos
a = 10
b = 5
# Soma
soma = a + b
# Subtração
subtracao = a - b
# Multiplicação
multiplicacao = a * b
# Divisão
divisao = a / b
# Módulo (resto da divisão)
modulo = a % b
# Exponenciação
exponenciacao = a ** b
# Divisão inteira
divisao_inteira = a // b
# Exibir resultados
print(f"""
Soma: {soma}
Subtração: {subtracao}
Multiplicação: {multiplicacao}
Divisão: {divisao}
Módulo: {modulo}
Exponenciação: {exponenciacao}
Divisão Inteira: {divisao_inteira}
""")

# Operadores de Comparação
bigger = a > b
smaller = a < b
equal = a == b
not_equal = a != b
greater_or_equal = a >= b
less_or_equal = a <= b

# Exibir resultados
print(f"""
{"==" * 20}
Bigger: {bigger}
Smaller: {smaller}
Equal: {equal}
Not Equal: {not_equal}
Greater or Equal: {greater_or_equal}
Less or Equal: {less_or_equal}
{"==" * 20}
""")

# Operadores Lógicos
and_operator = (a > 0) and (b > 0)
or_operator = (a > 0) or (b < 0)
not_operator = not (a < 0)

# Operadores Atribuição
a += 5  # a = a + 5
b -= 2  # b = b - 2
a *= 3  # c = c * 3
b /= 4  # d = d / 4

# Case Sensitivity exemplo
def case_sensitivity_example():
    var1 = "Hello"
    Var1 = "World"
    print(f"var1: {var1}, Var1: {Var1}")
case_sensitivity_example()

def exercicio():
    firstName = input("Digite seu primeiro nome: ")
    lastName = input("Digite seu sobrenome: ")
    print(f"{lastName}, {firstName}!")
    invertName= firstName[::-1]
    print(f"Nome invertido: {invertName}")
    isPalindrome = firstName.lower() == invertName.lower()
    if isPalindrome:
        print(f"{firstName} é um palíndromo!")
    else:
        print(f"{firstName} não é um palíndromo.")
# exercicio()


movieInfo = [name, year, noteMovie, planIncluded]
def print_movie_info(movie):
    print(f"Nome do Filme: {movie[0]}")
    print(f"Ano de Lançamento: {movie[1]}")
    print(f"Nota do Filme: {movie[2]}")
    print(f"Incluído no Plano: {'Sim' if movie[3] else 'Não'}")
print_movie_info(movieInfo)
movieList = [
    ["Top Gun: Maverick", 2022, 8.5, True],
    ["The Matrix Resurrections", 2021, 6.5, False],
    ["Inception", 2010, 8.8, True]
]

# Métodos de lista
print(f"primeiros filmes da lista: {movieList[:2]}")  # Pegar os 2 primeiros filmes da lista
print(f"últimos filmes da lista: {movieList[-2:]}")  # Pegar os 2 últimos filmes da lista
print (f"tamanho da lista: {len(movieList)}")  # Tamanho da lista
print(f"primeiro filme da lista: {movieList[0]}")  # Pegar o primeiro filme da lista
print(f"último filme da lista: {movieList[-1]}")  # Pegar o último filme da lista
movieList.append(["Interstellar", 2014, 8.6, True])
movieList.sort(key=lambda x: x[1])  # Ordenar por ano de lançamento 
copiedList = movieList.copy()
print(f"Lista copiada: {copiedList}")
print(f"Índice do filme 'Inception': {movieList.index(['Inception', 2010, 8.8, True])}") # Remover um filme da lista
movieList.remove(["The Matrix Resurrections", 2021, 6.5, False])
movieList.clear() # remover tudo da lista


# Tuplas
movieTuple = ("Top Gun: Maverick", 2022, 8.5, True)
def print_movie_tuple(movie):
    print(f"Nome do Filme: {movie[0]}")
    print(f"Ano de Lançamento: {movie[1]}")
    print(f"Nota do Filme: {movie[2]}")
    print(f"Incluído no Plano: {'Sim' if movie[3] else 'Não'}")

print_movie_tuple(movieTuple)
# Tupla x Lista: As tuplas são imutáveis, enquanto as listas são mutáveis.
print(movieTuple.count("Top Gun: Maverick"))  # Contar quantas vezes o filme aparece na tupla
print(movieTuple.index("Top Gun: Maverick"))  # Encontrar o índice do filme na tupla

# Sets
movieSet = {"Top Gun: Maverick", 2022, 8.5, True}
# def print_movie_set(movie):
#     # print(f"Nome do Filme: {movie[0]}")
#     print(f"Ano de Lançamento: {movie[1]}")
#     print(f"Nota do Filme: {movie[2]}")
#     print(f"Incluído no Plano: {'Sim' if movie[3] else 'Não'}")
# print_movie_set(movieSet)

# Tupla x Set: Os sets não permitem duplicatas, enquanto as tuplas permitem.
print(f"Set contém 'Top Gun: Maverick': {'Top Gun: Maverick' in movieSet}")
print(movieSet.add("Inception"))  # Adicionar um filme ao set
print(movieSet.remove("Top Gun: Maverick"))  # Remover um filme do set
print(movieSet.update({"Interstellar", 2014, 8.6, True}))  # Atualizar o set com novos filmes

# Dicionários
filmInfo = {
    "name": "Top Gun: Maverick",
    "year": 2022,
    "rating": 8.5,
    "included_in_plan": True
}
print(f"Nome do Filme: {filmInfo['name']} {filmInfo.get('name')}")
print(f"Ano de Lançamento: {filmInfo['year']}")
print(f"Nota do Filme: {filmInfo['rating']}")
filmInfo["director"] = "Joseph Kosinski"
print(filmInfo.items())  # Exibe todos os itens do dicionário
print(filmInfo.keys())  # Exibe todas as chaves do dicionário
filmInfo["name"] = "Top Gun: Maverick"
print(filmInfo.values())  # Exibe todos os valores do dicionário
#  Removendo o filme do dicionário
del filmInfo["name"] # Ou filmInfo.pop("name")
print(f"Diretor do Filme: {filmInfo['director']}")

# Dicionários x Listas: Os dicionários são usados para armazenar pares chave-valor, enquanto as listas são usadas para armazenar uma coleção ordenada de itens.
# Dicionários aninhados:
nested_dict = {
    "movie1": {
        "name": "Top Gun: Maverick",
        "year": 2022,
        "rating": 8.5,
        "included_in_plan": True
    },
    "movie2": {
        "name": "Inception",
        "year": 2010,
        "rating": 8.8,
        "included_in_plan": True
    }
}
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(nested_dict)

# Buscando um filme específico no dicionário aninhado
print(f"Nome do Filme 1: {nested_dict['movie1']['name']}")
print(f"Ano de Lançamento do Filme 1: {nested_dict['movie1']['year']}")

# Adicionando um novo filme ao dicionário aninhado
nested_dict["movie3"] = {
    "name": "Interstellar",
    "year": 2014,
    "rating": 8.6,
    "included_in_plan": True
}

#  Excluindo um filme do dicionário aninhado
del nested_dict["movie2"]


# Condicionais
if nested_dict["movie1"]["rating"] > 8.0:
    print(f"O filme {nested_dict['movie1']['name']} é altamente recomendado!")
elif nested_dict["movie1"]["rating"] > 7.0:
    print(f"O filme {nested_dict['movie1']['name']} é bom.")
else:
    print(f"O filme {nested_dict['movie1']['name']} não é tão bem avaliado.")
# Deixando o rating com 3 casas decimais
print(f"Rating do filme {nested_dict['movie1']['name']}: {nested_dict['movie1']['rating']:.3f}")


# Laços de repetição
for movie in nested_dict.values():
    print(f"Nome do Filme: {movie['name']}")
    print(f"Ano de Lançamento: {movie['year']}")
    print(f"Nota do Filme: {movie['rating']}")
    print(f"Incluído no Plano: {'Sim' if movie['included_in_plan'] else 'Não'}")
    print("-" * 20)

# Usando break e continue
for movie in nested_dict.values():
    if movie["rating"] < 8.0:
        continue  # Pula filmes com rating abaixo de 8.0
    print(f"Nome do Filme: {movie['name']}")
    print(f"Ano de Lançamento: {movie['year']}")
    print(f"Nota do Filme: {movie['rating']}")
    if movie["name"] == "Interstellar":
        break  # Interrompe o loop ao encontrar "Interstellar"
    print("-" * 20)

# Usando range
for i in range(1, 6):  # Loop de 1 a 5
    print(f"Contagem: {i}")

#  Usando while
count = 0
while count < 5:
    print(f"Contagem: {count}")
    count += 1  # Incrementa o contador

#  List Comprehensions
squared_numbers = [x**2 for x in range(10)]  # Cria uma lista com os quadrados dos números de 0 a 9
print(f"Números ao quadrado: {squared_numbers}")

# List Comprehensions x For Loop: List comprehensions são uma maneira mais concisa e eficiente de criar listas em comparação com loops for tradicionais.
# List Comprehensions com Condições
even_numbers = [x for x in range(10) if x % 2 == 0]  # Cria uma lista com os números pares de 0 a 9
print(f"Números pares: {even_numbers}")
# List Comprehensions usando listas aninhadas
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
flattened_list = [num for sublist in nested_list for num in sublist]  # Achata a lista aninhada em uma lista simples
print(f"Lista achatada: {flattened_list}")


# Funções
def greet_user(name):
    """Função para cumprimentar o usuário."""
    print(f"Olá, {name}! Bem-vindo ao curso de Python para Agentes Inteligentes.")
def calculate_area(radius):
    """Função para calcular a área de um círculo dado o raio."""
    import math
    area = math.pi * radius ** 2
    return area
def main():
    """Função principal do programa."""
    greet_user("Estudante")
    radius = float(input("Digite o raio do círculo: "))
    area = calculate_area(radius)
    print(calculate_area(radius))  # Exibe a área do círculo
    print(f"A área do círculo com raio {radius} é: {area:.2f}")
main()
def address(country="Brasil", state="SP", city="São Paulo"):
    """Função para exibir o endereço do usuário."""
    print(f"Endereço: {city}, {state}, {country}")
address()  # Chama a função com os valores padrão


def factorial(n):
    """Calcula o fatorial de um número."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

def totalSum(num):
    if num == 0:
        return 0
    else:
        return num + totalSum(num - 1)
    
# Args e Kwargs
# *args e **kwargs são usados para passar um número variável de argumentos para uma função. *args permite passar argumentos posicionais, enquanto **kwargs permite passar argumentos nomeados.
# Args são tuploas e Kwargs são dicionários.

def print_args(*args):
    """Função que aceita um número variável de argumentos."""
    print("Argumentos:", args)

def print_kwargs(**kwargs):
    """Função que aceita um número variável de argumentos nomeados."""
    print("Argumentos nomeados:", kwargs)

def presentation_courses(**kwargs):
    """Função que aceita um número variável de argumentos nomeados para cursos."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main_args_kwargs():
    """Função principal para demonstrar o uso de *args e **kwargs."""
    print_args(1, 2, 3, "Python", True)
    print_kwargs(name="João", age=30, city="São Paulo")
    presentation_courses(course1="Python", course2="Java", course3="JavaScript")
main_args_kwargs()


# Lambda Functions
def main_lambda():
    """Função principal para demonstrar o uso de funções lambda."""
    # Função lambda para calcular o quadrado de um número
    square_lambda = lambda x: x ** 2
    print(f"Quadrado de 5 usando função lambda: {square_lambda(5)}")
    
    # Função lambda para somar dois números
    add = lambda x, y: x + y
    print(f"Soma de 3 e 4 usando função lambda: {add(3, 4)}")
    isOdd = lambda x: x % 2 != 0
    print(f"É ímpar? {isOdd(3)}")

    sum = lambda a,b: a + b 
    print(f"Soma de 10 e 5 usando função lambda: {sum(10, 5)}")


movieList = [
    {"name": "Top Gun: Maverick", "year": 2022, "rating": 8.5, "included_in_plan": True},
    {"name": "Inception", "year": 2010, "rating": 8.8, "included_in_plan": True},
    {"name": "Interstellar", "year": 2014, "rating": 8.6, "included_in_plan": True}
]
def sort_movies_by_year(movies):
    """Ordena a lista de filmes pelo ano de lançamento."""
    return sorted(movies, key=lambda x: x["year"])
def main_sort_movies():
    """Função principal para demonstrar a ordenação de filmes."""
    sorted_movies = sort_movies_by_year(movieList)
    print("Filmes ordenados por ano de lançamento:")
    for movie in sorted_movies:
        print(f"{movie['name']} ({movie['year']}) - Rating: {movie['rating']} - Incluído no Plano: {'Sim' if movie['included_in_plan'] else 'Não'}")
    average_rating = lambda movie: sum(movie["rating"] for movie in movieList) / len(movieList)
    # Recomendar filmes com base na média de rating
    print(f"Média de rating dos filmes: {average_rating(movieList):.2f}")