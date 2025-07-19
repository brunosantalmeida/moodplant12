import requests

API_KEY = "SUA_API_KEY"
CIDADE = "Rio de Janeiro"

def obter_clima():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&lang=pt_br&units=metric"
    try:
        resposta = requests.get(url).json()
        return resposta['westher'][0]['description']
    except:
        return "Indefinido"