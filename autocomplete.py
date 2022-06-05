# -*- coding: utf-8 -*-
"""

@authors: Alaa Farouk - Mariam Makram
"""

import re

ngramsNum = 3
trigram_list = {}
bigram_list = {}
probabilities = {}
count = 0
#nPredictions = 5
results = []


def prepareData():
    file = open(
        "dataset.txt",
        "r", encoding="UTF-8")
    dataset = file.read()
    file.close()
    return dataset


# preparing data for generating ngrams
def tokenizeText(text):
    text = text.lower()
    # tokenizing text to work on arabic and english words and numbers
    text = re.sub('[^\sa-zA-Z0-9ء-ي]', '', text)
    return text.split()

def calculateBigram(words_list):
    for term in range(0,len(words_list)):
        sentence = ' '.join(words_list[term:term + 2])
        if sentence not in bigram_list.keys():
             bigram_list[sentence] = 1
        else:
             bigram_list[sentence] += 1
        # counter += 1
def calculateTrigram(words_list):
    for term in range(0,len(words_list)-3):
        sentence = ' '.join(words_list[term:term + 3])
        if sentence not in trigram_list.keys():
             trigram_list[sentence] = 1
        else:
             trigram_list[sentence] += 1
    
def calculateProb():
    for sentence in trigram_list.keys():
        temp=splitSequence(sentence);
        #print(sentence,'    ' ,trigram_list[sentence],'       ',temp[0]+' '+temp[1])
        probabilities[sentence]=trigram_list[sentence]/bigram_list[temp[0]+' '+temp[1]]

def splitSequence(seq):
    return seq.split(" ")



def predict(inputt):
    predicted = []
   # nPred = nPredictions
    inputSequence = splitSequence(inputt)
    for sentence in probabilities.keys():
        if inputt in sentence:
            outputSequence = splitSequence(sentence)
            cont = False
            #print(sentence,"   ",sequence,"  ",  outputSequence)
            for i in range(0, len(inputSequence)):
                if outputSequence[i] != inputSequence[i]:
                    cont = True
                    break
            if cont:
                continue
            predicted.append((sentence, probabilities[sentence]))
    predicted.sort(key=lambda x: x[1], reverse=True)#sort by values reverse sorted
    noPrediction = False
    if len(predicted) == 0:
        print("No predicted words")
        numberofPredictions=0
        noPrediction = True
    else:
            numberofPredictions = len(predicted) 
    for i in range(0,  numberofPredictions):
        outputSequence = predicted[i][0].split(" ")#get key at a certain index
 #       print("%%%%%%%%%%%%%%%%%%5",outputSequence) 
        print(outputSequence[len(inputSequence)])
        results.append(outputSequence[len(inputSequence)]) # next predicted word
    return results, noPrediction, numberofPredictions        


dataset = prepareData()

words = tokenizeText(dataset)
calculateBigram(words)
calculateTrigram(words)
calculateProb()
#print(probabilities)
Input = input("Enter search words: ")
predict(Input)