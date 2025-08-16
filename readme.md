# Projeto de Predição de Diabetes

Este projeto é uma API simples em Python usando FastAPI para prever o estado de saúde de um paciente (não-diabético, pré-diabético ou diabético) com base em dados de saúde.

### Dataset
[Multiclass Diabetes Dataset](https://www.kaggle.com/datasets/yasserhessein/multiclass-diabetes-dataset/data "Multiclass Diabetes Dataset")


## Estrutura do Projeto

A estrutura de pastas do projeto é a seguinte:

```
.
├── api.py
├── best_model.pkl
├── data.csv
├── EDA.ipynb
├── index.html
├── readme.md
└── requirements.txt
```

* `api.py`: Contém o código da API usando FastAPI, incluindo o endpoint de predição.

* `best_model.pkl`: O modelo de aprendizado de máquina pré-treinado.

* `data.csv`: Conjunto de dados original usado para treinamento.

* `EDA.ipynb`: Notebook Jupyter com a Análise Exploratória de Dados (EDA) e treinamento do modelo.

* `index.html`: Formulário de teste HTML para interagir com a API.

* `requirements.txt`: Lista as bibliotecas Python necessárias para o projeto.

## Como Rodar

### 1. Instalar Dependências

Certifique-se de ter o Python instalado. Em seguida, instale as bibliotecas necessárias usando o `requirements.txt`:

``` bash
pip install -r requirements.txt
```
### 2. Iniciar a API

Para rodar a API, navegue até a pasta do projeto e execute o seguinte comando no terminal. Certifique-se de que seus arquivos `.pkl` e `.joblib` estão na mesma pasta que `api.py`.

```
uvicorn api:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`. O `--reload` faz com que o servidor reinicie automaticamente a cada mudança no código.

### 3. Testar a Aplicação

Abra o arquivo `index.html` em seu navegador web. Ele fornecerá uma interface gráfica para inserir os dados e enviar uma requisição para a sua API local.