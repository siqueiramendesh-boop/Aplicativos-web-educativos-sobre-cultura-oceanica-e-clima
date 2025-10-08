import streamlit as st

# Configuração da página (deve ser o primeiro comando Streamlit)
st.set_page_config(
    page_title="Cultura Oceânica e Clima",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título e introdução
st.title("Explorando a Conexão entre Oceano e Clima")

st.markdown("""
Bem-vindo à nossa aplicação educativa interativa!

Esta ferramenta foi projetada para explorar a profunda relação entre a saúde dos oceanos,
as mudanças climáticas e o conceito de **Cultura Oceânica**.

A Cultura Oceânica é a compreensão da influência do oceano sobre nós e da nossa influência sobre o oceano.

**👈 Navegue pelas páginas na barra lateral** para descobrir visualizações de dados, métricas e os princípios fundamentais que conectam a humanidade ao nosso planeta azul.
""")

st.divider()

st.header("Como usar esta aplicação")
st.info("""
- **Indicadores Climáticos Globais:** Explore dados em escala planetária, como anomalias de temperatura e elevação do nível do mar.
- **Métricas de Saúde Oceânica:** Mergulhe em dados locais, visualizando informações de estações de monitoramento na costa brasileira.
- **Princípios da Cultura Oceânica:** Aprenda sobre os sete princípios essenciais que formam a base para uma relação sustentável com o oceano.
""")

# Adicione uma imagem de banner se desejar.
# st.image("path/to/your/banner_image.jpg", caption="A imensidão da Amazônia Azul")
