import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração inicial
st.set_page_config(page_title="Dashboard de Performance", page_icon="📊", layout="wide")

# Título
st.title('📈 Análise de Performance por Departamento')

# Carregar o CSV
csv_file = 'employee_performance.csv'
df = pd.read_csv(csv_file)

# Exibir os dados
st.subheader('📋 Dados Carregados')
st.dataframe(df, use_container_width=True)

# Verificar colunas
if 'Department' in df.columns and 'Performance_Score' in df.columns:

    # Filtro lateral
    with st.sidebar:
        st.header("🔎 Filtros")
        departamentos = st.multiselect("Selecione os Departamentos:", options=df['Department'].unique(), default=df['Department'].unique())
    
    # Aplicar filtros
    df_filtered = df[df['Department'].isin(departamentos)]

    # KPIs principais
    avg_score = round(df_filtered['Performance_Score'].mean(), 2)
    total_employees = df_filtered.shape[0]
    top_department = df_filtered.groupby('Department')['Performance_Score'].mean().idxmax()

    col1, col2, col3 = st.columns(3)
    col1.metric("Média Geral de Performance", avg_score)
    col2.metric("Total de Funcionários", total_employees)
    col3.metric("Departamento de Maior Desempenho", top_department)

    st.markdown("---")

    # Gráfico de barras
    st.subheader("🏆 Média de Performance por Departamento")
    perf_dept = df_filtered.groupby('Department')['Performance_Score'].mean().sort_values(ascending=False).reset_index()

    fig_bar = px.bar(perf_dept, x='Performance_Score', y='Department', orientation='h',
                     color='Performance_Score', color_continuous_scale='blues',
                     labels={'Performance_Score': 'Média de Performance', 'Department': 'Departamento'},
                     title='Média de Performance por Departamento')

    st.plotly_chart(fig_bar, use_container_width=True)

    # Gráfico de pizza
    st.subheader("📊 Distribuição de Funcionários por Departamento")
    dept_counts = df_filtered['Department'].value_counts().reset_index()
    dept_counts.columns = ['Department', 'Count']

    fig_pie = px.pie(dept_counts, names='Department', values='Count',
                     title='Distribuição dos Funcionários',
                     color_discrete_sequence=px.colors.sequential.RdBu)
    
    st.plotly_chart(fig_pie, use_container_width=True)

else:
    st.error("Colunas 'Department' e/ou 'Performance_Score' não encontradas no CSV.")
