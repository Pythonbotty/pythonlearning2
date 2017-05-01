# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:12:12 2017

@author: yew
"""


import re
from nltk import WordNetLemmatizer
import get_synonym

#The core logic of the matcher
def levenshtein_distance(statement, other_statement):
    """
    Compare two statements based on the Levenshtein distance
    of each statement's text.

    For example, there is a 65% similarity between the statements
    "where is the post office?" and "looking for the post office"
    based on the Levenshtein distance algorithm.

    :return: The percent of similarity between the text of the statements.
    :rtype: float
    """
    import sys

    # Use python-Levenshtein if available
    try:
        from Levenshtein.StringMatcher import StringMatcher as SequenceMatcher
    except ImportError:
        from difflib import SequenceMatcher

    PYTHON = sys.version_info[0]

    # Return 0 if either statement has a falsy text value
    if not statement or not other_statement:
        return 0

    # Get the lowercase version of both strings
    if PYTHON < 3:
        statement_text = unicode(statement.lower())
        other_statement_text = unicode(other_statement.lower())
    else:
        statement_text = str(statement.lower())
        other_statement_text = str(other_statement.lower())

    similarity = SequenceMatcher(
        None,
        statement_text,
        other_statement_text
    )

    #Calculate a decimal percent of the similarity
    percent = round(similarity.ratio(), 2)

    return percent


# This gives a question to the program
a = "Hello how are you happy"
# This is the suggested answer of the program 
b = "Hello how are you happy"


#This is the Lemmatizer that brings words to the roots of the answers
wnl = WordNetLemmatizer()


senta =' '.join([wnl.lemmatize(i) for i in a.split()])
sentb =' '.join([wnl.lemmatize(i) for i in b.split()])

print senta
print sentb


#keywords = string_input.split()
keywords = ["glad"]


#try to find a synonym in sentence a for sentence b and add a score accordingly
for i in keywords:
    results = get_synonym.get_word_synonyms_from_sent(i, senta, sentb)*1.1
    print results

#if matched keywords can be found, add score. If not, continue on to check if synonym
#can be found. If still cannot, don't add to the score. 

for word in keywords:
    exactMatch = re.compile(r''.join(word), flags=re.IGNORECASE)
    matchedwords1 = exactMatch.findall(senta)
    if len(matchedwords1)>0:
        
        print matchedwords1
        
        exactMatch2= re.compile(r''.join(matchedwords1), flags=re.IGNORECASE)
        matchedwords2 = exactMatch2.findall(sentb)        
        print len(matchedwords2)
        distancefactor = len(matchedwords2)*1.1*results
        
        enhancedlevenshtein_distance = levenshtein_distance(a,b)*distancefactor
        print enhancedlevenshtein_distance
    elif len(matchedwords1)<=0:
        enhancedlevenshtein_distance = levenshtein_distance(a,b)*results
        print enhancedlevenshtein_distance
    else:
        enhancedlevenshtein_distance = levenshtein_distance(a,b)
