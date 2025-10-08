import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

# --- Configurações da Página ---
st.set_page_config(
    page_title="OceanApp Brasil: Visualização Unificada",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("🌊 OceanApp Brasil: Cultura Oceânica e Clima")
st.subheader("Painel de Visualização Unificado de Dados Abertos e Análise para o Litoral Brasileiro")
st.markdown("---")


# ⚠️ FUNÇÕES DE INTEGRAÇÃO DE DADOS REAIS (TEMPLATE DE SIMULAÇÃO)
# O código abaixo SIMULA a obtenção de dados das fontes (INMET, Marinha, NOAA, etc.)
# Você deve substituir o conteúdo destas funções pela sua lógica de chamada de API/leitura de arquivo para ter dados reais.

@st.cache_data
def get_dados_simulados():
    """Gera todos os DataFrames simulados para os gráficos e análises."""
    
    # 1. INMET (Temperatura Média Anual - 10 Anos)
    anos = pd.date_range(start='2015-01-01', periods=10, freq='Y')
    df_tendencia = pd.DataFrame({
        'Ano': anos.year,
        'Temp_Media_Anual_C': [25.0, 25.2, 25.4, 25.1, 25.3, 25.6, 25.8, 26.0, 26.2, 26.5],
    })
    
    # 2. OpenWeatherMap (Vento Diário - 7 dias)
    dias = pd.date_range(start=datetime.now(), periods=7, freq='D')
    df_vento = pd.DataFrame({
        'Dia': dias.strftime('%a, %d/%m'),
        'Velocidade_Vento_Nós': [10, 12, 8, 9, 15, 11, 7],
    })
    
    # 3. NOAA (Nível do Mar - 30 Anos)
    anos_nivel = pd.date_range(start='1990-01-01', periods=30, freq='Y')
    df_nivel_longo = pd.DataFrame({
        'Ano': anos_nivel.year,
        'Nivel_Medio_Mar_cm': 10 + np.cumsum(np.random.rand(30) * 0.2 + 0.1), 
    })

    # 4. CEMADEN (Alerta de Deslizamento - Simulação por Estado)
    df_risco = pd.DataFrame({
        'Estado': ['RJ', 'SP', 'ES', 'BA', 'PE', 'SC'],
        'Alertas_Recentes': [35, 28, 15, 10, 5, 20], 
    }).sort_values('Alertas_Recentes', ascending=False)
    
    # 5. Marinha do Brasil (Previsão de Maré - 48 horas)
    horas = pd.date_range(start=datetime.now(), periods=48, freq='H') 
    df_mare = pd.DataFrame({
        'Data_Hora': horas,
        'Nivel_Maré_m': [0.5, 0.8, 1.2, 1.0, 0.6, 0.2, 0.1, 0.4, 0.9, 1.5, 1.3, 0.7, 0.4, 0.8, 1.3, 1.1, 0.7, 0.3, 0.2, 0.5, 1.0, 1.4, 1.2, 0.6] * 2,
    }).set_index('Data_Hora')

    # 6. SiBBr (Ocorrências de Branqueamento de Corais por Ano)
    anos_corais = pd.date_range(start='2018-01-01', periods=8, freq='Y')
    df_corais = pd.DataFrame({
        'Ano': anos_corais.year,
        'Ocorrencias_Branqueamento': [5, 3, 10, 7, 15, 12, 18, 20], 
    })

    return df_tendencia, df_vento, df_nivel_longo, df_risco, df_mare, df_corais

# Chama a função de dados simulados
df_tendencia, df_vento, df_nivel_longo, df_risco, df_mare, df_corais = get_dados_simulados()


# --- 2. Definição dos Tópicos de Cultura Oceânica (6 Tópicos) ---
TOPICOS = [
    {
        "titulo": "1. Aumento do Nível do Mar",
        "causas": "Degelo polar e **expansão térmica** da água (aquecimento global).",
        "influencia": "Afeta os 8.500 km da costa brasileira, ameaçando cidades e ilhas costeiras.",
        "consequencias": "Aceleração da **erosão costeira**, inundações frequentes e salinização da água potável subterrânea.",
        "dica": "Apoiar planos municipais de adaptação e exigir infraestrutura resiliente em áreas costeiras.",
    },
    {
        "titulo": "2. Acidificação Oceânica",
        "causas": "O oceano absorve o **dióxido de carbono ($CO_2$)** da atmosfera (emissões e **desmatamento**).",
        "influencia": "Diretamente ligada às emissões brasileiras e prejudica a capacidade do oceano de absorver mais $CO_2$.",
        "consequencias": "Dificuldade de corais, ostras e mariscos em formar conchas. Risco à **aquicultura**.",
        "dica": "Reduzir o consumo de carne bovina e apoiar a transição para energias renováveis.",
    },
    {
        "titulo": "3. Eventos Climáticos Extremos",
        "causas": "Alterações nos padrões de circulação (**El Niño** e **La Niña**) intensificando os fenômenos.",
        "influencia": "Intensifica **secas prolongadas** (Nordeste) e **chuvas torrenciais** e deslizamentos (Sul/Sudeste).",
        "consequencias": "Deslizamentos de terra em encostas litorâneas, perdas na pesca e danos à infraestrutura portuária.",
        "dica": "Consultar a previsão de tempo e maré da **Marinha/INMET** e participar de sistemas de alerta comunitário (CEMADEN).",
    },
    {
        "titulo": "4. Branqueamento de Corais",
        "causas": "Aumento rápido da **Temperatura da Superfície do Mar (TSM)**, levando ao estresse térmico.",
        "influencia": "Afeta os recifes de corais, como os de **Abrolhos** (BA), que são berçários de vida marinha.",
        "consequencias": "Morte dos corais, perda de habitat e redução da proteção costeira natural.",
        "dica": "Apoiar projetos de monitoramento de corais e usar protetores solares *reef safe*.",
    },
    {
        "titulo": "5. Poluição Marinha por Plástico",
        "causas": "Gestão inadequada de resíduos sólidos em **cidades costeiras** e descarte em rios.",
        "influencia": "Grandes rios atuam como canais de transporte de resíduos, tornando o Brasil um grande contribuinte de lixo marinho.",
        "consequencias": "Ingestão e sufocamento da **fauna marinha** e contaminação por **microplásticos** na cadeia alimentar.",
        "dica": "Praticar os 3 R's (**Reduzir, Reutilizar, Reciclar**) e participar de mutirões de limpeza.",
    },
    {
        "titulo": "6. Impacto na Pesca Artesanal",
        "causas": "Mudança nas rotas migratórias dos peixes devido à **temperatura da água** e alterações nas correntes.",
        "influencia": "Afeta a principal fonte de renda e subsistência de comunidades pesqueiras tradicionais brasileiras.",
        "consequencias": "Diminuição do estoque pesqueiro, insegurança alimentar e êxodo das comunidades costeiras.",
        "dica": "Apoiar a **pesca sustentável** e consumir peixes certificados que não estejam em risco de extinção.",
    },
]


# --- 3. LAYOUT UNIFICADO (ABAS) ---

tab_graficos, tab_analise = st.tabs(["📊 Gráficos de Dados Abertos e Tendências", "💡 Análise e Conscientização no Brasil"])

# =================================================================
# ABA 1: GRÁFICOS DE DADOS ABERTOS (UNIFICADO)
# =================================================================
with tab_graficos:
    st.header("1. Tendências de Longo Prazo e Risco")
    
    col_temp, col_nivel, col_risco = st.columns(3)
    
    with col_temp:
        st.markdown("##### Temperatura Média Anual (INMET)")
        fig_temp = px.line(df_tendencia, x='Ano', y='Temp_Media_Anual_C', markers=True, height=250)
        st.plotly_chart(fig_temp, use_container_width=True)
    
    with col_nivel:
        st.markdown("##### Aumento do Nível do Mar (NOAA)")
        fig_nivel = px.line(df_nivel_longo, x='Ano', y='Nivel_Medio_Mar_cm', line_shape='spline', height=250)
        st.plotly_chart(fig_nivel, use_container_width=True)

    with col_risco:
        st.markdown("##### Alertas de Deslizamentos (CEMADEN)")
        fig_risco = px.bar(df_risco, x='Estado', y='Alertas_Recentes', height=250)
        st.plotly_chart(fig_risco, use_container_width=True)

    st.markdown("---")
    
    st.header("2. Previsão Operacional e Biodiversidade")
    
    col_mare, col_vento, col_corais = st.columns(3)

    with col_mare:
        st.markdown("##### Previsão de Nível da Maré (Marinha do Brasil)")
        fig_mare = px.area(df_mare.reset_index(), x='Data_Hora', y='Nivel_Maré_m', height=250)
        st.plotly_chart(fig_mare, use_container_width=True)
        
    with col_vento:
        st.markdown("##### Previsão de Vento Diário (OpenWeatherMap)")
        fig_vento = px.bar(df_vento, x='Dia', y='Velocidade_Vento_Nós', height=250)
        st.plotly_chart(fig_vento, use_container_width=True)

    with col_corais:
        st.markdown("##### Ocorrências de Branqueamento (SiBBr)")
        fig_corais = px.bar(df_corais, x='Ano', y='Ocorrencias_Branqueamento', height=250)
        st.plotly_chart(fig_corais, use_container_width=True)

    st.caption("Fonte: Dados provenientes de APIs abertas (INMET, NOAA, Marinha, CEMADEN, SiBBr, OpenWeatherMap) - **Simulação para Template**.")


# =================================================================
# ABA 2: ANÁLISE E CONSCIENTIZAÇÃO (UNIFICADO)
# =================================================================
with tab_analise:
    st.header("Análise Explícita de Impactos: Cultura Oceânica no Brasil")
    st.info("Aprofunde-se nas causas e consequências do clima no oceano brasileiro. Sua ação é fundamental.")

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
