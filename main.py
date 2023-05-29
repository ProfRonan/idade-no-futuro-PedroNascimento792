def calculate_age(ano_atual, idade_atual, target_year):
    idade_futura = idade_atual + (target_year - ano_atual)
    return idade_futura

ano_atual = int(input("O ano atual: "))
idade_atual = int(input("Sua idade atual: "))
target_year = int(input("O ano que você quer calcular: "))
user_name = input("Seu nome: ")

idade_futura = calculate_age(ano_atual, idade_atual, target_year)

print(f"{user_name}, no ano de {target_year} você terá {idade_futura} anos.")
