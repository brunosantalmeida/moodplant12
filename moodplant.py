from sentiment import analisar_sentimento
from weather import obter_clima
from database import carregar_estado, salvar_estado
from utils import mostrar_status, tempo_desde_ultima_visita
from datetime import datetime


def main():
    estado = carregar_estado()
    clima = obter_clima()

    print("🌿 Bem-vindo ao MoodPlant!")
    print(f"🕒 Última visita: {estado['ultima_visita']}")
    print(f"🌡️ Clima atual: {clima}")
    print(f"🪴 Status atual: {estado['humor']} - Saúde: {estado['saude']}%\n")

    tempo = tempo_desde_ultima_visita(estado['ultima_visita'])
    if tempo >= 2:
        print(f"😢 Você me deixou sozinho por {tempo} dias...")
        estado['saude'] = max(0, estado['saude'] - tempo * 10)

    msg = input("💬 Diga algo para sua planta: ")
    humor = analisar_sentimento(msg)

    if humor == 'positivo':
        print("😊 Amei o que você disse!")
        estado['humor'] = 'feliz'
        estado['saude'] = min(100, estado['saude'] + 5)
    elif humor == 'negativo':
        print("😡 Isso me deixou chateada...")
        estado['humor'] = 'triste'
        estado['saude'] = max(0, estado['saude'] - 5)
    else:
        print("😐 Hmmm... entendi.")
        estado['humor'] = 'neutra'

    estado['ultima_visita'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    salvar_estado(estado)
    mostrar_status(estado)


if __name__ == "__main__":
    main()
