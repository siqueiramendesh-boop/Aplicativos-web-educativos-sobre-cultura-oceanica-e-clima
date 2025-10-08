import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- Configurações da Página ---
st.set_page_config(
    page_title="OceanApp Brasil: Gráficos e Pesquisa",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Título Principal
st.title("🌊 OceanApp Brasil: Gráficos de Dados Abertos e Cultura Oceânica")
st.subheader("Análise Simultânea de Tendências Climáticas e Conscientização")
st.markdown("---")

# --- 1. Função de Simulação de Dados para Gráficos ---
# NOTA: Esta função SIMULA dados de fontes abertas (10 anos de Tendência e 48h de Previsão de Maré).
# Para usar DADOS REAIS: Substitua esta função por chamadas a APIs Abertas (INMET, Marinha, etc.)
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
        "causas": "Degelo polar e **expansão térmica** da água (aquecimento global).",
        "consequencias": "**Erosão costeira**, inundações frequentes e salinização de lençóis freáticos.",
        "dica": "Apoiar a adaptação costeira e usar dados de **altimetria** (satélites) para monitoramento local.",
    },
    {
        "titulo": "2. Acidificação Oceânica",
        "causas": "Absorção de **dióxido de carbono ($CO_2$)** da atmosfera (emissões e **desmatamento** brasileiro).",
        "consequencias": "Dificuldade de corais e moluscos em formar conchas. Risco à **aquicultura**.",
        "dica": "Reduzir a **pegada de carbono** e apoiar a restauração de biomas.",
    },
    {
        "titulo": "3. Eventos Climáticos Extremos",
        "causas": "Alterações em padrões oceânicos e atmosféricos (**El Niño** e **La Niña**).",
        "consequencias": "**Secas prolongadas** (Nordeste) e **chuvas torrenciais** (Sul/Sudeste), danos a portos.",
        "dica": "Consultar previsões de **INMET** e **Marinha** para segurança e planejamento.",
    },
    {
        "titulo": "4. Branqueamento de Corais",
        "causas": "**Aumento da temperatura da água** (estresse térmico) expulsa algas simbióticas.",
        "consequencias": "Morte de corais e perda de **biodiversidade** e de proteção costeira natural.",
        "dica": "Apoiar a **conservação marinha** e usar protetores solares *reef safe*.",
    },
    {
        "titulo": "5. Poluição Marinha por Plástico",
        "causas": "Gestão inadequada de resíduos sólidos em **cidades costeiras** e descarte em rios.",
        "consequencias": "Ingestão e sufocamento da **fauna marinha** e contaminação por **microplásticos**.",
        "dica": "Priorizar os 3 R's (**Reduzir, Reutilizar, Reciclar**) e participar de mutirões de limpeza.",
    },
]


# --- 3. Layout Principal em Colunas (Gráficos e Explicações Lado a Lado) ---

# Coluna Principal para Gráficos
col_graficos = st.columns([1])[0] 
# Coluna Principal para a Análise/Pesquisa
col_pesquisa = st.columns([1])[0] 

# Usamos a estrutura do Streamlit para dividir os componentes

st.markdown("## 📊 Visualização de Dados Abertos (10 Anos)")
st.info("Gráficos interativos gerados a partir de dados abertos (simulados) de tendências climáticas no Brasil.")

# GRÁFICOS DE TENDÊNCIA (Temperatura e Nível do Mar)
col_temp_graph, col_nivel_graph = st.columns(2)

with col_temp_graph:
    # Gráfico 1: Temperatura
    fig_temp_decada = px.line(
        df_tendencia,
        x='Ano',
        y='Temp_Media_Anual_C',
        title='Tendência de Temperatura Média Anual (°C)',
        labels={'Temp_Media_Anual_C': 'Temperatura Média Anual (°C)'},
        markers=True,
        height=300
    )
    st.plotly_chart(fig_temp_decada, use_container_width=True)

with col_nivel_graph:
    # Gráfico 2: Nível do Mar
    fig_nivel_decada = px.bar(
        df_tendencia,
        x='Ano',
        y='Nivel_Medio_Mar_cm',
        title='Aumento do Nível Médio do Mar (cm)',
        labels={'Nivel_Medio_Mar_cm': 'Aumento do Nível (cm)'},
        height=300
    )
    st.plotly_chart(fig_nivel_decada, use_container_width=True)

st.markdown("---")

st.markdown("## 🔎 Análise Detalhada (Causas, Consequências e Dicas)")
st.info("Os gráficos mostram as tendências. Esta seção explica as causas, consequências e as ações de **Cultura Oceânica**.")

# Loop para exibir cada tópico da pesquisa, alinhando-o ao gráfico de Maré
for i, topico in enumerate(TOPICOS):
    
    # Se for o Tópico 1, colocamos o Gráfico de Maré ao lado dele
    if i == 0:
        col_pesquisa_content, col_mare_graph = st.columns([1, 1])

        with col_mare_graph:
            st.markdown("### Previsão de Maré (48h)")
            st.caption("Gráfico crucial para segurança e gestão costeira (Marinha do Brasil/Simulação).")
            # GRÁFICO 3: MARÉ
            fig_mare = px.area(
                df_mare,
                y='Nivel_Maré_m',
                title='Variação do Nível da Maré em 48 Horas (Metros)',
                labels={'Nivel_Maré_m': 'Nível da Maré (m)', 'Data_Hora': 'Data e Hora'},
                line_shape='spline',
                height=350
            )
            st.plotly_chart(fig_mare, use_container_width=True)

        with col_pesquisa_content:
            st.markdown(f"### {topico['titulo']}")
            col_causas, col_cons, col_dica = st.columns([1, 1, 1])
            with col_causas:
                st.markdown(f"**Causas:**")
                st.write(f"👉 {topico['causas']}")
            with col_cons:
                st.markdown(f"**Consequências:**")
                st.warning(f"⚠️ {topico['consequencias']}")
            with col_dica:
                st.markdown(f"**Dica (Cultura Oceânica):**")
                st.success(f"✅ {topico['dica']}")
        
        st.markdown("---")

    # Demais Tópicos da Pesquisa, exibidos em linha
    else:
        st.markdown(f"### {topico['titulo']}")
        col_causas, col_cons, col_dica = st.columns([1, 1, 1])
        
        with col_causas:
            st.markdown(f"**Causas:**")
            st.write(f"👉 {topico['causas']}")
        
        with col_cons:
            st.markdown(f"**Consequências:**")
            st.warning(f"⚠️ {topico['consequencias']}")
        
        with col_dica:
            st.markdown(f"**Dica (Cultura Oceânica):**")
            st.success(f"✅ {topico['dica']}")
        
        if i < len(TOPICOS) - 1:
            st.markdown("---")

st.caption("O aplicativo utiliza dados abertos (simulados) com a estrutura correta para integração de APIs reais do INMET, Marinha, etc.")
