'''
======================================================
Renomeador de Pastas em Ordem Numérica com Prefixo
======================================================
Desenvolvido por: Leonardo Longaray dos Santos (wangtianming)
Data: Outubro de 2024
Contato: llongaray77@gmail.com

Descrição:
Este programa renomeia pastas dentro de um diretório, utilizando um prefixo fornecido pelo usuário seguido de um número extraído do final do nome de cada pasta. Ele organiza as pastas em ordem numérica e armazena as renomeações realizadas em um arquivo de log.

Direitos Autorais (c) 2024 Leonardo Longaray dos Santos
Todos os direitos reservados.

Este código é fornecido "como está", sem garantias de qualquer tipo, expressas ou implícitas, incluindo, mas não se limitando, às garantias de comercialização e adequação a um propósito específico. O autor não será responsável por quaisquer danos decorrentes do uso deste código.

Licença:
Este código pode ser utilizado e modificado para fins pessoais ou educacionais. A redistribuição em forma original ou modificada só é permitida com a devida atribuição ao autor original.

======================================================
'''


import os  # Biblioteca para interagir com o sistema de arquivos (ler, escrever, renomear, etc.)
import re  # Biblioteca para trabalhar com expressões regulares (para encontrar padrões em strings)

# Função responsável por renomear as pastas no diretório dado
def renomear_pastas(diretorio, prefixo):
    # Mostra o caminho que foi recebido
    print(f"\nCaminho '{diretorio}' recebido!")
    
    '''
    Verifica se o caminho que o usuário digitou realmente existe no sistema.
    Se o diretório não for encontrado, o programa informa o erro e retorna (para de executar).
    '''
    if not os.path.isdir(diretorio):
        print("\nErro: O diretório não foi encontrado. Verifique o caminho e tente novamente.\n")
        return  # Sai da função caso o diretório não exista
    
    print("\nLendo nomes de pastas...\n")
    
    '''
    Lista todas as pastas dentro do diretório fornecido.
    "os.listdir()" lista todos os itens (arquivos e pastas).
    "os.path.isdir()" garante que estamos pegando apenas as pastas.
    '''
    pastas = [pasta for pasta in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, pasta))]
    
    # Mostra todas as pastas que foram encontradas
    print(f"Pastas encontradas: {pastas}\n")
    
    '''
    Aqui estamos criando uma expressão regular (regex) que irá procurar um número no final do nome de cada pasta.
    O "\d+" significa "um ou mais dígitos" e o "$" significa que o número deve estar no final do nome.
    '''
    regex = re.compile(r'(\d+)$')
    
    '''
    Ordena as pastas de acordo com o número no final de seus nomes.
    Para cada pasta, a função "regex.search()" busca o número no final.
    A função "int()" transforma esse número em inteiro para que a ordenação seja correta.
    Caso não haja número, ele coloca no final da lista usando "float('inf')" (infinito).
    '''
    pastas_ordenadas = sorted(pastas, key=lambda nome: int(regex.search(nome).group(1)) if regex.search(nome) else float('inf'))
    
    # Mostra as pastas já ordenadas com base no número no final do nome
    print(f"Pastas organizadas: {pastas_ordenadas}\n")
    
    '''
    Vamos usar este dicionário para guardar as renomeações.
    Para cada pasta renomeada, guardaremos o nome antigo e o novo nome.
    Isso será útil para o usuário ver o que mudou.
    '''
    renomeados = {}
    
    '''
    Agora vamos passar por cada pasta que foi organizada, uma por uma.
    O programa vai:
    1. Encontrar o número no nome da pasta.
    2. Renomear a pasta, usando o prefixo que o usuário forneceu.
    3. Armazenar essa mudança no dicionário "renomeados".
    '''
    for pasta in pastas_ordenadas:
        match = regex.search(pasta)  # Busca o número no final do nome da pasta
        if match:
            numero = match.group(1)  # Captura o número
            novo_nome = f"{prefixo} {numero}"  # Cria o novo nome usando o prefixo fornecido e o número
            
            # Define os caminhos antigo e novo da pasta
            caminho_antigo = os.path.join(diretorio, pasta)
            caminho_novo = os.path.join(diretorio, novo_nome)
            
            # Mostra a ação de renomear cada pasta
            print(f"Renomeando '{pasta}' para '{novo_nome}'...")
            
            # Renomeia a pasta no sistema de arquivos
            os.rename(caminho_antigo, caminho_novo)
            
            # Armazena no dicionário a relação de antes e depois
            renomeados[pasta] = novo_nome
    
    '''
    Após renomear, mostramos ao usuário todas as renomeações feitas.
    Usamos um loop para imprimir cada item do dicionário "renomeados".
    '''
    print("\nRenomeações realizadas:")
    for antes, depois in renomeados.items():
        print(f"'{antes}' -> '{depois}'")
    
    '''
    Agora vamos salvar essas renomeações em um arquivo de texto.
    O arquivo será chamado 'antes-e-depois.txt' e será salvo no mesmo diretório que as pastas.
    Ele listará o nome antigo e o novo nome de cada pasta.
    '''
    with open(os.path.join(diretorio, 'antes-e-depois.txt'), 'w') as arquivo:
        arquivo.write("Renomeações realizadas:\n")
        for antes, depois in renomeados.items():
            arquivo.write(f"'{antes}' -> '{depois}'\n")
    
    # Informa ao usuário que as renomeações foram salvas no arquivo
    print("\nRenomeações armazenadas em 'antes-e-depois.txt'\n")


# Função principal do programa
def main():
    while True:
        '''
        Aqui o programa pede ao usuário para inserir o caminho do diretório onde estão as pastas.
        O usuário pode também digitar 'exit' para encerrar o programa.
        '''
        caminho = input("\nPor favor, insira o caminho do diretório ou 'exit' para sair: ").strip()
        
        if caminho.lower() == 'exit':  # Se o usuário digitar 'exit', o programa para
            print("\nPrograma encerrado!\n")
            break  # Sai do loop e encerra o programa
        
        '''
        Após o caminho do diretório, o programa pergunta ao usuário qual prefixo ele quer usar.
        O prefixo será adicionado antes do número na renomeação das pastas.
        Exemplo: Se o prefixo for 'Capítulo', a pasta 'exemplo-06' vira 'Capítulo 06'.
        '''
        prefixo = input("\nPor favor, insira o prefixo a ser usado antes dos números (ex: 'Capítulo'): ").strip()
        
        # Chama a função que renomeia as pastas, passando o caminho e o prefixo fornecidos pelo usuário
        renomear_pastas(caminho, prefixo)

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Executa a função principal
