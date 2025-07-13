import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AIzaSyA920dNYCD5GyHJ7Cce8fcGgC8KfxOrYqQ"))
model = genai.GenerativeModel("gemini-1.5-flash")

def process_text(file):
    text = file.read().decode("utf-8")
    return text

def verify_news(texto):
    prompt = f"""
Você é um verificador especialistade fake news. Leia a seguinte notícia:

{texto}

Com base em dados disponíveis, fontes confiáveis e verificações de fatos:

1. Essa notícia é verdadeira ou falsa?
2. Dê uma estimativa da porcentagem de confiança (ex: 80% real ou 65% falsa).
3. Escreva um parágrafo explicando sua análise de forma clara e objetiva.

Use linguagem simples. Não invente fatos. Seja direto.
"""

    try:
        response = model.generate_content(prompt)
        resposta = response.text

        veredito = "Desconhecido"
        confianca = "-"
        justificativa = resposta.strip()

        if "fals" in resposta.lower():
            veredito = "Falsa"
        elif "verdade" in resposta.lower() or "real" in resposta.lower():
            veredito = "Verdadeira"

        for linha in resposta.split("\n"):
            if "%" in linha:
                confianca = linha.strip()
                break

        return {
            "veredito": veredito,
            "confianca": confianca,
            "justificativa": justificativa
        }

    except Exception as e:
        return {
            "veredito": "Erro",
            "confianca": "-",
            "justificativa": f"Erro ao verificar: {e}"
        }