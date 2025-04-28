#   Hugging Face Models para Análise de Comentários de E-commerce

Este é um projeto de estudos e testes que utiliza modelos pré-treinados da Hugging Face para realizar diversas análises em comentários e reviews de produtos de sites de e-commerce. As funcionalidades incluem análise de sentimentos, resumo de texto, preenchimento de palavras, resposta a perguntas, classificação de tópicos e tradução.

##   Funcionalidades

O projeto é composto pelos seguintes scripts Python:

* **sentimento.py:** Realiza análise de sentimentos em comentários de produtos, classificando o sentimento como positivo ou negativo.
* **resumo.py:** Gera resumos concisos de múltiplas avaliações de produtos.
* **preenchimento.py:** Preenche palavras mascaradas em frases sobre produtos.
* **pergunta.py:** Responde a perguntas sobre produtos com base em um contexto fornecido.
* **classificacao.py:** Classifica comentários de produtos em diferentes categorias (ex: qualidade, entrega, atendimento ao cliente).
* **traducao.py:** Traduz texto de comentários de português para inglês.

##   Dependências

Para executar este projeto, você precisará das seguintes bibliotecas Python:

* `transformers`
* `torch` (PyTorch)
* `python-dotenv`
* `requests`
* `urllib3`

Você pode instalar as dependências usando o pip. É recomendado instalar o PyTorch primeiro, seguindo as instruções do site oficial para garantir a compatibilidade com seu sistema (CPU ou GPU).

1.  **Instale o PyTorch:**

    * Visite o site oficial do PyTorch: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)
    * Selecione a configuração do seu sistema (sistema operacional, pacote, linguagem, CUDA se você tiver GPU) e execute o comando fornecido. Por exemplo:

        ```bash
        #   Exemplo para CPU (verifique o site do PyTorch para a instrução correta)
        pip3 install torch torchvision torchaudio
        ```

2.  **Instale as outras dependências:**

    ```bash
    pip install transformers python-dotenv requests urllib3
    ```

##   Configuração

1.  **Chave da API da Hugging Face:**

    * Você precisa de uma chave da API da Hugging Face para usar os modelos de inferência. Se você ainda não tem uma, crie uma conta no [Hugging Face](https://huggingface.co/) e obtenha sua chave.
    * Crie um arquivo `.env` na raiz do projeto.
    * Adicione a sua chave da API da Hugging Face ao arquivo `.env`:

        ```
        HUGGING_FACE_API_KEY=SUA_CHAVE_AQUI
        ```

2.  **Execução dos Scripts:**

    * Cada script pode ser executado individualmente usando o Python. Por exemplo, para executar `sentimento.py`:

        ```bash
        python sentimento.py
        ```

    * Certifique-se de estar no diretório do projeto ao executar os scripts.

##   Detalhes dos Scripts

* **sentimento.py:**

    * Utiliza o modelo `lxyuan/distilbert-base-multilingual-cased-sentiments-student` para análise de sentimentos.
    * Processa uma lista de comentários de produtos e imprime o sentimento de cada um.

* **resumo.py:**

    * Utiliza o modelo `facebook/bart-large-cnn` para gerar resumos.
    * Envia os comentários para a API da Hugging Face e imprime os resumos recebidos.
    * Requer a chave da API da Hugging Face para autenticação.

* **preenchimento.py:**

    * Utiliza o modelo `neuralmind/bert-base-portuguese-cased` para preencher palavras mascaradas.
    * Envia uma frase com uma máscara para a API e imprime as palavras previstas.
    * Requer a chave da API da Hugging Face.

* **pergunta.py:**

    * Utiliza o modelo `pierreguillou/bert-base-cased-squad-v1.1-portuguese` para responder a perguntas.
    * Fornece um contexto e uma pergunta sobre um produto e imprime a resposta gerada pela API.

* **classificacao.py:**

    * Utiliza o modelo `facebook/bart-large-mnli` para classificar comentários em categorias predefinidas.
    * Classifica os comentários em categorias como "qualidade", "entrega", "atendimento ao cliente", etc. (Essas categorias podem ser personalizadas).
    * Requer a chave da API da Hugging Face.

* **traducao.py:**

    * Utiliza o modelo `facebook/mbart-large-50-many-to-many-mmt` para traduzir de português para inglês.
    * Traduz um comentário e imprime a tradução.

##   Observações

* Certifique-se de que sua chave da API da Hugging Face está configurada corretamente no arquivo `.env`.
* Os scripts fazem chamadas para a API da Hugging Face, portanto, é necessária uma conexão com a internet.
* A biblioteca `urllib3` é usada para desabilitar avisos de segurança, o que pode ser útil em alguns ambientes, mas considere as implicações de segurança em produção.

##   Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.

##   Licença

Este projeto é licenciado sob a [MIT License](LICENSE) (Adicione o arquivo LICENSE se você tiver um).