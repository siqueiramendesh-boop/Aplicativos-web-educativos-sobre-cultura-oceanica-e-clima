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
