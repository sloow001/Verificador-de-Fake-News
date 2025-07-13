# Verificador de Fake News com IA

🕵️‍♂️ Um app feito com Python e Streamlit que usa a API do Gemini para analisar notícias e dizer se são verdadeiras, falsas ou inconclusivas, com justificativa e nível de confiança.

---

## Sobre o projeto

Este projeto foi desenvolvido para **estudo e aprendizado**. Ele usa inteligência artificial para tentar verificar a veracidade de textos noticiosos, mas a IA pode se confundir ou gerar resultados não precisos em alguns casos. Use os resultados como um apoio, não como uma verdade absoluta.

---

## Tecnologias utilizadas

- **[Streamlit](https://streamlit.io/)**: para criar a interface web interativa de forma rápida e simples.
- **[Google Gemini API](https://aistudio.google.com/)**: modelo de linguagem utilizado para analisar e interpretar as notícias.

---

## Funcionalidades

- Entrada de texto manual ou upload de arquivo `.txt` com a notícia
- Análise automática com IA (Google Gemini)
- Veredito com emoji e cores para facilitar a leitura:
  - ✅ Verdadeira (verde)
  - ❌ Falsa (vermelho)
  - ⚠️ Inconclusiva (laranja)
- Justificativa detalhada e explicativa

---

## Como usar

### Requisitos

- Python 3.8 ou superior
- Biblioteca do Streamlit
- Chave de API do Google Gemini ([Crie aqui!](https://aistudio.google.com/app/apikey))

### Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/sloow001/Verificador-de-Fake-News
cd seu-repositorio
pip install -r requirements.txt
```

Abra o arquivo `utils.py` e mude a variável ```api_key``` para a sua chave

```
api_key = "SUA_CHAVE_AQUI"
```

### Rodando o app

```bash
streamlit run main.py
```

Abra o navegador no endereço que o Streamlit indicar (geralmente http://localhost:8501).

---

## Observações

- O projeto está em fase de testes e aprendizado. A IA pode gerar respostas incorretas ou inconclusivas.
- A qualidade do veredito depende da clareza da notícia e da base de conhecimento da IA.
- Sinta-se à vontade para contribuir, sugerir melhorias ou reportar problemas!
