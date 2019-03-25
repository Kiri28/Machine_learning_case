#First lemmatization example with pymystem3 
#And nltk- Russian stopwords
def lem(text):
    import nltk
    import pymystem3
    nltk.download('stopwords')
    from nltk.corpus import brown
    stop_words= nltk.corpus.stopwords.words('russian')
    
    mystem = pymystem3 . Mystem ( )
    z=text.split()
    lem=""
    for i in range(0,len(z)):
        if(mystem. lemmatize (z[i])[0] not in stop_words):
            lem =lem + " "+ mystem. lemmatize (z[i])[0]
    return(lem)


