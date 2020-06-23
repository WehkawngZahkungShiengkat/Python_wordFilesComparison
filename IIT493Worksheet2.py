# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 22:22:40 2019

@author: We-z (5905040063)
"""

import re

def findRecall(List1,List2): #function for calculating the recall of the two input strings and return the result
    collection1 = {}
    collection2 = {}
    lineresult = 0
    count = 0
    
    for i1 in List1:
        collection1[i1] = collection1.get(i1,0) + 1
    for i2 in List2:
        collection2[i2] = collection2.get(i2,0) + 1
    
    for p in collection1.keys():
        if p in collection2.keys():
            #updated version
            if (collection2[p]<=collection1[p]):
                lineresult += collection2[p]
            else:
                lineresult += collection1[p]
        count += collection1[p]
            
            #old version has been detected incorrect and I have corrected it
            #result = (collection2[p]/collection1[p]) if (collection2[p]/collection1[p]) <= 1 else 1
            #lineresult += result
            #count += 1
            
    return (lineresult/count)


def findPrecise(List1,List2): #function for calculating the Precision of the two input strings and return the result
    collection1 = {}
    collection2 = {}
    match = 0
    count = 0
    
    #correct = 0
    #incor = 0
    
    for i1 in List1:
        collection1[i1] = collection1.get(i1,0) + 1
    for i2 in List2:
        collection2[i2] = collection2.get(i2,0) + 1
    
    for p in collection1.keys():
        if p in collection2.keys():
            #updated version
            if (collection2[p]<=collection1[p]):
                match += collection2[p]
            else:
                match += collection1[p]
    for q in collection2.keys():
        count += collection2[q]
        
        #old version is working and correct but I update it to shorter code and take off unneccessary code
            #if (collection2[p] <= collection1[p]):
             #   correct += collection2[p]
            #else:
             #   correct += collection1[p]
              #  incor += (collection2[p] - collection1[p])
                
    #for q in collection2.keys():
     #   if q not in collection1.keys():
      #      incor += collection2[q]
    #alltotal = correct + incor
            
    return (match/count)


def findTrigram(In1,In2): #function for matching trigram pair of the two input strings and return the match pairs number
    j = 0
    list1 = []  
    list2 = []
    
    #this is the final updated version for Trigrams and work perfectly, in this version I use tuples in a list to compare and then remove the match one
    for cl in range(len(In1)-2):
        t = In1[cl],In1[cl+1],In1[cl+2]
        list1.append(t)
    for cl1 in range(len(In2)-2):
        t2 = In2[cl1],In2[cl1+1],In2[cl1+2]
        list2.append(t2)

    for nx in list1:
        if nx in list2:
            j += 1
            #print(nx)  to see what trigrams are match
            list2.remove(nx)
    
    
    
    #this is my new updated version for trigram and but it doesn't work correctly. Therefore, I came up with the above version which fix all the problems fix in this code
    #for x in range(len(In1)-2):
     #   for y in range(x,len(In2)-2):
      #      if (y+2 <= len(In2)):
       #         if ((In1[x],In1[x+1],In1[x+2]) == (In2[y],In2[y+1],In2[y+2])):
        #            j += 1
         #           break
          #  if (y > x+2):break    this code limit the distance or how far we compare the nearest trigram
    
    #this is the old version and it only check the exact trigram with the exam sequence by room no. (in the case x)
    #minlen = min(len(In1),len(In2))
    #for x in range(minlen-2):
    #    if ((In1[x],In1[x+1],In1[x+2]) == (In2[x],In2[x+1],In2[x+2])):
    #        j += 1        
    
    return j


def simplify(In1): #function for simplify the input string into simple lowercase words without comma and fullstop
    In1 = In1.lower()
    In1 = re.sub('[,\.\"]',"", In1)
    ShortedWords = {"this's":"this is","that's":"that is","those're":"those are","these're":"these are",
                "there's":"there is","here's":"here is","he's":"he is","she's":"she is",
                "they're":"they are","you're":"you are","we're":"we are","i'm":"i am","it's":"it is"}
    for a in ShortedWords:
        In1 = re.sub(a,ShortedWords[a],In1)
    #This above code will do mostly correctly but it can also make a mistake like changing a name which end with above dictionary's keys value.
    #For example - it could change Mohere's to Mohere is - where Mohere is a person's name and Mohere's and Mohere is has have different meaning.
    In1 = In1.split()
    
    return In1


def simplifyNoSW(In1): #function for simplify the input string into simple lowercase words without comma and fullstop, and also eliminate the Stopwords
    with open("Stopwords.txt","r") as SWfile: #get a list of stopwords from a file
        StopWords =SWfile.read()
    SWfile.close()
    StopWords = StopWords.split(",")
    In1 = In1.lower()
    
    #in the StopWords list i then space take a room and replace that with nothing (delete) but there can be a problem because it can also delete 'i' from a word end with 'i'.
    #I don't know how to solve that as I try to lowercase every character but 'i'. ANd I don't know how to do it. If I can do that that problem might be solve by insert 'I' and space as a room in a list.
    
    for z in range(len(StopWords)):
        In1 = re.sub(StopWords[z]," ",In1)
    
    In1 = re.sub('[,\.\"]',"", In1)
    ShortedWords = {"this's":"this is","that's":"that is","those're":"those are","these're":"these are",
                "there's":"there is","here's":"here is","he's":"he is","she's":"she is",
                "they're":"they are","you're":"you are","we're":"we are","i'm":"i am","it's":"it is"}
    for a in ShortedWords:
        In1 = re.sub(a,ShortedWords[a],In1)
    #This above code will do mostly correctly but it can also make a mistake like changing a name which end with above dictionary's keys value.
    #For example - it could change Mohere's to Mohere is - where Mohere is a person's name and Mohere's and Mohere is has have different meaning.
    In1 = In1.split()
    
    return In1


try: #Use try to prevent any type of error
    with open("OriginTranEng.txt","r") as OEfile:
        OriEng = OEfile.read()
    OEfile.close()
    OriEngs = simplify(OriEng)
    OriEngsNoSW = simplifyNoSW(OriEng)
    
    with open("Tran1Google.txt","r") as TEfile1:
        TranG = TEfile1.read()
    TEfile1.close()
    TranGs = simplify(TranG)
    TranGsNoSW = simplifyNoSW(TranG)
    
    with open("Tran2Bing.txt","r") as TEfile2:
        TranB = TEfile2.read()
    TEfile2.close()
    TranBs = simplify(TranB)
    TranBsNoSW = simplifyNoSW(TranB)
    
    with open("Tran3Translate.com.txt","r") as TEfile3:
        TranT = TEfile3.read()
    TEfile3.close()
    TranTs = simplify(TranT)
    TranTsNoSW = simplifyNoSW(TranT)
    
    tR1 = findRecall(OriEngs,TranGs)
    tR2 = findRecall(OriEngs,TranBs)
    tR3 = findRecall(OriEngs,TranTs)
    
    tR1NoSW = findRecall(OriEngsNoSW,TranGsNoSW)
    tR2NoSW = findRecall(OriEngsNoSW,TranBsNoSW)
    tR3NoSW = findRecall(OriEngsNoSW,TranTsNoSW)
    
    tP1 = findPrecise(OriEngs,TranGs)
    tP2 = findPrecise(OriEngs,TranBs)
    tP3 = findPrecise(OriEngs,TranTs)
    
    tP1NoSW = findPrecise(OriEngsNoSW,TranGsNoSW)
    tP2NoSW = findPrecise(OriEngsNoSW,TranBsNoSW)
    tP3NoSW = findPrecise(OriEngsNoSW,TranTsNoSW)
    
    tT1 = findTrigram(OriEngs,TranGs)
    tT2 = findTrigram(OriEngs,TranBs)
    tT3 = findTrigram(OriEngs,TranTs)
    
    #the below print will output nice and clear result
    print("Compare To Origin Translate \t\tRecall \t\tRecall \t\tPrecision \tPrecision \tTrigrams")
    print("\t\t\t\t\tWith Stopwords \tNo Stopwords \tWith Stopwords \tNo Stopwords")
    print("Google Translate \t\t\t%.2f \t\t%.2f \t\t%.2f \t\t%.2f \t\t%.2f" %(tR1,tR1NoSW,tP1,tP1NoSW,tT1))
    print("Bing Translate \t\t\t\t%.2f \t\t%.2f \t\t%.2f \t\t%.2f \t\t%.2f" %(tR2,tR2NoSW,tP2,tP2NoSW,tT2))
    print("Translate.com \t\t\t\t%.2f \t\t%.2f \t\t%.2f \t\t%.2f \t\t%.2f" %(tR3,tR3NoSW,tP3,tP3NoSW,tT3))
except:
    print("Sorry! Something's wrong. Error has been detected")


    
