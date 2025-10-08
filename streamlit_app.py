import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- Configurações da Página ---
st.set_page_config(
    page_title="OceanApp Brasil: Cultura Oceânica e Clima",
    layout="wide",
    initial_sidebar_state="collapsed", # Colapsa a barra lateral, focando no conteúdo principal
)

# Título Principal
st.title("🌊 OceanApp Brasil: Cultura Oceânica e Clima")
st.subheader("Análise de Tendências, Previsão e Conscientização para o Litoral Brasileiro")
st.markdown("---")


# --- 1. Função de Simulação de Dados para Gráficos ---
# NOTA: Esta função simula dados de Tendência Climática de 10 anos e Maré de 2 dias.
# EM UMA APLICAÇÃO REAL: Substitua esta função por chamadas a APIs Abertas (ex: INMET, Marinha do Brasil, NOAA).
def get_dados_simulados():
    """Simula dados de tendências de 10 anos e previsão de 48h para demonstração."""
    
    # 1. Dados de Tendência Climática (10 anos)
    anos = pd.date_range(start='2015-01-01', periods=10, freq='Y')
    tendencia_data = {
        'Ano': anos,
        'Temp_Media_Anual_C': [25.0, 25.2, 25.4, 25.1, 25.3, 25.6, 25.8, 26.0, 26.2, 26.5],
        'Nivel_Medio_Mar_cm': [10.0, 10.5, 11.0, 11.2, 11.5, 11.9, 12.3, 12.8, 13.3, 14.0],
    }
    df_tendencia = pd.DataFrame(tendencia_data)
    df_tendencia['Ano'] = df_tendencia['Ano'].dt.year

    # 2. Dados de Previsão de Maré (48 horas)
    data_hoje = datetime.now().date()
    horas = pd.date_range(start=f'{data_hoje} 00:00', periods=48, freq='H') 
    mare_data = {
        'Data_Hora': horas,
        'Nivel_Maré_m': [0.5, 0.8, 1.2, 1.0, 0.6, 0.2, 0.1, 0.4, 0.9, 1.5, 1.3, 0.7, 0.4, 0.8, 1.3, 1.1, 0.7, 0.3, 0.2, 0.5, 1.0, 1.4, 1.2, 0.6] * 2,
    }
    df_mare = pd.DataFrame(mare_data).set_index('Data_Hora')
    
    return df_tendencia, df_mare

df_tendencia, df_mare = get_dados_simulados()


# --- 2. Definição dos Tópicos Explicativos (Cultura Oceânica e Clima) ---
TOPICOS = [
    {
        "titulo": "1. Aumento do Nível do Mar",
        "causas": "Degelo de calotas polares e **expansão térmica** da água (causada pelo aquecimento).",
        "influencia": "Afeta a costa brasileira (8.500 km), ameaçando infraestrutura e ecossistemas como **manguezais**.",
        "consequencias": "**Erosão costeira**, inundações frequentes e salinização da água potável subterrânea.",
        "dica": "Apoiar a adaptação costeira e usar dados de **altimetria** (satélites) para monitoramento local.",
    },
    {
        "titulo": "2. Acidificação Oceânica",
        "causas": "Absorção de **dióxido de carbono ($CO_2$)** emitido pela queima de combustíveis e **desmatamento** no Brasil.",
        "influencia": "Diminui o pH da água, dificultando a vida de organismos com conchas e esqueletos.",
        "consequencias": "Risco à **aquicultura** (criação de ostras e moluscos) e danos aos recifes de corais brasileiros.",
        "dica": "Reduzir a **pegada de carbono** individual e apoiar a restauração de biomas como a **Mata Atlântica**.",
    },
    {
        "titulo": "3. Eventos Climáticos Extremos",
        "causas": "Alterações nos padrões de circulação oceânica e atmosférica (ex: **El Niño** e **La Niña**).",
        "influencia": "Causa **secas prolongadas** no Nordeste e **chuvas torrenciais** e inundações no Sul e Sudeste.",
        "consequencias": "Deslizamentos de terra, perdas agrícolas, e danos severos a portos e comunidades costeiras.",
        "dica": "Consultar previsões de tempo e maré do **INMET** e da **Marinha do Brasil** para planejamento e segurança.",
    },
    {
        "titulo": "4. Branqueamento de Corais",
        "causas": "**Aumento da temperatura da água** (estresse térmico), que expulsa as algas simbióticas (que dão cor e vida).",
        "influencia": "Impacta recifes cruciais para o turismo e a pesca, como os do **Parque Nacional de Abrolhos** (BA).",
        "consequencias": "Morte de corais, perda de biodiversidade marinha e redução da proteção natural contra ondas fortes.",
        "dica": "Apoiar a conservação marinha e usar protetores solares *reef safe* (seguros para recifes).",
    },
    {
        "titulo": "5. Poluição Marinha por Plástico",
        "causas": "Gestão ineficaz de resíduos sólidos em **cidades costeiras** e descarte em rios (que levam ao mar).",
        "influencia": "Grandes rios brasileiros atuam como canais de transporte de resíduos para o oceano.",
        "consequencias": "Ingestão e sufocamento da **fauna marinha** (tartarugas, peixes) e contaminação por **microplásticos**.",
        "dica": "Aplicar os 3 R's (**Reduzir, Reutilizar, Reciclar**) e participar ativamente de mutirões de limpeza de praias.",
    },
]

