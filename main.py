import requests
import time
from bs4 import BeautifulSoup

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

def obter_jogos_ao_vivo():
    url = "https://www.sofascore.com/pt/football/livescore"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Esse seletor pode mudar com o tempo; é o que está funcionando atualmente
    jogos = soup.select("div.event__match.event__match--live")

    alertados = set()  # evita alertar o mesmo jogo repetidamente

    for jogo in jogos:
        try:
            time_tag = jogo.select_one("div.event__stage--block")
            home_team = jogo.select_one("div.event__participant--home").text.strip()
            away_team = jogo.select_one("div.event__participant--away").text.strip()

            minuto = time_tag.text.strip() if time_tag else "Ao vivo"
            nome_jogo = f"{home_team} vs {away_team}"

            if nome_jogo not in alertados:
                send_alert("ao vivo", nome_jogo, "Análise básica", "1.30", minuto, "Jogo em andamento - análise em construção", "Média")
                alertados.add(nome_jogo)

        except Exception as e:
            print(f"Erro ao processar jogo: {e}")

def monitorar_jogos():
    while True:
        obter_jogos_ao_vivo()
        time.sleep(300)  # espera 5 min entre cada varredura

if __name__ == "__main__":
    monitorar_jogos()
