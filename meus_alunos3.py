import os
import platform

plataforma = platform.system()

def limpar_tela():
  if plataforma != "Windows":
    os.system("clear")
  else:
    os.system('cls')

def arquivo_existe(nome_arquivo):
  if os.path.exists(nome_arquivo):
    return True
  else:
    return False

# Função para ler os dados de alunos de um arquivo e carregá-los em um dicionário
# nome_arquivo: nome do arquivo 
def carregar_alunos(nome_arquivo):
  alunos = dict()
  if arquivo_existe(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
      for line in file:
        matricula, nome, curso, sexo = line.strip().split(',')
        alunos[matricula] = (nome, curso, sexo)
    return alunos
  else:
    return dict()

# Função para salvar os dados dos alunos em um arquivo
# alunos: dicionario contendo os dados de todos os alunos do arquivo
# nome_arquivo: nome do arquivo 
def salvar_alunos(alunos, nome_arquivo):
  with open(nome_arquivo, 'w') as file:
    for matricula, dados in alunos.items():
      nome, curso, sexo = dados
      file.write(f"{matricula},{nome},{curso},{sexo}\n")

# Função para validar a formatação da matrícula
# matricula: chave do aluno
def matricula_valida(matricula):
  for caractere in matricula:
    if not caractere.isdigit():
      return False
  return True

# Função para inserir um novo aluno
# nome_arquivo: nome do arquivo 
# alunos: dicionario contendo os dados de todos os alunos do arquivo
def inserir_aluno(nome_arquivo, alunos):
  matricula = input("Digite a matrícula do aluno: ")

  # Validação da formatação da matrícula
  while not matricula_valida(matricula):
    print("A matrícula deve conter apenas números (0..9)")
    matricula = input("Digite a matrícula do aluno: ")

  # Checa se a matrícula já existe
  while matricula in alunos:
    print('Matrícula já existe!')
    matricula = input("Digite a matrícula do aluno: ")

  nome = input("Digite o nome do aluno: ")
  curso = input("Digite o curso do aluno: ")
  sexo = input("Digite o sexo do aluno [Masculino/Feminino] (M/F): ")

  # Validar sexo
  while sexo not in ("M", "F"):
    sexo = input("Sexo inválido. Digite M para masculino ou F para feminino: ")

  with open(nome_arquivo, 'a') as file:
    file.write(f"{matricula},{nome},{curso},{sexo}\n")
  print("Aluno cadastrado com sucesso!")

# Função para listar todos os alunos
# alunos: dicionario contendo os dados de todos os alunos do arquivo
def listar_alunos(alunos):
  if alunos:
    print("----------------------------------------")
    print("Lista de Alunos")
    print("----------------------------------------")
    for matricula, info in alunos.items():
      print(
          f"Matrícula: {matricula}, Nome: {info[0]}, Curso: {info[1]}, Sexo: {info[2]}"
      )
  else:
    print("Nenhum aluno cadastrado.")

# Função para pesquisar aluno por matrícula
# alunos: dicionario contendo os dados de todos os alunos do arquivo
def pesquisar_aluno_matricula(alunos):
  matricula = input("Digite a matrícula do aluno a ser pesquisado: ")

  if matricula in alunos:
    dados_aluno = alunos[matricula]
    print("----------------------------------------")
    print(f"Aluno encontrado:")
    print(
        f"Matrícula: {matricula}, Nome: {dados_aluno[0]}, Curso: {dados_aluno[1]}, Sexo: {dados_aluno[2]}"
    )
    print("----------------------------------------")
  else:
    print("Aluno não encontrado.")

# Função para pesquisar aluno por nome
# alunos: dicionario contendo os dados de todos os alunos do arquivo
def pesquisar_aluno_nome(alunos):
  nome = input("Digite o nome do aluno a ser pesquisado: ")

  alunos_encontrados = []
  for matricula, info in alunos.items():
    if nome.lower() in info[0].lower():
      alunos_encontrados.append((matricula, *info))

  if alunos_encontrados:
    print("----------------------------------------")
    print(f"Alunos encontrados com o nome '{nome}':")
    print("----------------------------------------")
    for aluno in alunos_encontrados:
      print(
          f"Matrícula: {aluno[0]}, Nome: {aluno[1]}, Curso: {aluno[2]}, Sexo: {aluno[3]}"
      )
  else:
    print("Aluno não encontrado.")

# Função para atualizar dados de um aluno existente
# alunos: dicionario contendo os dados de todos os alunos do arquivo
# nome_arquivo: nome do arquivo 
def atualiza_aluno(alunos, nome_arquivo):
  matricula = input("Digite a matrícula do aluno: ")

  if matricula in alunos:
    print('--- Dados do aluno ---')
    print(
        f"Matrícula: {matricula}, Nome: {alunos[matricula][0]}, Curso: {alunos[matricula][1]}, Sexo: {alunos[matricula][2]}"
    )
    print('--- Informe os novos dados --')
    nome = input("Digite o novo nome do aluno: ")
    curso = alunos[matricula][1]
    sexo = input("Digite o sexo do aluno [Masculino/Feminino] (M/F): ")

    # Atualizar os dados do aluno no dicionário
    alunos[matricula] = (nome, curso, sexo)
    salvar_alunos(alunos, nome_arquivo)
    print("Aluno atualizado com sucesso!")
  else:
    print("Matrícula não existe!")

# Função para remover um aluno
# alunos: dicionario contendo os dados de todos os alunos do arquivo
# nome_arquivo: nome do arquivo 
def remover_aluno(alunos, nome_arquivo):
  matricula = input("Digite a matrícula do aluno a ser removido: ")

  if matricula in alunos:
    del alunos[matricula]
    salvar_alunos(alunos, nome_arquivo)
    print("Aluno removido com sucesso!")
  else:
    print("Aluno não encontrado.")

# Função para exibir o menu principal
def menu_principal():
  print("#####################################")
  print("## Cadastro Simplificado de Alunos ##")
  print("#####################################")
  print("Opções:")
  print("1. Cadastrar aluno")
  print("2. Listar todos os alunos")
  print("3. Pesquisar por matrícula")
  print("4. Pesquisar por nome")
  print("5. Atualizar aluno")
  print("6. Remover aluno")
  print("7. SAIR")

limpar_tela()
arquivo = "alunos.txt"
while True:
  alunos = carregar_alunos(arquivo)
  menu_principal()
  opcao = input('Qual a sua opção? ')
  if opcao == '1':
    inserir_aluno(arquivo, alunos)
  elif opcao == '2':
    listar_alunos(alunos)
  elif opcao == '3':
    pesquisar_aluno_matricula(alunos)
  elif opcao == '4':
    pesquisar_aluno_nome(alunos)
  elif opcao == '5':
    atualiza_aluno(alunos, arquivo)
  elif opcao == '6':
    remover_aluno(alunos, arquivo)
  elif opcao == '7':
    break
  else:
    print('Opção inválida!')
