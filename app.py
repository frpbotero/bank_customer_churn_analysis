import streamlit as st
import pandas as pd
import joblib

# Configuração da Página
st.set_page_config(page_title="Predição de Churn", layout="wide")
st.title("🏦 Predição de Churn (Pipeline Automático)")

st.markdown("""
Este app utiliza o **Pipeline Completo** treinado. 
Ele aceita dados brutos (texto) e faz o tratamento internamente.
""")

# --- 1. BARRA LATERAL ---
with st.sidebar:
    st.header("📂 Carregar Modelo")
    # Agora carregamos o modelo único que o script salvou
    uploaded_file = st.file_uploader("Arraste o arquivo 'modelo_final_para_streamlit.pkl'", type=["pkl", "joblib"])
    
    st.divider()
    
    st.header("⚙️ Configuração")
    threshold = st.slider("Threshold (Ponto de Corte)", 0.0, 1.0, 0.5, 0.01,
                          help="Acima deste valor, a predição será 'Churn' (Saída).")

# --- 2. FORMULÁRIO (Inputs) ---
st.subheader("📝 Dados do Cliente")

c1, c2, c3 = st.columns(3)

with c1:
    # Nomes das labels para o usuário (podem ser em português)
    credit_score = st.number_input("Credit Score", 300, 850, 600)
    geography = st.selectbox("País", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gênero", ["Male", "Female"])
    age = st.number_input("Idade", 18, 100, 40)

with c2:
    tenure = st.slider("Anos de Relacionamento", 0, 10, 3)
    balance = st.number_input("Saldo Bancário", 0.0, 300000.0, 60000.0)
    num_products = st.slider("Qtd. Produtos", 1, 4, 1)
    estimated_salary = st.number_input("Salário Estimado", 0.0, 300000.0, 50000.0)

with c3:
    has_crcard = st.selectbox("Tem Cartão de Crédito?", [1, 0], format_func=lambda x: "Sim" if x==1 else "Não")
    is_active = st.selectbox("Membro Ativo?", [1, 0], format_func=lambda x: "Sim" if x==1 else "Não")
    
    # Extras (Baseado nas colunas do seu treino)
    card_type = st.selectbox("Tipo de Cartão", ["DIAMOND", "GOLD", "SILVER", "PLATINUM"])
    points = st.number_input("Pontos Ganhos", 0, 1000, 500)
    satisfaction = st.slider("Nota de Satisfação", 1, 5, 3)

# --- 3. PREDIÇÃO DIRETA ---
if st.button("Realizar Predição", type="primary"):
    if uploaded_file is None:
        st.warning("⚠️ Por favor, carregue o arquivo .pkl na barra lateral primeiro.")
    else:
        try:
            # Carrega o Pipeline
            pipeline = joblib.load(uploaded_file)
            
            # --- CRIAÇÃO DO DATAFRAME ---
            # O Segredo: Os nomes das colunas (keys) DEVEM ser EXATAMENTE iguais aos do CSV de treino.
            # E os valores DEVEM ser as strings originais ("France", "Male"). Nada de 0 ou 1 aqui.
            input_df = pd.DataFrame({
                'CreditScore': [credit_score],
                'Geography': [geography],       # Passando string direto!
                'Gender': [gender],             # Passando string direto!
                'Age': [age],
                'Tenure': [tenure],
                'Balance': [balance],
                'NumOfProducts': [num_products],
                'HasCrCard': [has_crcard],
                'IsActiveMember': [is_active],
                'EstimatedSalary': [estimated_salary],
                'Satisfaction Score': [satisfaction],  # Atenção ao espaço no nome
                'Card Type': [card_type],              # Atenção ao espaço no nome
                'Point Earned': [points]               # Atenção ao espaço no nome
            })
            
            # Debug: Mostra o que está entrando no modelo
            with st.expander("Ver dados enviados ao modelo (Debug)"):
                st.dataframe(input_df)

            # Previsão
            # O Pipeline vai receber 'France', transformar internamente e prever.
            proba = pipeline.predict_proba(input_df)[:, 1][0]
            prediction = 1 if proba >= threshold else 0

            # Exibição
            st.divider()
            col_res1, col_res2 = st.columns([1, 2])
            
            with col_res1:
                st.subheader("Resultado")
                if prediction == 1:
                    st.error("🚨 **ALTO RISCO DE CHURN**")
                    st.write("O modelo indica saída.")
                else:
                    st.success("✅ **CLIENTE SEGURO**")
                    st.write("O modelo indica permanência.")
            
            with col_res2:
                st.metric("Probabilidade Calculada", f"{proba:.2%}")
                st.progress(proba)
                st.caption(f"Corte definido: {threshold:.2%}")

        except Exception as e:
            st.error("Erro na execução. Verifique os nomes das colunas.")
            st.code(e)