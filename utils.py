import google.generativeai as genai

api_key = "AIzaSyA920dNYCD5GyHJ7Cce8fcGgC8KfxOrYqQ"

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def process_text(file):
    text = file.read().decode("utf-8")
    return text

def verify_news(text):
    prompt = f"""
Você é um verificador especialistade fake news. Leia a seguinte notícia:

{text}

Com base em dados disponíveis, fontes confiáveis e verificações de fatos:

1. Essa notícia é verdadeira ou falsa?
2. Dê uma estimativa da porcentagem de confiança (ex: 80% real ou 65% falsa).
3. Escreva um parágrafo explicando sua análise de forma clara e objetiva.

Use linguagem simples. Não invente fatos. Seja direto.
"""

    try:
        response = model.generate_content(prompt)
        gemini_response = response.text

        veredict = "Desconhecido"
        trust = "-"
        justification = gemini_response.strip()

        if "fals" in gemini_response.lower():
            veredict = "Falsa"
        elif "verdade" in gemini_response.lower() or "real" in gemini_response.lower():
            veredict = "Verdadeira"

        for line in gemini_response.split("\n"):
            if "%" in line:
                trust = line.strip()
                break

        return {
            "veredito": veredict,
            "confianca": trust,
            "justificativa": justification
        }

    except Exception as e:
        return {
            "veredito": "Erro",
            "confianca": "-",
            "justificativa": f"Erro ao verificar: {e}"
        }