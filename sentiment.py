from textblob import TextBlob

def analizar_sentimento(frase):
    polaridade = blob.sentiment.polarity
    if polaridade > 0.2:
        return 'positivo'
    elif polaridade < -0.2:
        return 'negativo'
    else:
        return 'neutro'