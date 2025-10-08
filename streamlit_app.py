import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime

# --- Configurações do Aplicativo Streamlit ---
st.set_page_config(
    page_title="Ocean & Clima App (Dados Abertos)",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Título Principal do App
st.title("🌊 OceanApp: Monitoramento Oceânico e Climático")
st.subheader("Visualizando Dados Abertos para Cultura Oceânica e Conscientização Climática")

# --- 1. Função de Coleta de Dados (Simulação de API de Dados Abertos) ---
# NOTA: Em um aplicativo real, você usaria sua própria chave API da OpenWeatherMap, Climatempo ou de um órgão governamental.
# A estrutura de dados JSON abaixo simula uma resposta de API de dados abertos de previsão horária.

def get_dados_climaticos_simulados(cidade):
    """
    Simula a obtenção de dados de previsão de tempo e maré de uma API pública.
    Os dados reais de temperatura e umidade são substituídos por valores de exemplo
    para garantir que o código funcione sem uma chave API real.
    """
    
    # Simulação de dados de 7 dias (horários)
    data_hoje = datetime.now().date()
    horas = pd.date_range(start=f'{data_hoje} 00:00', periods=48, freq='H') # 48 horas (2 dias)

    # Dados Simples (para o propósito do App) - Tente usar fontes de dados Abertos Brasileiras como INMET ou Marinha.
    dados = {
        'Data_Hora': horas,
        'Temperatura_C': [25, 26, 27, 26, 25, 24, 23, 22, 21, 22, 23, 24, 25, 26, 27, 28, 27, 26, 25, 24, 23, 22, 21, 20] * 2,
        'Umidade_Perc': [70, 68, 65, 66, 68, 72, 75, 78, 80, 75, 70, 65, 60, 58, 55, 53, 55, 58, 62, 68, 72, 75, 78, 80] * 2,
        'Velocidade_Vento_Nós': [5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 5, 7, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3] * 2,
        'Nivel_Maré_m': [0.5, 0.8, 1.2, 1.0, 0.6, 0.2, 0.1, 0.4, 0.9, 1.5, 1.3, 0.7, 0.4, 0.8, 1.3, 1.1, 0.7, 0.3, 0.2, 0.5, 1.0, 1.4, 1.2, 0.6] * 2
    }
    
    # Cria o DataFrame
    df = pd.DataFrame(dados)
    df['Data_Hora'] = pd.to_datetime(df['Data_Hora'])
    df = df.set_index('Data_Hora')
    
    return df

# --- 2. Interface do Usuário (Streamlit Sidebar) ---

with st.sidebar:
    st.header("Parâmetros de Pesquisa")
    cidade_selecionada = st.selectbox(
        "Selecione uma Cidade Costeira",
        ("Rio de Janeiro, RJ", "Florianópolis, SC", "Salvador, BA", "Recife, PE")
    )
    st.info(f"Dados abertos para **{cidade_selecionada}** (Simulação de API).")

# --- 3. Coleta e Processamento dos Dados ---

df_clima = get_dados_climaticos_simulados(cidade_selecionada)


# --- 4. Visualização dos Dados (Gráficos Reais Gerados a Partir dos Dados Abertos) ---

st.header(f"Previsão de 48 Horas para {cidade_selecionada}")

# Gráfico 1: Temperatura e Umidade (Clima)
st.markdown("### 🌡️ Temperatura e Umidade do Ar")
fig_temp = px.line(
    df_clima,
    y=['Temperatura_C', 'Umidade_Perc'],
    title='Variação de Temperatura e Umidade (48h)',
    labels={'value': 'Valor', 'Data_Hora': 'Data/Hora', 'variable': 'Variável'}
)
# Personalização do Plotly
fig_temp.update_layout(height=400, legend_title_text='Medidas')
fig_temp.update_traces(mode='lines+markers') # Adiciona marcadores para interatividade
st.plotly_chart(fig_temp, use_container_width=True)
st.caption("Fonte: Dados Climáticos Abertos (INMET/Simulação de API).")


st.markdown("---")

# Gráfico 2: Condições Oceânicas (Vento e Maré)
st.markdown("### 🌬️ Condições Oceânicas (Vento e Maré)")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Velocidade do Vento (Nós)")
    fig_vento = px.bar(
        df_clima,
        y='Velocidade_Vento_Nós',
        title='Velocidade do Vento',
        labels={'Velocidade_Vento_Nós': 'Vento (Nós)'}
    )
    fig_vento.update_layout(height=350)
    st.plotly_chart(fig_vento, use_container_width=True)

with col2:
    st.markdown("#### Nível da Maré (Metros)")
    fig_mare = px.area(
        df_clima,
        y='Nivel_Maré_m',
        title='Nível da Maré',
        labels={'Nivel_Maré_m': 'Maré (m)'}
    )
    fig_mare.update_layout(height=350)
    st.plotly_chart(fig_mare, use_container_width=True)
    
st.caption("Fonte: Dados Oceânicos Abertos (Marinha do Brasil/Simulação de API).")

st.markdown("---")

# --- 5. Componente de Cultura Oceânica ---

st.header("Educação e Cultura Oceânica")
st.info("""
**Por que isso importa?**
O oceano é um regulador fundamental do clima global, absorvendo calor e dióxido de carbono ($CO_2$).
Monitorar variáveis como a **temperatura** e o **nível da maré** em áreas costeiras é crucial para entender
os impactos da mudança climática na vida marinha e nas comunidades costeiras.
""")

st.write("A **cultura oceânica** promove a compreensão da influência do oceano sobre nós e nossa influência sobre o oceano.")
