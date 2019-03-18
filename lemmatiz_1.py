
def lem_1(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    import nltk,string
    from nltk.stem import  SnowballStemmer
    stemmer = SnowballStemmer('russian')
    stem=[stemmer.stem(w) for w in text.split()]
    stem= ' '.join(stem)
    stem1=''
    for p in stem:
        if(p not in punctuations):stem1+=p
    return(stem1)

