# Projeto ML – Inteligência Artificial com Python

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Manager-60A5FA?logo=poetry&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

Este projeto exemplifica a construção de uma aplicação de Machine Learning em Python.  
O foco é aplicar técnicas de IA para analisar dados de pizzas e apresentar resultados por meio de uma aplicação web simples.

---

## 📂 Conteúdo do repositório

- `.devcontainer/` – configuração do ambiente de desenvolvimento (VS Code + Docker).
- `src/projeto_ml/` – código-fonte da lógica de Machine Learning.
- `tests/` – testes automatizados.
- `MLpizza.png` – imagem ilustrativa do projeto/resultados.
- `app.py` – aplicação web utilizando Streamlit.
- `pizzas.csv` – dataset utilizado no projeto.
- `pyproject.toml` & `poetry.lock` – gerenciamento de dependências com Poetry.
- `testes.ipynb` – notebook com experimentos/visualizações interativas.

---

## 🚀 Como rodar o projeto

### ✅ Pré-requisitos

- Python **3.10+**
- [Poetry](https://python-poetry.org/) instalado (`pip install poetry`)

### ▶️ Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/MariaEduardaCiarini/projeto-ml.git
cd projeto-ml

# 2. Instale as dependências
poetry install

# 3. Ative o ambiente virtual (opcional, mas recomendado)
poetry env activate

# 4. Rode a aplicação com Streamlit
streamlit run app.py
