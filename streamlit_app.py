import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

# --- Configurações da Página ---
st.set_page_config(
    page_title="OceanApp Brasil: Cultura Oceânica e Clima",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("🌊 OceanApp Brasil: Cultura Oceânica e Clima (Dados Abertos e Conscientização)")
st.subheader("Análise Integrada de Fontes Governamentais e Científicas Brasileiras")
st.markdown("---")


# ⚠️ FUNÇÕES DE INTEGRAÇÃO DE DADOS REAIS (TEMPLATE)
# 
# NOTA: Para usar dados 100% reais, substitua o conteúdo das funções 
# @st.cache_data pela sua lógica de chamada de API/leitura de CSV.
# O framework Streamlit (@st.cache_data) garante performance.

@st.cache_data
def get_dados_clima():
    """Simula dados de Temperatura (INMET) e Vento (OpenWeatherMap)."""
    # 📢 INMET (Temperatura Média Anual - 10 Anos)
    anos = pd.date_range(start='2015-01-01', periods=10, freq='Y')
    df_tendencia = pd.DataFrame({
        'Ano': anos.year,
        'Temp_Media_Anual_C': [25.0, 25.2, 25.4, 25.1, 25.3, 25.6, 25.8, 26.0, 26.2, 26.5],
    })
    
    # 📢 OpenWeatherMap (Vento Diário - 7 dias)
    dias = pd.date_range(start=datetime.now(), periods=7, freq='D')
    df_vento = pd.DataFrame({
        'Dia': dias.strftime('%a, %d/%m'),
        'Velocidade_Vento_Nós': [10, 12, 8, 9, 15, 11, 7],
    })
    return df_tendencia, df_vento

@st.cache_data
def get_dados_risco():
    """Simula dados de Nível do Mar (NOAA) e Deslizamento (CEMADEN)."""
    # 📢 NOAA (Nível do Mar - 30 Anos)
    anos_nivel = pd.date_range(start='1990-01-01', periods=30, freq='Y')
    df_nivel_longo = pd.DataFrame({
        'Ano': anos_nivel.year,
        'Nivel_Medio_Mar_cm': 10 + np.cumsum(np.random.rand(30) * 0.2 + 0.1), 
    })

    # 📢 CEMADEN (Alerta de Deslizamento - Simulação por Estado)
    df_risco = pd.DataFrame({
        'Estado': ['RJ', 'SP', 'ES', 'BA', 'PE', 'SC'],
        'Alertas_Recentes': [35, 28, 15, 10, 5, 20], 
    }).sort_values('Alertas_Recentes', ascending=False)
    
    return df_nivel_longo, df_risco

@st.cache_data
def get_dados_mare_e_bio():
    """Simula dados de Marinha do Brasil (Maré) e SiBBr (Biodiversidade)."""
    # 📢 Marinha do Brasil (Previsão de Maré - 48 horas)
    horas = pd.date_range(start=datetime.now(), periods=48, freq='H') 
    df_mare = pd.DataFrame({
        'Data_Hora': horas,
        'Nivel_Maré_m': [0.5, 0.8, 1.2, 1.0, 0.6, 0.2, 0.1, 0.4, 0.9, 1.5, 1.3, 0.7, 0.4, 0.8, 1.3, 1.1, 0.7, 0.3, 0.2, 0.5, 1.0, 1.4, 1.2, 0.6] * 2,
    }).set_index('Data_Hora')

    # 📢 SiBBr (Ocorrências de Branqueamento de Corais por Ano)
    anos_corais = pd.date_range(start='2018-01-01', periods=8, freq='Y')
    df_corais = pd.DataFrame({
        'Ano': anos_corais.year,
        'Ocorrencias_Branqueamento': [5, 3, 10, 7, 15, 12, 18, 20], 
    })
    return df_mare, df_corais

# Chama as funções de dados
df_tendencia, df_vento = get_dados_clima()
df_nivel_longo, df_risco = get_dados_risco()
df_mare, df_corais = get_dados_mare_e_bio()


# --- 2. Tópicos de Cultura Oceânica (Explicitação) ---
TOPICOS = [
    {
        "titulo": "1. Aumento do Nível do Mar",
        "causas": "Degelo das calotas polares e **expansão térmica** da água (aquecimento global).",
        "influencia": "Afeta os 8.500 km da costa brasileira, ameaçando cidades e ilhas costeiras.",
        "consequencias": "Aceleração da **erosão costeira**, inundações frequentes e salinização da água potável subterrânea.",
        "dica": "Apoiar planos municipais de adaptação e exigir infraestrutura resiliente em áreas costeiras.",
    },
    {
        "titulo": "2. Acidificação Oceânica",
        "causas": "O oceano absorve cerca de 30% do **dióxido de carbono ($CO_2$)** liberado, diminuindo seu pH.",
        "influencia": "Diretamente ligada às emissões brasileiras (principalmente **desmatamento** e transporte).",
        "consequencias": "Dificuldade de organismos como corais, ostras e mariscos em formar conchas e esqueletos. Risco à **aquicultura**.",
        "dica": "Reduzir o consumo de carne bovina (grande causa do desmatamento) e apoiar energias renováveis.",
    },
    {
        "titulo": "3. Eventos Climáticos Extremos",
        "causas": "Alterações nos padrões de circulação oceânica e atmosférica (**El Niño** e **La Niña**).",
        "influencia": "Intensifica as **secas prolongadas** no Nordeste e as **chuvas torrenciais** e deslizamentos no Sul/Sudeste do Brasil.",
        "consequencias": "Deslizamentos de terra em encostas litorâneas, perdas na pesca artesanal e danos à infraestrutura portuária.",
        "dica": "Consultar a previsão de tempo e maré da **Marinha/INMET** e participar de sistemas de alerta comunitário (CEMADEN).",
    },
    {
        "titulo": "4. Branqueamento de Corais",
        "causas": "Aumento rápido da **Temperatura da Superfície do Mar (TSM)**, que expulsa as algas simbióticas dos corais (estresse térmico).",
        "influencia": "Afeta os recifes de corais, como os de **Abrolhos** (BA), que são berçários de vida marinha e importantes para o turismo.",
        "consequencias": "Morte dos corais, perda de habitat para peixes e invertebrados, e redução da proteção costeira contra o impacto das ondas.",
        "dica": "Apoiar financeiramente projetos de monitoramento de corais e usar protetores solares *reef safe* (sem oxibenzona).",
    },
    {
        "titulo": "5. Poluição Marinha por Plástico",
        "causas": "Gestão inadequada de resíduos sólidos em **cidades costeiras** e o descarte ilegal em rios que desaguam no mar.",
        "influencia": "Grandes rios como o Amazonas e a Baía de Guanabara são canais de transporte de resíduos para o oceano.",
        "consequencias": "Ingestão e sufocamento da **fauna marinha** (tartarugas, aves) e contaminação por **microplásticos** na cadeia alimentar.",
        "dica": "Praticar os 3 R's (**Reduzir, Reutilizar, Reciclar**) e participar de mutirões de limpeza de praia (ações de cidadania oceânica).",
    },
    {
        "titulo": "6. Impacto na Pesca Artesanal",
        "causas": "Mudança nas rotas migratórias dos peixes devido à **temperatura da água** e alterações nas correntes marinhas.",
        "influencia": "Prejudica a principal fonte de renda e subsistência de comunidades pesqueiras tradicionais brasileiras.",
        "consequencias": "Diminuição do estoque pesqueiro, insegurança alimentar e êxodo das comunidades costeiras.",
        "dica": "Apoiar a **pesca sustentável** e consumir peixes certificados que não estejam em risco de extinção.",
    },
]


# --- 3. LAYOUT UNIFICADO COM ABAS (Gráficos e Pesquisa em um só lugar) ---

tab_graficos, tab_analise = st.tabs(["📊 Gráficos de Dados Abertos e Tendências", "💡 Análise e Conscientização no Brasil"])

# =================================================================
# ABA 1: GRÁFICOS DE DADOS ABERTOS
# =================================================================
with tab_graficos:
    st.header("1. Tendências Climáticas (INMET / NOAA)")
    st.info("Visualizações de longo prazo que evidenciam o aquecimento e a subida do nível do mar.")
    col_temp, col_nivel = st.columns(2)
    with col_temp:
        fig_temp = px.line(df_tendencia, x='Ano', y='Temp_Media_Anual_C', title='Temperatura Média Anual (°C) - (INMET)', 
                           labels={'Temp_Media_Anual_C': 'Temp. Média Anual (°C)'}, markers=True, height=300)
        st.plotly_chart(fig_temp, use_container_width=True)
    with col_nivel:
        fig_nivel = px.line(df_nivel_longo, x='Ano', y='Nivel_Medio_Mar_cm', title='Aumento Histórico do Nível do Mar (cm) - (NOAA)', 
                            labels={'Nivel_Medio_Mar_cm': 'Nível Relativo (cm)'}, line_shape='spline', height=300)
        st.plotly_chart(fig_nivel, use_container_width=True)

    st.markdown("---")
    
    st.header("2. Previsão e Risco (Marinha do Brasil / CEMADEN)")
    st.info("Dados operacionais cruciais para segurança e alerta de desastres.")
    col_mare, col_risco = st.columns(2)
    with col_mare:
        st.markdown("#### Previsão de Nível da Maré (Marinha do Brasil)")
        fig_mare = px.area(df_mare.reset_index(), x='Data_Hora', y='Nivel_Maré_m', title='Variação da Maré em 48 Horas', 
                            labels={'Nivel_Maré_m': 'Maré (m)', 'Data_Hora': 'Data e Hora'}, height=300)
        st.plotly_chart(fig_mare, use_container_width=True)
    with col_risco:
        st.markdown("#### Alertas de Risco Geológico (CEMADEN)")
        fig_risco = px.bar(df_risco, x='Estado', y='Alertas_Recentes', title='Alertas de Deslizamentos Recentes (Exemplo)', 
                           labels={'Alertas_Recentes': 'Nº de Alertas'}, color_discrete_sequence=['#FF4B4B'], height=300)
        st.plotly_chart(fig_risco, use_container_width=True)

    st.markdown("---")
    
    st.header("3. Biodiversidade e Clima (SiBBr / OpenWeatherMap)")
    st.info("Impactos diretos nos ecossistemas marinhos e padrões de vento.")
    col_corais, col_vento_bio = st.columns(2)
    with col_corais:
        fig_corais = px.bar(df_corais, x='Ano', y='Ocorrencias_Branqueamento', title='Ocorrências de Branqueamento de Corais (SiBBr)', 
                            labels={'Ocorrencias_Branqueamento': 'Nº de Ocorrências'}, height=300)
        st.plotly_chart(fig_corais, use_container_width=True)
    with col_vento_bio:
        fig_vento = px.bar(df_vento, x='Dia', y='Velocidade_Vento_Nós', title='Previsão de Vento Diário (OpenWeatherMap)', 
                           labels={'Velocidade_Vento_Nós': 'Vento (Nós)'}, height=300)
        st.plotly_chart(fig_vento, use_container_width=True)
    
    st.caption("Fonte: Dados provenientes de APIs abertas (INMET, NOAA, etc.) - **Simulação para Template**.")


# =================================================================
# ABA 2: ANÁLISE E CONSCIENTIZAÇÃO
# =================================================================
with tab_analise:
    st.header("Análise Explícita: Cultura Oceânica no Brasil")
    st.info("Entenda a relação entre Oceano, Clima e a Sociedade Brasileira. Aja com consciência.")

    # Exibição dos Tópicos
    for i, topico in enumerate(TOPICOS):
        st.markdown(f"### {topico['titulo']}")
        st.markdown("---")
        
        col_causas, col_influencia, col_cons, col_dica = st.columns(4)

        with col_causas:
            st.markdown(f"**Causas:**")
            st.write(f"👉 {topico['causas']}")
        
        with col_influencia:
            st.markdown(f"**O que Influencia:**")
            st.warning(f"💡 {topico['influencia']}")
        
        with col_cons:
            st.markdown(f"**Consequências no Brasil:**")
            st.error(f"⚠️ {topico['consequencias']}")
            
        with col_dica:
            st.markdown(f"**Ação de Cultura Oceânica (Dica):**")
            st.success(f"✅ {topico['dica']}")
        
        if i < len(TOPICOS) - 1:
            st.markdown("---")