# --- 3. Layout com Abas para Navegação em Local Único ---

tab_graficos, tab_analise = st.tabs(["📊 Gráficos de Dados Abertos", "💡 Análise e Conscientização (Causas e Dicas)"])

# =================================================================
# ABA 1: GRÁFICOS DE DADOS ABERTOS
# =================================================================
with tab_graficos:
    st.header("1. Tendências Climáticas (10 Anos)")
    st.info("Visualização de dados abertos (Simulados) mostrando tendências cruciais para o Brasil.")
    
    col_temp, col_nivel = st.columns(2)

    with col_temp:
        # GRÁFICO 1: TEMPERATURA
        fig_temp_decada = px.line(
            df_tendencia,
            x='Ano',
            y='Temp_Media_Anual_C',
            title='Tendência de Temperatura Média Anual (°C)',
            labels={'Temp_Media_Anual_C': 'Temperatura Média Anual (°C)'},
            markers=True
        )
        st.plotly_chart(fig_temp_decada, use_container_width=True)

    with col_nivel:
        # GRÁFICO 2: NÍVEL DO MAR
        fig_nivel_decada = px.bar(
            df_tendencia,
            x='Ano',
            y='Nivel_Medio_Mar_cm',
            title='Tendência de Aumento do Nível Médio do Mar (cm)',
            labels={'Nivel_Medio_Mar_cm': 'Aumento do Nível (cm)'}
        )
        st.plotly_chart(fig_nivel_decada, use_container_width=True)

    st.markdown("---")
    
    st.header("2. Previsão de Maré (48 Horas)")
    st.info("Dado essencial para a segurança costeira, portos, pesca e planejamento de atividades na praia.")

    # GRÁFICO 3: MARÉ
    fig_mare = px.area(
        df_mare,
        y='Nivel_Maré_m',
        title='Variação do Nível da Maré em 48 Horas (Metros)',
        labels={'Nivel_Maré_m': 'Nível da Maré (m)', 'Data_Hora': 'Data e Hora'},
        line_shape='spline'
    )
    fig_mare.update_layout(height=500)
    st.plotly_chart(fig_mare, use_container_width=True)
    
    st.caption("**Fonte dos Dados:** Dados Climáticos e Oceanográficos Abertos (Simulação baseada em APIs públicas).")

# =================================================================
# ABA 2: ANÁLISE DETALHADA E CULTURA OCEÂNICA
# =================================================================
with tab_analise:
    st.header("Análise Detalhada dos Tópicos - Cultura Oceânica em Ação")
    st.markdown("""
        O Brasil possui uma costa vasta e vulnerável. A **Cultura Oceânica** é a chave para a adaptação e mitigação.
        Entenda o impacto de cada fator e saiba como você pode influenciar positivamente.
    """)

    # Exibição dos Tópicos em colunas
    for i, topico in enumerate(TOPICOS):
        st.markdown(f"### {topico['titulo']}")
        st.markdown("---")
        
        col_causas, col_cons, col_dica = st.columns([1, 1, 1])

        with col_causas:
            st.markdown(f"**Causas e O que Influencia (Causa Raiz):**")
            st.write(f"👉 {topico['causas']}")
        
        with col_cons:
            st.markdown(f"**Consequências no Brasil (Impacto):**")
            st.warning(f"⚠️ {topico['consequencias']}")
        
        with col_dica:
            st.markdown(f"**Ação de Cultura Oceânica (Dica/Solução):**")
            st.success(f"✅ {topico['dica']}")
        
        if i < len(TOPICOS) - 1:
            st.markdown("---")
