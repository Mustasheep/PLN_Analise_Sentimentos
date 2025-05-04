import argparse
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import re
import unicodedata
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import gensim.downloader as api

def text_preprocessing(text):
    """Preprocessa um texto removendo caracteres especiais,
    removendo números, stop words e lematizando."""
    try:
        text = unicodedata.normalize('NFD', text)
        text = ''.join([c for c in text if not unicodedata.combining(c)])
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        text = re.sub(r'\s+', ' ', text)
        tokens = word_tokenize(text)

        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]

        lemmatizer = WordNetLemmatizer()
        tokens_sl = [lemmatizer.lemmatize(token) for token in tokens]

        return " ".join(tokens_sl)
    except Exception as e:
        print(f"Erro no pre-processamento: {e}")
        return ""

def vectorize_review(review, model):
    """Converte um comentário em um vetor usando word embeddings."""
    words = word_tokenize(review)
    words = [word for word in words if word in model]
    if not words:
        return np.zeros(model.vector_size)
    try:
        word_vectors = [model[word] for word in words]
        review_vector = np.mean(word_vectors, axis=0)
        return review_vector
    except Exception as e:
        print(f"Erro ao vetorizar review: {e}")
        return np.zeros(model.vector_size)

def analisar_sentimento(texto, modelo, modelo_word2vec):
    """Analisa o sentimento de um texto."""
    texto_preprocessado = text_preprocessing(texto)
    if not texto_preprocessado:
        return "Erro no pre-processamento"
    
    vetor_texto = vectorize_review(texto_preprocessado, modelo_word2vec)
    
    sentimento = modelo.predict([vetor_texto])[0]
    return sentimento

def main():
    """Função principal para executar a análise de sentimentos."""
    parser = argparse.ArgumentParser(description="Analisa o sentimento de um texto.")
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-t", "--text", help="Texto para análise.")
    group.add_argument("-f", "--file", help="Caminho para o arquivo de texto.")
    args = parser.parse_args()

    # Checando dependências
    WordNetLemmatizer()
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('punkt')
    nltk.download('punkt_tab')

    # Carregando modelo e word embeddings
    print("Carregando modelo...")
    modelo = LogisticRegression()
    try:
        modelo = pd.read_pickle("../modelo_treinado.pkl") 
    except FileNotFoundError:
        print("Erro: Arquivo 'modelo_treinado.pkl' não encontrado.")
        return
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return

    print("Carregando word embeddings...")
    try:
        modelo_word2vec = api.load("glove-twitter-50")
    except Exception as e:
        print(f"Erro ao carregar word embeddings: {e}")
        return

    texto_para_analise = ""

    if args.text:
        texto_para_analise = args.text
    elif args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                texto_para_analise = f.read()
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado.")
            return
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            return

    if texto_para_analise:
        sentimento = analisar_sentimento(texto_para_analise, modelo, modelo_word2vec)
        print(f"Sentimento: {sentimento}")

if __name__ == "__main__":
    main()
