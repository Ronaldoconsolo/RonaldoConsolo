import urllib.request
import json

def buscar_cotacao_dolar_oficial():
    print("🌐 O robô está consultando a API oficial de câmbio...")
    
    # URL da API pública estável que fornece dados em formato JSON (texto puro estruturado)
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    
    try:
        # Configura a requisição segura
        headers = {'User-Agent': 'Mozilla/5.0'}
        requisicao = urllib.request.Request(url, headers=headers)
        
        # Acessa e lê a resposta em formato JSON
        with urllib.request.urlopen(requisicao) as resposta:
            dados_brutos = resposta.read().decode('utf-8')
            
        print("🔍 Convertendo e estruturando os dados recebidos...")
        
        # Transforma o texto bruto em um dicionário do Python de forma limpa
        dados_ajustados = json.loads(dados_brutos)
        
        # Extrai a informação exata da cotação comercial
        preco_comercial = dados_ajustados["USDBRL"]["bid"]
        
        # Formata o número de texto para exibir no padrão brasileiro (ex: 5.05)
        valor_formatado = float(preco_comercial)
        
        print("\n=========================================")
        print(f"💵 DÓLAR COMERCIAL AO VIVO: R$ {valor_formatado:.2f}")
        print("=========================================\n")
            
    except Exception as erro:
        print(f"🚨 Houve um erro na conexão da API: {erro}")

if __name__ == "__main__":
    print("🚀 Iniciando o robô de extração de dados Inteligente...")
    buscar_cotacao_dolar_oficial()
    print("✨ Extração concluída com sucesso!")
