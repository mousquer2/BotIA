import requests
import time

TOKEN = "8164137561:AAElTmHu2JuSsktc2CVOXpAkUwFboOz4YVQ"
CHANNEL_ID = "@Mestreia_bot"

def send_alert(tipo, jogo, mercado, odd, hora, detalhes, confianca):
    mensagem = f"""
ALERTA {tipo.upper()}

Jogo: {jogo}
Mercado: {mercado}
Odds: {odd}
Hora: {hora}
{detalhes}
Confiança: {confianca}
"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": mensagem
    }
    requests.post(url, data=payload)

# Simulador de alertas (depois trocaremos por dados ao vivo)
def gerar_alertas():
    while True:
        send_alert("pré-jogo", "Salzburg vs LASK", "Over 1.5 gols", "1.40", "16:00",
                   "Média de 3.2 gols/jogo | 80% over 1.5 nos últimos 5 jogos", "Alta")
        time.sleep(10)

        send_alert("ao vivo", "Genk vs Club Brugge", "Over 0.5 HT", "1.28", "1T - 18min",
                   "9 chutes, 3 no alvo, 2 escanteios | Alta pressão ofensiva", "Média-Alta")
        time.sleep(300)

if __name__ == "__main__":
    gerar_alertas()
