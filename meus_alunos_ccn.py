import os
import requests

# Ler os dados do arquivo alunos_ccn.csv e mostra o conteudo
def mostra_dados_alunos_ccn_arquivo(nome_arquivo):
    f_alunos_ccn = open(nome_arquivo, mode='r')
    conteudo = f_alunos_ccn.read()
    print(conteudo)
    f_alunos_ccn.close()

def mostra_dados_alunos_ccn_dicionario(dicionario):
    for matricula, dados in dicionario.items():
        nome = dados[0]
        curso = dados[1]
        print(matricula, nome, curso)

# Ler os dados do arquivo alunos_ccn.csv e guarda em um dicionario
def carrega_dados_no_dicionario(nome_arquivo):
    dict_alunos_ccn_aux = {}
    f_alunos_ccn = open(nome_arquivo, mode='r')
    for linha in f_alunos_ccn:
        #cada linha tem: matricula,nome,curso
        linha_corrente = linha.split(',')
        matricula = linha_corrente[0]
        nome = linha_corrente[1]
        curso = linha_corrente[2]
        # Remove o caractere especial \n
        curso = curso.strip()
        dict_alunos_ccn_aux[matricula] = (nome, curso)
    f_alunos_ccn.close()
    # Remove o 1o item do dicionario
    del dict_alunos_ccn_aux['Matrícula']
    return dict_alunos_ccn_aux

def mostra_alunos_do_curso(dicionario, nome_curso):
    for matricula, dados in dicionario.items():
        nome = dados[0]
        curso = dados[1]
        if curso == nome_curso.upper():
            print(matricula, nome, curso)
        else: 
            print(f"Curso {nome_curso.upper()} não localizado!")

def pesquisa_aluno(dicionario, matricula):
    if matricula in dicionario:
        return dicionario[matricula]
    else:
        return None

def consulta_aluno_por_matricula(dicionario_alunos):
    entrada_matricula = input('Qual a sua matrícula? ')
    aluno_procurado = pesquisa_aluno(dicionario=dicionario_alunos, matricula=entrada_matricula)
    if aluno_procurado:
        nome = aluno_procurado[0]
        curso = aluno_procurado[1]
        print(f"Resuldo da busca pela matrícula {entrada_matricula}")
        print(f"nome: {nome}, curso: {curso}")
    else: 
        print(f"O aluno de matricula {entrada_matricula} não foi encontrado!")

def carrega_arquivo_internet(url, filename):    
    response = requests.get(url)
    if response.status_code == 200:
        text_content = response.text
        with open(filename, "w") as file:
            file.write(text_content)
        print(f"O download do arquivo {filename} foi realizado com sucesso!")
    else:
        print(f"O download falhou!. Status code: {response.status_code}")

# Chamada do sistema operacional para limpar a tela
os.system("clear")

arquivo_principal = "alunos_ccn.csv"

print("Faz o download do arquivo da Internet")
url_arquivo = "https://github.com/armandossrecife/lp2024-1/raw/main/alunos_ccn.csv"
carrega_arquivo_internet(url=url_arquivo, filename=arquivo_principal)

print(f"Carrega os dados do arquivo {arquivo_principal} na memória")
dict_alunos_ccn = carrega_dados_no_dicionario(arquivo_principal)
print("Dados carregados com sucesso! ")
print("Obs: o arquivo contem apenas alunos dos cursos Computação, Matemática, Física, Química e Biologia do CCN/UFPI")
consulta_aluno_por_matricula(dict_alunos_ccn)

# Proximas questoes: 
# Quantos alunos de computação aparecem nesse arquivo? 
# Liste apenas os alunos de computação e matemática
# Liste apenas os alunos que tenham o nome Maria
# Liste apenas os alunos que tem Maria no primeiro nome
