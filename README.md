# Verificador de Fake News com IA

🕵️‍♂️ Um app feito com Python e Streamlit que usa a API do Gemini para analisar notícias e dizer se são verdadeiras, falsas ou inconclusivas, com justificativa e nível de confiança.

---

## Sobre o projeto

Este projeto foi desenvolvido para **estudo e aprendizado**. Ele usa inteligência artificial para tentar verificar a veracidade de textos noticiosos, mas a IA pode se confundir ou gerar resultados não precisos em alguns casos. Use os resultados como um apoio, não como uma verdade absoluta.

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
- Chave de API do Google Gemini (configure diretamente no código `utils.py`)

### Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz com sua chave:

```
GEMINI_API_KEY=SUA_CHAVE_DO_GEMINI
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

---

## Contato

Se quiser contribuir, dúvidas ou sugestões, abra uma issue no repositório.

---

**Divirta-se testando e aprendendo! 🚀**