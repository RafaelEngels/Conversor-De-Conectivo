import sys

def substituir_conectivos(sentenca):
    sentenca = sentenca.replace(" ", "")  
    while "↔" in sentenca:
        i = sentenca.find("↔")
        a = sentenca[i - 1]
        if sentenca[i - 1] == ")":
            j = i - 2
            par = 1
            while j >= 0 and par != 0:
                if sentenca[j] == ")":
                    par += 1
                elif sentenca[j] == "(":
                    par -= 1
                j -= 1
            a = sentenca[j + 1:i]
        b = sentenca[i + 1]
        if sentenca[i + 1] == "(":
            j = i + 2
            par = 1
            while j < len(sentenca) and par != 0:
                if sentenca[j] == "(":
                    par += 1
                elif sentenca[j] == ")":
                    par -= 1
                j += 1
            b = sentenca[i + 1:j]
        nova = f"((¬{a}∨{b})∧(¬{b}∨{a}))"
        sentenca = sentenca.replace(f"{a}↔{b}", nova)

    while "→" in sentenca:
        i = sentenca.find("→")
        a = sentenca[i - 1]
        if sentenca[i - 1] == ")":
            j = i - 2
            par = 1
            while j >= 0 and par != 0:
                if sentenca[j] == ")":
                    par += 1
                elif sentenca[j] == "(":
                    par -= 1
                j -= 1
            a = sentenca[j + 1:i]
        b = sentenca[i + 1]
        if sentenca[i + 1] == "(":
            j = i + 2
            par = 1
            while j < len(sentenca) and par != 0:
                if sentenca[j] == "(":
                    par += 1
                elif sentenca[j] == ")":
                    par -= 1
                j += 1
            b = sentenca[i + 1:j]
        nova = f"(¬{a}∨{b})"
        sentenca = sentenca.replace(f"{a}→{b}", nova)

    return sentenca



entrada = input("Digite a sentença lógica (ex: P→q→p) usando estes conectivos: ↔  → ")
resultado = substituir_conectivos(entrada)
print("Forma canônica:")
print(resultado)


acabouEagora = input("Digite 1 para digitar outra sentença e 2 para sair: ")

while acabouEagora != "2":  
    if acabouEagora == "1":
        entrada = input("Digite a sentença lógica (ex: P→q→p) usando estes conectivos: ↔  → ")
        resultado = substituir_conectivos(entrada)
        print("Forma canônica:")
        print(resultado)
        acabouEagora = input("Digite 1 para digitar outra sentença e 2 para sair: ")
    elif acabouEagora not in ["1", "2"]:
        print("Digite um valor válido")
        acabouEagora = input("Digite 1 para digitar outra sentença e 2 para sair: ")
    elif acabouEagora == "2":
        sys.exit()  

