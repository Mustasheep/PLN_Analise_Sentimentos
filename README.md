[![Licença](https://img.shields.io/badge/licença-MIT-verde.svg)](LICENSE) 
# Análise de Sentimentos em Textos com Python e NLTK

Este projeto implementa um sistema de análise de sentimentos utilizando técnicas de Processamento de Linguagem Natural (PLN) e a biblioteca NLTK em Python. O objetivo é identificar e classificar a polaridade (positiva, negativa) de textos, como comentários de redes sociais, reviews de produtos, etc.

Inicialmente, suporta apenas textos em inglês.

## Sumário
*   [1. Visão Geral](#1-visão-geral)
*   [2. Funcionalidades](#2-funcionalidades)
*   [3. Estrutura](#3-estrutura)
*   [4. Tecnologias Utilizadas](#4-tecnologias-utilizadas)
*   [5. Instalação](#5-instalação)
*   [6. Como Usar](#6-como-usar)
*   [7. Contribuição](#7-contribuição)
*   [8. Licença](#8-licença)
*   [9. Autor](#9-autor)


## 1. Visão Geral
Este projeto visa criar um sistema de análise de sentimentos robusto e preciso, capaz de processar textos em inglês e identificar a emoção predominante (positiva, negativa). A análise de sentimentos tem diversas aplicações, como:
*   Monitoramento de redes sociais para entender a opinião pública sobre um produto ou marca.
*   Análise de reviews de clientes para identificar pontos fortes e fracos de um serviço.
*   Detecção de fake news e discurso de ódio.

Este projeto utiliza a biblioteca NLTK, uma das mais populares para PLN em Python, e técnicas de aprendizado de máquina para treinar um modelo capaz de classificar sentimentos em textos.


## 2. Funcionalidades
*   **Análise de Sentimentos:** Classifica textos em duas categorias: positivo e negativo.
*   **Extensibilidade:** Código modular e fácil de adaptar para diferentes casos de uso.


## 3. Estrutura
```
PLN_Analise_Sentimentos/
├── notebooks/
│ ├── 01_Dataset.ipynb
│ ├── 02_EDA_Preprocessamento.ipynb
│ └── 03_Treinamento_e_Aplicação.ipynb
├── scripts/
│ └── analisar_sentimento.py
├── README.md 
├── LICENSE
├── modelo_treinado.pkl
└── requirements.txt
```

## 4. Tecnologias Utilizadas
*   [Python](https://www.python.org/) - Linguagem de programação principal.
*   [NLTK](https://www.nltk.org/) - Biblioteca para Processamento de Linguagem Natural.
*   [Scikit-learn](https://scikit-learn.org/) - Biblioteca para aprendizado de máquina.
*   [Pandas](https://pandas.pydata.org/) - Biblioteca para manipulação e análise de dados.

## 5. Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/Mustasheep/PLN_Analise_Sentimentos.git
    cd PLN_Analise_Sentimentos/
    ```
2.  Crie um ambiente virtual (recomendado):
    ```bash
    python -m venv venv
    #source venv/bin/activate --descomente para usar em Linux/IOs
    venv\Scripts\activat
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## 6. Como Usar

Para executar a análise de sentimentos em um texto, utilize o seguinte comando:

```bash
cd scripts
python analisar_sentimento.py --text "I loved this movie, it's magnificent."
```
Resultado:
```bash
Sentimento: Positivo
```
Você também pode analisar um arquivo de texto:
```bash
python analisar_sentimento.py --file arquivo.txt
```

## 7. Contribuição

Contribuições são sempre bem-vindas! Se você tiver alguma sugestão, encontrou um bug ou gostaria de adicionar uma nova funcionalidade, siga os seguintes passos:

1.  Faça um fork do repositório.
2.  Crie uma branch com sua alteração: `git checkout -b minha-alteracao`
3.  Faça as alterações e adicione commits com mensagens descritivas.
4.  Envie um pull request.

## 8. Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

## 9. Autor

*   [LinkedIn](https://www.linkedin.com/in/thiago-mustasheep/)

---------------
[Início](#análise-de-sentimentos-em-textos-com-python-e-nltk)
