import csv
import random

# Definições para geração de imóveis fictícios
enderecos = [
    "Rua das Palmeiras, 123 - São Paulo",
    "Avenida Brasil, 456 - Rio de Janeiro",
    "Rua XV de Novembro, 789 - Curitiba",
    "Avenida Paulista, 101 - São Paulo",
    "Rua dos Andradas, 303 - Porto Alegre"
]
tipos_imovel = ["Apartamento", "Casa", "Cobertura", "Studio", "Sobrado"]

# Criando um arquivo CSV e alimentando com dados fictícios
arquivo_csv = "files/imoveis.csv"

with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Endereço", "Preço", "Quartos", 
                     "Banheiros", "Metragem", "Tipo"])

    for i in range(1, 21):  # Gera 20 imóveis fictícios
        endereco = random.choice(enderecos)
        preco = random.randint(200000, 2000000)  # Preço entre 200k e 2M
        quartos = random.randint(1, 5)
        banheiros = random.randint(1, 4)
        metragem = random.randint(40, 300)  # Metragem em m²
        tipo = random.choice(tipos_imovel)

        writer.writerow([i, endereco, preco, quartos, banheiros, 
                         metragem, tipo])

print(f"Arquivo {arquivo_csv} criado com sucesso!")