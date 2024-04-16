import requests

def download_file(url, destination):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na requisição

        with open(destination, 'wb') as file:
            file.write(response.content)

        print(f"Download completo. Arquivo salvo em: {destination}")
    except requests.exceptions.MissingSchema:
        print("URL inválida. Certifique-se de fornecer uma URL válida.")
    except requests.exceptions.RequestException as e:
        print(f"Erro na conexão: {e}")

# Exemplo 1 de uso (caminho feliz)
url = 'https://raw.githubusercontent.com/armandossrecife/teste/main/screen_matrix.jpeg'  # Insira a URL do arquivo desejado
destination = 'screen_matrix.jpeg'  # Insira o caminho de destino para salvar o arquivo

download_file(url, destination)
