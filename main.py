import streamlit as st
from utils import process_text, verify_news

st.set_page_config(page_title="🔎 Verificador de Fake News", layout="centered")
st.title("🕵️ Verificador de Fake News")

st.write("Coloque abaixo o texto da notícia que deseja verificar, ou envie um arquivo .txt contendo a notícia.")

texto_manual = st.text_area("Digite ou cole a notícia aqui:", height=200)

file = st.file_uploader("Ou envie um arquivo .txt:", type=["txt"])
final_text = ""

if file is not None:
    final_text = process_text(file)
elif texto_manual.strip() != "":
    final_text = texto_manual

if final_text:
    if st.button("Verificar notícia"):
        with st.spinner("Analisando..."):
            result = verify_news(final_text)

        st.subheader("🔎 Resultado")

        if result['veredito'] == "Verdadeira":
            st.markdown(f"<span style='color:green; font-size:20px;'>✅ <b>Veredito:</b> {result['veredito']}</span>", unsafe_allow_html=True)
        elif result['veredito'] == "Falsa":
            st.markdown(f"<span style='color:red; font-size:20px;'>❌ <b>Veredito:</b> {result['veredito']}</span>", unsafe_allow_html=True)
        elif result['veredito'] == "Inconclusiva":
            st.markdown(f"<span style='color:orange; font-size:20px;'>⚠️ <b>Veredito:</b> {result['veredito']}</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<b>Veredito:</b> {result['veredito']}", unsafe_allow_html=True)

        st.markdown(f"<b>Confiança:</b> {result['confianca']}", unsafe_allow_html=True)

        st.markdown(f"**Justificativa:**\n{result['justificativa']}")
else:
    st.info("Digite ou envie uma notícia para análise.")

st.markdown("Criado por [**Sloow**](https://github.com/sloow001)")
st.markdown("**Github do projeto** [aqui](https://github.com/sloow001/Verificador-de-Fake-News)!")