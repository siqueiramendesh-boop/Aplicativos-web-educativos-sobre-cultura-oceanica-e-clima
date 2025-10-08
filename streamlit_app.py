import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- Configurações do Aplicativo Streamlit ---
st.set_page_config(
    page_title="OceanApp Brasil: Clima e Oceano",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Título Principal do App
st.title("🌊 OceanApp Brasil: Monitoramento, Cultura e Clima")
st.subheader("Análise de Dados Abertos e Conscientização para o Litoral Brasileiro")

# --- 1. Função de Simulação de Dados para Gráficos ---
# NOTA: Esta função simula dados de Tendência Climática de 10 anos e Maré de 2 dias.
# Em uma aplicação real, estes seriam substituídos por chamadas a APIs Abertas (ex: INMET, Marinha, Satélites).
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

# --- 2. Tópicos de Cultura Oceânica e Clima no Brasil (Resumo e Explicação) ---

# Definição dos tópicos (mínimo 5, máximo 9)
TOPICOS = [
    {
        "titulo": "1. Aumento do Nível do Mar",
        "causas": "Degelo de calotas polares e expansão térmica da água do mar devido ao aquecimento global.",
        "influencia": "Impacta 8.500 km da costa brasileira, afetando cidades litorâneas e ecossistemas de **manguezais**.",
        "consequencias": "Inundações costeiras mais frequentes, perda de habitat, salinização de lençóis freáticos e erosão costeira.",
        "dica": "Apoiar planos municipais de adaptação costeira e usar dados de **altimetria** (satélites) para monitoramento local.",
    },
    {
        "titulo": "2. Acidificação Oceânica",
        "causas": "O oceano absorve cerca de 30% do dióxido de carbono ($CO_2$) liberado na atmosfera, diminuindo seu pH.",
        "influencia": "Diretamente ligado às **emissões de gases de efeito estufa** no Brasil (desmatamento, transporte, indústria).",
        "consequencias": "Dificuldade de organismos como corais, ostras e moluscos em formar conchas e esqueletos de carbonato de cálcio. Risco à **aquicultura** brasileira.",
        "dica": "Reduzir o consumo de carne bovina (relacionada ao desmatamento) e apoiar a transição para energias renováveis.",
    },
    {
        "titulo": "3. Eventos Climáticos Extremos",
        "causas": "Alterações nos padrões de circulação atmosférica e oceânica (como o **El Niño** e **La Niña**), intensificando fenômenos.",
        "influencia": "Provoca **secas** severas no Nordeste e **chuvas intensas** e inundações no Sul e Sudeste do Brasil.",
        "consequencias": "Perdas na agricultura, deslizamentos de terra (em áreas costeiras e serranas), e danos à infraestrutura portuária.",
        "dica": "Consultar a previsão de tempo e maré da Marinha e do INMET (dados abertos) antes de atividades no mar ou na costa.",
    },
    {
        "titulo": "4. Branqueamento de Corais",
        "causas": "Aumento da temperatura da água (estresse térmico) expulsa as algas simbióticas (zooxantelas) que dão cor e alimento aos corais.",
        "influencia": "Afeta ecossistemas de recifes críticos, como os de **Abrolhos** (BA), essenciais para a biodiversidade marinha.",
        "consequencias": "Morte dos corais, perda de habitats para peixes e invertebrados, e redução da proteção costeira contra ondas.",
        "dica": "Apoiar unidades de conservação marinhas e evitar o uso de protetores solares com oxibenzona, que prejudicam os corais.",
    },
    {
        "titulo": "5. Poluição Marinha por Plástico",
        "causas": "Gestão inadequada de resíduos sólidos em áreas costeiras e urbanas, além do descarte ilegal em rios.",
        "influencia": "A **Baía de Guanabara** e a foz de grandes rios são pontos críticos de entrada de plástico no oceano.",
        "consequencias": "Ingestão e sufocamento da fauna marinha (tartarugas, peixes, aves) e contaminação por **microplásticos** na cadeia alimentar.",
        "dica": "Priorizar o consumo de produtos sustentáveis, evitar plásticos de uso único e participar de mutirões de limpeza de praia (ações de **Cultura Oceânica**).",
    },
]

# --- 3. Geração dos Gráficos com Dados Abertos (Simulados) ---

# Aba Principal para os Tópicos e Gráficos
tab1, tab2, tab3 = st.tabs(["📊 Tendências Climáticas (10 Anos)", "🌊 Previsão de Maré (48h)", "💡 Análise e Conscientização"])

with tab1:
    st.header("Gráfico 1: Aquecimento e Subida do Nível do Mar (Tendência de 10 Anos)")
    st.info("Visualização baseada em dados abertos (Simulados) para mostrar o aumento de temperatura e nível do mar na costa brasileira.")
    
    col_a, col_b = st.columns(2)

    with col_a:
        fig_temp_decada = px.line(
            df_tendencia,
            x='Ano',
            y='Temp_Media_Anual_C',
            title='Tendência de Temperatura Média Anual (°C)',
            labels={'Temp_Media_Anual_C': 'Temperatura Média Anual (°C)'},
            markers=True
        )
        st.plotly_chart(fig_temp_decada, use_container_width=True)

    with col_b:
        fig_nivel_decada = px.bar(
            df_tendencia,
            x='Ano',
            y='Nivel_Medio_Mar_cm',
            title='Tendência de Aumento do Nível Médio do Mar (cm)',
            labels={'Nivel_Medio_Mar_cm': 'Aumento do Nível (cm)'}
        )
        st.plotly_chart(fig_nivel_decada, use_container_width=True)

    st.caption("Fonte: Dados climáticos e oceanográficos abertos (Simulação baseada em tendências reais).")

with tab2:
    st.header("Gráfico 2: Previsão Detalhada de Maré (48 Horas)")
    st.info("Dados cruciais para a segurança da navegação, pesca e gestão costeira. Em aplicações reais, use a API da Marinha do Brasil.")

    fig_mare = px.area(
        df_mare,
        y='Nivel_Maré_m',
        title='Variação do Nível da Maré em 48 Horas',
        labels={'Nivel_Maré_m': 'Nível da Maré (metros)', 'Data_Hora': 'Data e Hora'},
        line_shape='spline'
    )
    fig_mare.update_layout(height=500)
    st.plotly_chart(fig_mare, use_container_width=True)
    st.caption("Fonte: Dados Oceânicos Abertos (Simulação de previsão de maré).")


with tab3:
    st.header("Análise Detalhada dos Tópicos")
    st.info("Abaixo, uma visão explícita de como a relação oceano-clima afeta o Brasil e como podemos agir (Cultura Oceânica).")

    # Exibição dos Tópicos
    for i, topico in enumerate(TOPICOS):
        st.markdown(f"### {topico['titulo']}")
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.markdown(f"**Causas e O que Influencia:**")
            st.write(f"- {topico['causas']}")
        
        with col2:
            st.markdown(f"**Consequências no Brasil:**")
            st.warning(f"- {topico['consequencias']}")
        
        with col3:
            st.markdown(f"**Ação de Cultura Oceânica (Dica):**")
            st.success(f"- {topico['dica']}")
        
        if i < len(TOPICOS) - 1:
            st.markdown("---")
