a = 7
b = 3

def soma(x, y):
    return x + y

def main():
    resultado_soma = soma(a, b)
    print(f'{a} + {b} = {resultado_soma}')

# Chamando a função principal
if __name__ == "__main__":
    main()


def verificar_inicio(texto):
    if texto.startswith("Olá"):
        return "A frase começa com 'Olá'."
    else:
        return "A frase não começa com 'Olá'."

def main():
    try:
        # Abrindo e lendo o conteúdo do arquivo
        with open("verificar_inicio.txt", "r", encoding="utf-8") as arquivo:
            frase = arquivo.readline().strip()  # Lendo a primeira linha e removendo espaços extras
            resultado = verificar_inicio(frase)
            print(f"Frase encontrada: {frase}")
            print(resultado)
    except FileNotFoundError:
        print("O arquivo 'verificar_inicio.txt' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()



def soma_multiplos_de_tres(arquivo_nome):
    try:
        # Abrindo o arquivo
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            numeros = arquivo.readlines()  # Lendo todas as linhas do arquivo
        
        soma = 0
        for linha in numeros:
            try:
                numero = int(linha.strip())  # Convertendo cada linha para um número inteiro
                if numero % 3 == 0:  # Verificando se o número é múltiplo de 3
                    soma += numero
            except ValueError:
                print(f"Ignorando valor inválido no arquivo: {linha.strip()}")
        
        print(f"A soma dos números múltiplos de 3 é: {soma}")
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_nome}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chamando a função
nome_do_arquivo = "numeros.txt"
soma_multiplos_de_tres(nome_do_arquivo)

def criar_arquivo(nome_arquivo, conteudo):
    try:
        # Criando e escrevendo no arquivo
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
        print(f"O arquivo '{nome_arquivo}' foi criado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o arquivo: {e}")

# Solicitando informações ao usuário
nome_arquivo = input("Digite o nome do arquivo (com .txt no final): ")
conteudo = input("Digite o conteúdo que deseja escrever no arquivo: ")

# Chamando a função
criar_arquivo(nome_arquivo, conteudo)
