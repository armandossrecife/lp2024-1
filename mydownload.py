import os
import platform
import requests
# Requests é um das bibliotecas mais usadas pela comunidade Python para fazer requisições HTTP
# Mais detalhes sobre HTTP em https://en.wikipedia.org/wiki/HTTP

plataforma = platform.system()

def limpa_tela():
    if plataforma != "Windows":
        os.system('clear')
    else:
        os.system('cls')

# Dada uma url e um local de arquivo (destination) faz o download do conteudo da url no arquivo
def download_file(url, destination):
    try:
        response = requests.get(url) # Faz a requisicao do arquivo 
        response.raise_for_status()  # Verifica se houve algum erro na requisição
        conteudo = response.content  # Guarda o conteudo binario da resposta da requisicao

        # Coloca o conteudo da requisicao em um arquivo local 
        # Cria um novo arquivo e insere o conteudo neste arquivo
        with open(destination, mode='wb') as file:
            file.write(conteudo)
        
        return True # Download realizado com sucesso
    except requests.exceptions.MissingSchema:
        # Caso seja uma excecao de url invalida
        print("URL inválida. Certifique-se de fornecer uma URL válida.")
        print("Download cancelado!")
        return False
    except requests.exceptions.ConnectionError:
        # Caso seja uma excecao de comunicacao de rede
        print(f"Erro na conexão!")
        print("Download cancelado!")
        return False
    except IOError: 
        # Caso aconteca um erro de IO do arquivo
        print(f"Arquivo {destination} inválido!")
        print("Download cancelado!")
        return False

# Exemplo 1 de uso (caminho feliz)
url = '://raw.githubusercontent.com/armandossrecife/teste/main/screen_matrix.jpeg'  # Insira a URL do arquivo desejado
destination = 'screen_matrix.jpeg'  # Insira o caminho de destino para salvar o arquivo
current_dir = os.getcwd() # Pega o path do diretorio corrente

if plataforma != 'Windows':
  path_arquivo_local = current_dir + "/" + destination
else:
  path_arquivo_local = current_dir + "\\" + destination

limpa_tela()
if download_file(url, destination):
    print(f"Download do arquivo {url}")
    print(f"Arquivo {destination} salvo em {path_arquivo_local}")
    print("Download realizado com sucesso!")
else:
    print("Download falhou!")
