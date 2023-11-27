from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo" 
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negativo"
        
analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento("I'm happy")
print(resultado)