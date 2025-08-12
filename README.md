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

## Instalação e Configuração

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
      - Crie um ficheiro `.env` na raiz do projeto (pode basear-se num `.env.example` se existir).
      - Configure as variáveis necessárias, como a URL do MongoDB:
        ```env
        MONGODB_URL=mongodb://localhost:27017/spva
        ```
3.  **Iniciar o serviço com Docker Compose:**
    ```bash
    docker-compose up -d --build
    ```
    Este comando irá construir a imagem Docker e iniciar o contentor da aplicação. O serviço estará disponível na porta `8001` por defeito.

## Como Executar o Projeto

O script `run.sh` permite executar a aplicação em diferentes ambientes:

  - **Desenvolvimento:**

    ```bash
    ./run.sh dev
    ```

    O Uvicorn iniciará o servidor com *hot-reload* ativado.

  - **Produção:**

    ```bash
    ./run.sh prod
    ```

    O Gunicorn iniciará o servidor com múltiplos *workers* para um ambiente de produção.

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