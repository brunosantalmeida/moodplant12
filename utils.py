from datetime import datetime

def tempo_desde_ultima_visita(date_str):
    ultima = datetime.strptime(data_str,"%Y-%m-%d %H:%M:%S")
    agora = datetime.now()
    return (agora - ultima).days

def mostrar_status(estado):
    print("\n🌱 Estado Atual")
    print(f"humor: {estado['humor'].capitalize()}")
    print(f"saude: {estado['saude']}%\n")

