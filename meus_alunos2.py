# Cadastro simplificado de alunos 
# salva os dados em um arquivo texto

import os

def arquivo_existe(arquivo):
  if os.path.exists(arquivo):
    return True
  else:
    return False

def matricula_valida(matricula):
  for caractere in matricula:
    if not caractere.isdigit():
      return False
  return True

# Faz a leitura de todas as linhas do arquivo 
# e guarda os dados em um dicionario
def converte_conteudo_arquivo_para_dicionario():
  dicionario_alunos = dict()
  if arquivo_existe(arquivo='meus_alunos.txt'):
    arquivo_alunos = open('meus_alunos.txt', mode='r')
    # checa se existe pelo menos uma linha
    # cada linha tem a seguinte estrutura: matricula,nome,curso,sexo
    linhas = arquivo_alunos.readlines()
    if len(linhas) > 0:  
      for linha in linhas:
        aluno = linha.split(',')
        matricula = aluno[0]
        nome = aluno[1]
        curso = aluno[2]
        sexo = aluno[3]
        dicionario_alunos[matricula] = (nome, curso, sexo)
      arquivo_alunos.close()
  return dicionario_alunos

# Função para inserir um novo aluno
def inserir_aluno():
  matricula = input("Digite a matrícula do aluno: ")

  # Faz a validação da formatacao da matricula
  while not matricula_valida(matricula):
    print("A matrícula deve conter apenas números (0..9)")
    matricula = input("Digite a matrícula do aluno: ")

  # Checa se a matricula ja existe 
  alunos = converte_conteudo_arquivo_para_dicionario()
  while matricula in alunos: 
    print('Matrícula já existe!')
    matricula = input("Digite a matrícula do aluno: ")

  nome = input("Digite o nome do aluno: ")
  curso = input("Digite o curso do aluno: ")
  sexo = input("Digite o sexo do aluno [Masculino/Feminino] (M/F): ")

  # Validar sexo
  while sexo not in ("M", "F"):
    sexo = input("Sexo inválido. Digite M para masculino ou F para feminino: ")

  # Adicionar o aluno ao arquivo texto
  valores = [matricula, nome, curso, sexo]
  conteudo = ",".join(valores)
  arquivo_alunos = open('meus_alunos.txt', mode='a')
  conteudo = conteudo + '\n'
  arquivo_alunos.write(conteudo)
  arquivo_alunos.close()
  print("Aluno cadastrado com sucesso!")

# Função para listar todos os alunos
def listar_alunos():
  try: 
    if arquivo_existe(arquivo='meus_alunos.txt'):
      arquivo_alunos = open('meus_alunos.txt', mode='r')
      linhas = arquivo_alunos.readlines()
      if len(linhas) > 0:
        print("----------------------------------------")
        print("Lista de Alunos")
        print("----------------------------------------")
        for linha in linhas: 
          print(linha, end='')
      else:
        print("Nenhum aluno cadastrado.")
      arquivo_alunos.close()
    else:
      print('O arquivo ainda não foi criado!')
  except Exception as ex:
    print(f'Erro ao abrir o arquivo: {str(ex)}')
  
# Função para pesquisar aluno por matrícula
def pesquisar_aluno_matricula():
  matricula = input("Digite a matrícula do aluno a ser pesquisado: ")

  alunos = converte_conteudo_arquivo_para_dicionario()
  if matricula in alunos:
    dados_aluno = (matricula, alunos[matricula][0], alunos[matricula][1], alunos[matricula][2])
    print("----------------------------------------")
    print(f"Aluno encontrado:")
    print(f"Matrícula: {dados_aluno[0]}, Nome: {dados_aluno[1]}, Curso: {dados_aluno[2]}, Sexo: {dados_aluno[3]}")
    print("----------------------------------------")
  else:
    print("Aluno não encontrado.")

def menu_principal():
  print("#####################################")
  print("## Cadastro Simplificado de Alunos ##")
  print("#####################################")
  print("Opções:")
  print("1. Cadastrar aluno")
  print("2. Listar todos os alunos")
  print("3. Pesquisar aluno por matrícula")
  print("4. SAIR")

# Menu principal
while True:
  menu_principal()
  opcao = input("Qual sua opção? ")
  if opcao=='1':
    inserir_aluno()
  elif opcao=='2':
    listar_alunos()
  elif opcao=='3':
    pesquisar_aluno_matricula()
  elif opcao=='4':
    print("Programa encerrado.")
    break
  else:
    print("Opção inválida!")
