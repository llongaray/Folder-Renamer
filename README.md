# README.txt

## Descrição

Este script Python foi desenvolvido para renomear pastas dentro de um diretório, utilizando um **prefixo fornecido pelo usuário** seguido de um número extraído do final do nome de cada pasta. 

Por exemplo, se houver pastas com nomes como `capitulo-01`, `capitulo-02`, etc., o programa pode renomeá-las para algo como `Capítulo 1`, `Capítulo 2`, e assim por diante, dependendo do prefixo que o usuário escolher. O principal objetivo é organizar de forma consistente e automática pastas que seguem uma numeração no final de seus nomes.

Além disso, o script **salva um registro de todas as renomeações realizadas** em um arquivo de texto chamado `antes-e-depois.txt`, para que o usuário tenha uma referência das mudanças.

---

## Objetivo

O objetivo deste script é:

1. **Facilitar o processo de renomeação de pastas em massa**.
2. **Organizar pastas que possuem uma numeração no final de seus nomes**, permitindo que o usuário defina um prefixo personalizado.
3. **Armazenar um registro das renomeações feitas**, para que o usuário possa consultar quais nomes de pastas foram alterados.

Este tipo de renomeação pode ser útil em uma variedade de cenários, como a organização de capítulos de um livro, episódios de uma série, ou até arquivos de backup que seguem uma ordem numérica.

---

## Funcionamento

O programa segue as seguintes etapas:

1. **Entrada do caminho do diretório**: O usuário insere o caminho do diretório onde estão as pastas a serem renomeadas.
   
2. **Entrada do prefixo**: O usuário escolhe um prefixo que será usado antes dos números nas pastas renomeadas.

3. **Verificação do diretório**: O script verifica se o diretório informado existe. Caso o caminho não seja válido, o programa exibe uma mensagem de erro.

4. **Listagem das pastas**: O script lista todas as pastas no diretório e as organiza com base no número encontrado no final do nome de cada pasta.

5. **Renomeação das pastas**: Cada pasta que possui um número no final do nome é renomeada com o prefixo fornecido seguido do número. Exemplo:
   
   - Antes: `capitulo-01`
   - Depois: `Capítulo 1` (se o prefixo escolhido for "Capítulo")

6. **Registro das renomeações**: As mudanças são registradas em um arquivo de texto chamado `antes-e-depois.txt`, salvo no mesmo diretório onde as pastas foram renomeadas. Este arquivo contém a lista de todos os nomes antigos e novos.

7. **Loop de execução**: O programa continua pedindo novos diretórios e prefixos até que o usuário digite `exit` para sair.

---

## Uso

### 1. Pré-requisitos
- **Python 3**: Este script foi escrito em Python 3 e requer que esta versão (ou superior) esteja instalada em seu computador.

### 2. Execução

1. Abra um terminal ou prompt de comando.

2. Navegue até o diretório onde o script está salvo.

3. Execute o script com o comando:

    ```bash
    python nome_do_script.py
    ```

4. Insira o caminho do diretório que contém as pastas a serem renomeadas.

    - **Exemplo**: `/caminho/para/suas/pastas/`
    
5. Insira o prefixo que deseja adicionar antes do número de cada pasta.

    - **Exemplo**: Se você digitar `Capítulo`, as pastas serão renomeadas para algo como `Capítulo 1`, `Capítulo 2`, etc.

6. O programa renomeará as pastas conforme o prefixo fornecido e criará um arquivo `antes-e-depois.txt` contendo a lista de todas as renomeações realizadas.

7. Para encerrar o programa, digite `exit` quando solicitado a inserir o caminho de um diretório.

---

## Estrutura do Código

### Função `renomear_pastas(diretorio, prefixo)`
Essa função é responsável por todo o processo de renomeação. Aqui está o que ela faz:

1. **Recebe o diretório e o prefixo fornecido pelo usuário**.
2. **Verifica se o diretório existe**: Caso não exista, retorna uma mensagem de erro e interrompe a execução.
3. **Lista as pastas dentro do diretório**: Filtra apenas as que são realmente pastas e não arquivos.
4. **Organiza as pastas pelo número final**: Utiliza uma expressão regular (regex) para encontrar o número no final de cada nome de pasta.
5. **Renomeia as pastas**: Para cada pasta encontrada, o número final é mantido, mas um novo nome é gerado utilizando o prefixo escolhido.
6. **Salva as renomeações**: Um arquivo `antes-e-depois.txt` é criado no mesmo diretório, listando todas as mudanças realizadas.

### Função `main()`
Essa função cuida da interação com o usuário, pedindo o **caminho do diretório** e o **prefixo a ser usado**. Ela repete o processo até o usuário decidir encerrar o programa digitando `exit`.

---

## Exemplo

Suponha que você tenha o seguinte cenário de pastas no diretório `/meus/arquivos/`:

- `pasta-01`
- `pasta-02`
- `pasta-03`

Você executa o script, insere o caminho `/meus/arquivos/` e define o prefixo como `Capítulo`. O programa renomeia as pastas para:

- `Capítulo 1`
- `Capítulo 2`
- `Capítulo 3`

O arquivo `antes-e-depois.txt` conterá algo como:

```
Renomeações realizadas:
'pasta-01' -> 'Capítulo 1'
'pasta-02' -> 'Capítulo 2'
'pasta-03' -> 'Capítulo 3'
```

---

## Observações

- O script **não altera pastas que não tenham números no final do nome**.
- O programa é **sensível à formatação do nome**. Ele espera encontrar um número no final do nome da pasta para funcionar corretamente.
- É sempre bom **fazer um backup de suas pastas antes de usar o programa**, para evitar renomeações indesejadas.

---

## Melhorias Futuras

- Permitir a renomeação de arquivos, além de pastas.
- Adicionar uma opção de desfazer as renomeações, utilizando o arquivo `antes-e-depois.txt` como referência.
- Adicionar a opção de remover partes específicas do nome original da pasta, como prefixos antigos.

---

**Desenvolvido por: [llongaray77]**
