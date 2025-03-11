import requests

def obter_clima(cidade):
    chave_api = "74337f5de3cb4d4f8baf9b4eb8e6ca1e"
    url = f"https://api.weatherbit.io/v2.0/current?city={cidade}&key={chave_api}&lang=pt"

    resposta = requests.get(url)
    resposta.raise_for_status()  # Verifica se houve erro na requisição HTTP
    dados = resposta.json()

    if "data" in dados:
        clima = dados["data"][0]
        print(f"\nPrevisão do tempo para {cidade.capitalize()}:")
        print(f"Temperatura: {clima['temp']}°C")
        print(f"Clima: {clima['weather']['description']}")
    else:
        print("\nNão foi possível obter os dados para a cidade informada.")

def main():
    cidade = input("Digite o nome de uma cidade: ")
    obter_clima(cidade)

if __name__ == "__main__":
    main()
