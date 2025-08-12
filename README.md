# SPVA-Recommender

## Descrição do Projeto

O **SPVA-Recommender** é um microsserviço de recomendação de candidatos, parte do ecossistema do portal de empregos SPVA. A sua principal função é analisar a descrição de uma vaga de emprego e os currículos de uma lista de candidatos para classificar os candidatos mais adequados para essa vaga. Para tal, utiliza um modelo de processamento de linguagem natural (PLN) para calcular a similaridade semântica entre os documentos.

## Como Funciona

O processo de recomendação segue os seguintes passos:

1.  O serviço recebe um ID de uma vaga e uma lista de IDs de candidatos através de um pedido de API.
2.  Consulta uma base de dados MongoDB para obter o texto da descrição da vaga e os textos dos currículos dos candidatos.
3.  Utiliza um modelo pré-treinado da biblioteca `sentence-transformers` para converter os textos da vaga e dos currículos em vetores numéricos (embeddings).
4.  Calcula a similaridade de cosseno entre o vetor da vaga e os vetores de cada um dos candidatos.
5.  Retorna uma lista ordenada dos candidatos com base na sua pontuação de similaridade, do mais relevante para o menos relevante.

## Tecnologias Utilizadas

  - **Back-end:** Python, FastAPI
  - **Base de Dados:** MongoDB
  - **ODM (Object-Document Mapper):** Beanie
  - **Machine Learning:** Sentence-Transformers, PyTorch
  - **Conteinerização:** Docker, Docker Compose
  - **Servidor Web:** Uvicorn, Gunicorn

## Como Executar o Projeto

Existem duas maneiras de executar o projeto: utilizando Docker para uma configuração completa e automatizada, ou localmente para desenvolvimento.

### Modo 1: Executando com Docker (Recomendado)

Este modo orquestra a aplicação em um contêiner.

**Pré-requisitos:**

  - Docker
  - Docker Compose

**Passos:**

1.  **Clonar o repositório:**

    ```bash
    git clone git@github.com:victordantas1/spva-recommender.git
    cd spva-recommender
    ```

2.  **Configurar variáveis de ambiente:**

      - Crie um arquivo `.env` a partir do template fornecido.
        ```bash
        cp .env.template .env
        ```
      - Revise o arquivo `.env` e ajuste as variáveis se necessário, especialmente a `MONGODB_URL` para apontar para sua instância do MongoDB.

3.  **Iniciar o serviço com Docker Compose:**

    ```bash
    docker-compose up -d --build
    ```

    Este comando irá construir a imagem Docker e iniciar o contêiner da aplicação. O serviço estará disponível na porta `8001` por padrão.

### Modo 2: Executando Localmente (Desenvolvimento)

Este modo é ideal para desenvolvimento e depuração. Requer que você tenha as dependências (Python, MongoDB) instaladas na sua máquina.

**Pré-requisitos:**

  - Python 3.10 ou superior
  - Acesso a uma instância do MongoDB.

**Passos:**

1.  **Clonar o repositório:**

    ```bash
    git clone git@github.com:victordantas1/spva-recommender.git
    cd spva-recommender
    ```

2.  **Criar ambiente virtual e instalar dependências:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Configurar variáveis de ambiente:**

      - Crie o arquivo `.env` a partir do template:
        ```bash
        cp .env.template .env
        ```
      - **Edite o arquivo `.env`** para configurar as variáveis, como a `MONGODB_URL` e a `PORT`.

4.  **Executar o script de inicialização:**

      - Para modo de desenvolvimento com hot-reload:
        ```bash
        ./run.sh dev
        ```
      - Para modo de produção:
        ```bash
        ./run.sh prod
        ```

    A API estará acessível na porta configurada no seu arquivo `.env` (padrão `8001`).

## API Endpoint

O serviço expõe um único endpoint principal para obter recomendações.

### Obter Recomendações de Candidatos

  - **GET** `/recommendation/{job_id}`

    Retorna uma lista classificada dos candidatos mais relevantes para a vaga especificada.

  - **Parâmetros de Consulta (Query):**

      - `candidates` (List[int]): Uma lista de IDs de utilizadores (candidatos) a serem avaliados.
      - `top_k` (int): O número máximo de candidatos a serem retornados na lista.

  - **Exemplo de Pedido:**

    ```
    GET http://localhost:8001/recommendation/123?candidates=1&candidates=2&top_k=2
    ```

  - **Resposta de Sucesso (200 OK):**

    ```json
    [
      {
        "candidate": {
          "user_id": 2,
          "document": "Desenvolvedor de software experiente com foco em Python e desenvolvimento web. Conhecimentos em Django e FastAPI.",
          "tokens": ["desenvolvedor", "de", "software", "experiente", "com", "foco", "em", "python", "e", "desenvolvimento", "web", "conhecimentos", "em", "django", "e", "fastapi"],
          "tokens_clean": ["desenvolvedor", "software", "experiente", "foco", "python", "desenvolvimento", "web", "conhecimentos", "django", "fastapi"],
          "tokens_ner": ["Desenvolvedor de software", "Python", "Django", "FastAPI"]
        },
        "score": 0.89
      },
      {
        "candidate": {
          "user_id": 1,
          "document": "Recém-formado em ciência da computação. Conhecimentos básicos em Java e C++.",
          "tokens": ["recém-formado", "em", "ciência", "da", "computação", "conhecimentos", "básicos", "em", "java", "e", "c++"],
          "tokens_clean": ["recém-formado", "ciência", "computação", "conhecimentos", "básicos", "java", "c++"],
          "tokens_ner": ["Ciência da Computação", "Java", "C++"]
        },
        "score": 0.75
      }
    ]
    ```