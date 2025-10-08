import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Configuração da Página ---
# Define o título da página, ícone e layout. O layout 'wide' aproveita melhor o espaço da tela.
st.set_page_config(
    page_title="Cultura Oceânica e Clima",
    page_icon="🌊",
    layout="wide",
)

# --- Funções de Geração de Dados ---
# Para garantir que o aplicativo funcione sem depender de arquivos externos,
# vamos gerar dados de exemplo que simulam tendências reais.
def gerar_dados_temperatura(anos=(1980, 2024)):
    """Gera dados simulados da anomalia da temperatura da superfície do mar."""
    ano_inicio, ano_fim = anos
    anos_lista = np.arange(ano_inicio, ano_fim + 1)
    # Cria uma tendência de aquecimento com alguma variabilidade
    tendencia = np.linspace(0, 0.9, len(anos_lista))
    ruido = np.random.normal(0, 0.08, len(anos_lista))
    anomalia = tendencia + ruido
    df = pd.DataFrame({"Ano": anos_lista, "Anomalia de Temperatura (°C)": anomalia})
    return df

def gerar_dados_nivel_mar(anos=(1993, 2024)):
    """Gera dados simulados do aumento do nível do mar."""
    ano_inicio, ano_fim = anos
    anos_lista = np.arange(ano_inicio, ano_fim + 1)
    # Aumento médio de ~3.4 mm/ano, com variabilidade
    taxa_aumento_mm = 3.4
    aumento_total = (anos_lista - ano_inicio) * taxa_aumento_mm
    ruido = np.random.normal(0, 5, len(anos_lista))
    nivel_mar_mm = aumento_total + ruido
    df = pd.DataFrame({"Ano": anos_lista, "Variação do Nível do Mar (mm)": nivel_mar_mm})
    return df

# --- Título e Introdução ---
st.title("🌊 Aplicativo Educativo: Cultura Oceânica e o Clima")
st.markdown("""
Bem-vindo! Este aplicativo foi criado para explorar a **Cultura Oceânica** e entender como as **mudanças climáticas** estão impactando nossos oceanos.
Use as visualizações interativas abaixo para descobrir mais.
""")
st.markdown("---")


# --- Seção: Cultura Oceânica ---
st.header("O que é Cultura Oceânica?")
st.markdown("""
A Cultura Oceânica (ou Letramento Oceânico) é o entendimento da influência do oceano sobre nós e da nossa influência sobre o oceano.
Ela se baseia em 7 princípios fundamentais que nos ajudam a tomar decisões mais conscientes e responsáveis.
""")

# Usando um expander para não poluir a tela principal
with st.expander("Clique aqui para conhecer os 7 Princípios da Cultura Oceânica"):
    st.write("""
    - **Princípio 1:** A Terra tem um oceano, grande e único.
    - **Princípio 2:** O oceano e a vida no oceano modelam as feições da Terra.
    - **Princípio 3:** O oceano exerce uma grande influência sobre o tempo e o clima.
    - **Princípio 4:** O oceano torna a Terra habitável.
    - **Princípio 5:** O oceano sustenta uma imensa diversidade de vida e ecossistemas.
    - **Princípio 6:** O oceano e os seres humanos estão intrinsecamente conectados.
    - **Princípio 7:** O oceano é, em grande parte, inexplorado.
    """)
st.markdown("---")


# --- Seção: Visualização de Dados Climáticos ---
st.header("Analisando os Impactos das Mudanças Climáticas nos Oceanos")
st.write("Os gráficos abaixo usam dados simulados baseados em tendências observadas por agências como a NASA e a NOAA.")

# Dividindo a tela em duas colunas para os gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌡️ Aquecimento da Superfície do Mar")
    st.write("O oceano absorve a maior parte do calor extra gerado pelas emissões de gases de efeito estufa. Isso leva ao aumento da temperatura da água, o que afeta a vida marinha, como os corais, e intensifica eventos climáticos.")

    # Slider para selecionar o intervalo de anos
    anos_temperatura = st.slider(
        "Selecione o intervalo de anos para a temperatura do mar:",
        1980, 2024, (1980, 2024),
        key="slider_temp" # Chave única para o slider
    )

    # Gera e filtra os dados com base no slider
    dados_temp = gerar_dados_temperatura(anos=anos_temperatura)

    # Cria o gráfico com Plotly Express
    fig_temp = px.line(
        dados_temp,
        x="Ano",
        y="Anomalia de Temperatura (°C)",
        title="Anomalia da Temperatura da Superfície do Mar (1980-2024)",
        template="plotly_white",
        markers=True
    )
    fig_temp.update_layout(font_family="Arial", font_size=18)
    st.plotly_chart(fig_temp, use_container_width=True)

with col2:
    st.subheader("📈 Aumento do Nível do Mar")
    st.write("O aumento do nível do mar é causado principalmente por dois fatores relacionados ao aquecimento global: a expansão térmica da água (água quente ocupa mais espaço) e o derretimento de geleiras e mantos de gelo.")

    # Slider para selecionar o intervalo de anos
    anos_nivel_mar = st.slider(
        "Selecione o intervalo de anos para o nível do mar:",
        1993, 2024, (1993, 2024),
        key="slider_nivel" # Chave única para o slider
    )

    # Gera e filtra os dados com base no slider
    dados_nivel = gerar_dados_nivel_mar(anos=anos_nivel_mar)

    # Cria o gráfico com Plotly Express
    fig_nivel = px.line(
        dados_nivel,
        x="Ano",
        y="Variação do Nível do Mar (mm)",
        title="Variação do Nível Médio Global do Mar (1993-2024)",
        template="plotly_white",
        color_discrete_sequence=['#ef553b']
    )
    fig_nivel.update_layout(font_family="Arial", font_size=18)
    st.plotly_chart(fig_nivel, use_container_width=True)

st.markdown("---")

# --- Conclusão e Chamada para Ação ---
st.header("O que podemos fazer?")
st.markdown("""
A conscientização é o primeiro passo! Ao entender a conexão entre nossas ações, o clima e a saúde do oceano, podemos tomar decisões melhores no nosso dia a dia.
- **Reduza sua pegada de carbono:** Use transporte público, economize energia e consuma de forma consciente.
- **Apoie a conservação marinha:** Participe de limpezas de praia e apoie organizações que protegem o oceano.
- **Compartilhe conhecimento:** Converse com amigos e familiares sobre a importância dos oceanos!
""")

