import streamlit as st
from utils import process_text, verify_news

st.set_page_config(page_title="🔎 Verificador de Fake News", layout="centered")
st.title("🕵️ Verificador de Fake News")

st.write("Coloque abaixo o texto da notícia que deseja verificar, ou envie um arquivo .txt contendo a notícia.")

texto_manual = st.text_area("Digite ou cole a notícia aqui:", height=200)

arquivo = st.file_uploader("Ou envie um arquivo .txt:", type=["txt"])
texto_final = ""

if arquivo is not None:
    texto_final = process_text(arquivo)
elif texto_manual.strip() != "":
    texto_final = texto_manual

if texto_final:
    if st.button("Verificar notícia"):
        with st.spinner("Analisando..."):
            resultado = verify_news(texto_final)

        st.subheader("🔎 Resultado")

        if resultado['veredito'] == "Verdadeira":
            st.markdown(f"<span style='color:green; font-size:20px;'>✅ <b>Veredito:</b> {resultado['veredito']}</span>", unsafe_allow_html=True)
        elif resultado['veredito'] == "Falsa":
            st.markdown(f"<span style='color:red; font-size:20px;'>❌ <b>Veredito:</b> {resultado['veredito']}</span>", unsafe_allow_html=True)
        elif resultado['veredito'] == "Inconclusiva":
            st.markdown(f"<span style='color:orange; font-size:20px;'>⚠️ <b>Veredito:</b> {resultado['veredito']}</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<b>Veredito:</b> {resultado['veredito']}", unsafe_allow_html=True)

        st.markdown(f"<b>Confiança:</b> {resultado['confianca']}", unsafe_allow_html=True)

        st.markdown(f"**Justificativa:**\n{resultado['justificativa']}")
else:
    st.info("Digite ou envie uma notícia para análise.")

st.markdown("**Github do projeto** [aqui](https://google.com)!")