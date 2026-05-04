from colorama import Fore, Style, init

print("\n"+"-"*30)
print("Controle de Níveis de Água")
print("-"*30)

mensagens = [
    ("Nível 1", "Muito baixo (crítico)", Fore.RED),
    ("Nível 2", "Baixo", Fore.YELLOW),
    ("Nível 3", "Médio", Fore.GREEN),
    ("Nível 4", "Alto", Fore.CYAN),
    ("Nível 5", "Muito alto (alerta)", Fore.BLUE)
]

def exibir_mensagem(nivel):
    if 1 <= nivel <= 5:
        prefixo, situacao, cor = mensagens[nivel - 1]
        print(prefixo + " = " + cor + situacao + Style.RESET_ALL)
    else:
        print("Nível inválido")

for i in range(1, 6):
    exibir_mensagem(i)

nivel_atual = 4
print("\nSituação atual do reservatório: ")
exibir_mensagem(nivel_atual)