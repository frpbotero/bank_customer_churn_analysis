# 📊 Bank Customer Churn Analysis

Este repositório apresenta um estudo completo de previsão de evasão de clientes (**Churn**) no setor bancário, utilizando um processo estruturado de **KDD — Knowledge Discovery in Databases**. O projeto combina análise exploratória, pré-processamento avançado, balanceamento de classes, redução de dimensionalidade e avaliação comparativa de múltiplos algoritmos de machine learning.

O trabalho foi desenvolvido por **Felipe R. P. Botero**, como parte de um estudo acadêmico focado em modelos preditivos de retenção de clientes.

---

## 🧠 Objetivo do Projeto

Antecipar clientes com maior probabilidade de cancelar seus serviços bancários, permitindo ao negócio aplicar ações preventivas e reduzir perdas financeiras.
A métrica principal deste estudo é o **Recall da Classe 1 (clientes que cancelam)**, pois o custo de não identificar um cliente em risco é maior do que agir preventivamente em um cliente que não sairia.

---

## 📂 Estrutura do Projeto

* **Exploratory Data Analysis (EDA)**
* **Tratamento de outliers (Winsorização)**
* **Codificação de variáveis categóricas (One-Hot Encoding)**
* **Escalonamento de variáveis numéricas**
* **Balanceamento com SMOTE**
* **Redução de dimensionalidade com PCA**
* **Avaliação de múltiplos modelos**
* **Ajuste de threshold para maximização do Recall**

Todas essas etapas seguem rigorosamente as melhores práticas de ciência de dados citadas no artigo .

---

## 📊 Base de Dados

* Origem: Dataset público do **Kaggle – Bank Customer Churn Prediction**.
* Total de registros: **10.000 clientes**.
* Etapas de preparação:

  * Remoção de atributos irrelevantes (ex.: *RowNumber*, *CustomerID*, *Surname*) .
  * Análise de correlação e exclusão de variável com correlação perfeita para evitar **data leakage**.

---

## 🔧 Modelos Avaliados

Foram avaliados modelos de diferentes naturezas, incluindo:

* Logistic Regression
* AdaBoost
* Random Forest
* SVM
* KNN
* Decision Tree
* MLP Neural Network
* XGBoost

A validação foi realizada via **GridSearch**, seguindo boas práticas acadêmicas .

### 📌 Resultado Inicial dos Modelos

Segundo a Tabela 1 do artigo, os melhores desempenhos (Recall Classe 1):

| Modelo              | Recall | Balanceamento | PCA   |
| ------------------- | ------ | ------------- | ----- |
| AdaBoost            | 70.05% | SMOTE         | TRUE  |
| Logistic Regression | 69.39% | SMOTE         | TRUE  |
| Logistic Regression | 69.07% | SMOTE         | FALSE |



---

## 🎯 Estratégia Final

Embora o **AdaBoost** tenha apresentado o melhor resultado inicial, o modelo que mais se destacou após otimização foi a **Regressão Logística com ajuste de threshold**.

### 🔥 Otimização por Ajuste de Threshold

Ao reduzir o limiar de classificação para **0.30**, o Recall aumentou para **86%**, mantendo níveis aceitáveis de precisão e acurácia para o contexto de negócio:

| Threshold | Recall     | Precision | F1-Score | Acurácia |
| --------- | ---------- | --------- | -------- | -------- |
| 0.10      | 98.53%     | 22.16%    | 36.19%   | 29.23%   |
| 0.20      | 92.14%     | 25.31%    | 39.72%   | 43.03%   |
| **0.30**  | **86.42%** | 28.65%    | 43.03%   | 53.40%   |

Tabela completa disponível no artigo .

---

## 🧩 Principais Insights do Estudo

Com base na análise exploratória e nos resultados do modelo, destacam-se:

* Tendência de evasão maior na **Alemanha**.
* Clientes mais idosos apresentam maior propensão ao churn.
* 45% dos clientes possuem **saldo zero** ou utilizam apenas um produto do banco.
* Forte impacto das variáveis **idade**, **atividade do cliente** e **saldo em conta** na probabilidade de churn.
* Possível direcionamento do banco a um público mais masculino.

Todos esses insights estão detalhados na seção de conclusão do material .

---

## 🚀 Tecnologias Utilizadas

* Python
* Pandas, NumPy
* Scikit-learn
* Imbalanced-learn (SMOTE, Tomek Links)
* Matplotlib, Seaborn
* PCA
* GridSearchCV

---

## 📈 Próximos Passos

O estudo sugere as seguintes evoluções:

* Testar **arquiteturas de Deep Learning**.
* Incorporar **dados temporais** (ABERTURA/ENCERRAMENTO DE CONTA).
* Integrar métricas financeiras como **CAC (Custo de Aquisição de Cliente)**.
* Expandir o pipeline para ambientes de produção.



---

## 📎 Arquivos do Repositório

* `bank_customer_churn_analysis.ipynb` – Notebook completo de análise.
---

## 📝 Licença

Este projeto é distribuído para fins acadêmicos e de pesquisa.
Adicione aqui a licença desejada (MIT, Apache 2.0, etc.).

---

## 🙋‍♂️ Autor

**Felipe R. P. Botero**
