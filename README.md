# Sicredi Web Scraping

Este projeto realiza web scraping do site Sicredi Conexão para extrair informações de produtos e segmentos.

## 📋 Visão Geral

O script acessa a página inicial, navega até o menu de produtos e coleta os dados de todos os segmentos e links de produtos disponíveis, exportando-os para um arquivo CSV.

## 🛠️ Tecnologias Utilizadas

-   **Python 3.x**
-   **Selenium**: Para automação do navegador.
-   **WebDriver Manager**: Para gerenciamento automático dos drivers do navegador.

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina.

### Configuração do Ambiente

Recomendamos o uso de um ambiente virtual (venv) para isolar as dependências do projeto.

1.  **Crie o ambiente virtual:**

    ```bash
    python -m venv venv
    ```

2.  **Ative o ambiente virtual:**

    -   No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    -   No Linux/macOS:
        ```bash
        source venv/bin/activate
        ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

### Execução

Para rodar o scraper, execute o seguinte comando na raiz do projeto:

```bash
python main.py
```

## 📂 Saída (Output)

Os dados extraídos serão salvos automaticamente na pasta `output/` com o nome `segmentos.csv`.

**Formato do arquivo:**
-   **Segmento**: Categoria do produto.
-   **Nome do Produto**: Título do produto.
-   **URL**: Link direto para a página do produto.

> **Nota:** A pasta `output/` é mantida no repositório, mas os arquivos gerados dentro dela são ignorados pelo Git.
