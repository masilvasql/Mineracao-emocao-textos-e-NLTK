import nltk

# nltk.download()  --- Comando para atualizar o nltk

base = [('eu sou admirada por muitos', 'alegria'),
        ('me sinto completamente amado', 'alegria'),
        ('amar e maravilhoso', 'alegria'),
        ('estou me sentindo muito animado novamente', 'alegria'),
        ('eu estou muito bem hoje', 'alegria'),
        ('que belo dia para dirigir um carro novo', 'alegria'),
        ('o dia está muito bonito', 'alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem', 'alegria'),
        ('o amor e lindo', 'alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns',
             'vou']  # stop Words manuais, utilizar apenas se diver algo personalizado, caso contrário, utilizar a do NLTK

stopWordsNLTK = nltk.corpus.stopwords.words('portuguese')  # lista de stop words do próprio NLTK

'''
def removeStopWords(texto):
    frases = []
    for (palavras, emocao) in texto:
        semStop = [p for p in palavras.split() if p not in stopWordsNLTK]
        frases.append((semStop, emocao))
    return frases
'''


# extrai o radical das frases e remove stop Words
def aplicaStemmer(texto):
    # RSLPStemmer -> stemmer específico para o português
    stemmer = nltk.stem.RSLPStemmer()
    frasesStemming = []
    for (palavras, emocao) in texto:
        comStemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopWordsNLTK]
        frasesStemming.append((comStemming, emocao))
    return frasesStemming


frasesComStemming = aplicaStemmer(base)
print(frasesComStemming)


def buscaPalavras(frases):
    todasAsPalavras = []
    for (palavras, emocao) in frases:
        todasAsPalavras.extend(palavras)
    return todasAsPalavras


palavras = buscaPalavras(frasesComStemming)


def buscaFrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras


frequencia = buscaFrequencia(palavras)
print(frequencia.most_common(50))


def buscaPalavrasUnicas(frequencia):
    freq = frequencia.keys()
    return freq


palavrasUnicas = buscaPalavrasUnicas(frequencia)
print(palavrasUnicas)

def extratorPalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavrasUnicas:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas


caracteristicasFrase = extratorPalavras(['am','nov','dia'])
print(caracteristicasFrase)

#nesta parte, o extratorPalavras, é passado só com o nome, sem fazer a chamada da função ()
baseCompleta = nltk.classify.apply_features(extratorPalavras, frasesComStemming)
