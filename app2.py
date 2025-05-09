import streamlit as st
import pandas as pd

# Adiciona um CSS customizado para esconder elementos
st.markdown(
    """
    <style>
    .github-link {
        display: none;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Título do aplicativo
st.title('Análise de Performance por Departamento')

# Carregar o CSV
csv_file = 'employee_performance.csv'  # certifique-se que o arquivo está na mesma pasta que o app.py
df = pd.read_csv(csv_file)

# Exibir os dados
st.write('### Dados carregados:')
st.dataframe(df)

# Filtrar apenas as colunas necessárias (se necessário)
if 'Department' in df.columns and 'Performance_Score' in df.columns:
    
    # Agrupar por Departamento e calcular a média da performance
    performance_por_departamento = df.groupby('Department')['Performance_Score'].mean().sort_values(ascending=False)
    
    # Mostrar o gráfico
    st.write('### Média de Performance por Departamento')
    st.bar_chart(performance_por_departamento)

else:
    st.error("Colunas 'Department' e/ou 'Performance_Score' não encontradas no CSV.")

# Exemplo de link do GitHub que você quer ocultar
st.markdown('<a href="https://github.com/seu-usuario" class="github-link">GitHub</a>', unsafe_allow_html=True)

