 # importar la libreria nltk
import nltk

 # desde nltk descargar el paquete stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')

lista_stopwords = stopwords.words('spanish')

 # imprimir la lista de stopwords
print(lista_stopwords)

Lista_stopwords_english = stopwords.words('english')
print(Lista_stopwords_english)
print(len(Lista_stopwords_english))









