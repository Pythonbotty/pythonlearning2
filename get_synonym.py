# this is the function to help to attain synonyms from wordnet 







from nltk.corpus import wordnet

def get_word_synonyms_from_sent(word, senta, sentb):
    word_synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemma_names():
            if lemma in senta and lemma != word:
                word_synonyms.append(lemma)
    
    word_synonyms_match =[]
    for wording in word_synonyms:
        if wording in sentb:
            word_synonyms_match.append(wording)
    return len(word_synonyms_match)




