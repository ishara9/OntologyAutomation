import os
import nltk
import string
from nltk.corpus import stopwords
import collections
import string
from nltk.tag import StanfordNERTagger
from nltk import pos_tag, word_tokenize ,regexp_tokenize
from owlReady import OntologyMaker
from nltk.parse import stanford
from documentExtractor import *
from bagOfWords.bagOfWords import *
import re
import time
start_time = time.time()
# Download Stanford-ner and set path here
# os.environ['STANFORD_MODELS'] = 'C:/Users/HP/Desktop/FinalStage/Disease_NER/stanford-ner-2016-10-31'
os.environ['STANFORD_MODELS'] = '../stanford-ner-2016-10-31/classifiers'
# os.environ['CLASSPATH'] = "C:/Users/Ishara/Desktop/stanford-ner-2016-10-31"
os.environ['CLASSPATH'] = "../stanford-ner-2016-10-31"
# Set Java Path here
java_path = "C:/Program Files/Java/jre1.8.0_131/bin/java.exe"
os.environ['JAVAHOME'] = java_path

# Set trained model here
#st = StanfordNERTagger('ner-dis-cause-model.ser.gz')
st = StanfordNERTagger('dis-bio-ner-model-fix.gz')
# st = StanfordNERTagger('dis-bio-ner-model-huge.gz')

stop_words = set(stopwords.words("english"))


Abstracts=["" for x in range(6)]
Abses = list()

#abstract="Dengue fever is a disease caused by a family of viruses transmitted by mosquitoes. It is an acute illness of sudden onset that usually follows a benign course with symptoms such as headache, fever, exhaustion, severe muscle and joint pain, swollen lymph nodes (lymphadenopathy), and rash. The presence of fever, itchy rash, and headache (the "dengue triad") is characteristic of dengue. Other signs of dengue fever include bleeding gums, severe pain behind the eyes, and red palms and soles.Dengue (pronounced DENG-gay) can affect anyone but tends to be more severe in people with compromised immune systems. Because it is caused by one of five serotypes the dengue virus, it is possible to get dengue fever multiple times. However, an attack of dengue produces immunity for a lifetime to that particular viral serotype to which the patient was exposed."

#text=nltk.word_tokenize("Dengue fever is a disease caused by a family of viruses transmitted by mosquitoes. It is an acute illness of sudden onset that usually follows a benign course with symptoms such as headache, fever, exhaustion, severe muscle and joint pain, swollen lymph nodes (lymphadenopathy), and rash. The presence of fever, itchy rash, and headache is characteristic of dengue. Other signs of dengue fever include bleeding gums, severe pain behind the eyes, and red palms and soles.Dengue (pronounced DENG-gay) can affect anyone but tends to be more severe in people with compromised immune systems. Because it is caused by one of five serotypes the dengue virus, it is possible to get dengue fever multiple times. However, an attack of dengue produces immunity for a lifetime to that particular viral serotype to which the patient was exposed.")
# Abstracts[0]="Dengue is a  virus. You can get it if an infected mosquito bites you. Dengue does not spread from person to person. It is common in warm, wet areas of the world. Outbreaks occur in the rainy season. Dengue is rare in the United States."
# Abstracts[0]="Dengue has treatment which is panadol"
# Abstracts[1]="The right diagnosis and early treatment can slow joint damage and return you to your previous level of activity."
# Abstracts[0]="A child who has inattention associated with ADHD may have trouble paying attention to the task at hand. You can get it if an infected mosquito bites you. Dengue does not spread from person to person. It is common in warm, wet areas of the world. Outbreaks occur in the rainy season. Dengue is rare in the United States."
# Abstracts[0]="Without treatment, there may be a significant risk of intestinal cancer."
# Abstracts[1]="Inflammatory breast cancer is a rare type of cancer that often does not cause a breast lump or mass"
Abstracts[2]="Inflammatory breast cancer is a rare type of cancer that often does not cause a breast lump or mass"
# Abstracts[2]="Dengue fever (DF), an arbovirosis caused by Dengue viruses (DV, serotypes 1-4), is responsible for an increasing number of travel-related acute febrile illnesses due to population growth, climate changes, spreading by viremic travellers, and improved laboratory diagnosis. The presence of efficient vectors (mosquito Aedes albopictus) has also been described in temperate regions including italy which is considered the most heavily infected European country. Normally characterized by non-specific signs and symptoms, DF incidence is probably underestimated, especially in non-endemic countries, but the risk of severe forms is substantial. between august and november 2013, five DF patients (4 males, age 23-38) were observed in the Infectious Disease Clinic (University of Bari, Southern Italy). All had just returned from DF endemic areas (2 french polynesia, 3 dominican republic); 4/5 were hospitalized. Common clinical features included acute febrile syndrome, headache (2 with retro-orbital pain), rash (all patients), two with bleeding manifestations and one with gum bleeding. laboratory tests demonstrated leukopenia (4 patients), elevated liver enzymes (3 patients), and thrombocytopenia (1 patient). Serum samples for DV antibodies and RNA detection were analyzed by the Regional Arbovirosis Reference laboratory. Viral RNA was identified in 2/5 patients (DV-4) and seroconversion in the remaining cases. All patients made a complete recovery. Recent literature was reviewed, focusing on epidemiology and vector distribution (especially european and italian territories), pathogenesis, clinical features, diagnosis, and treatment including vaccine strategies. The occurrence of 5 DF cases during the period of highest vector activity (June-November) in Italy emphasizes the risk of local outbreaks in temperate regions. This paper highlights the importance of clinical alert for dengue also in non-endemic countries."
# Abstracts[3]="Dengue fever is caused by 1 of 4 different but related viruses. It is spread by the bite of mosquitoes, most commonly the mosquito Aedes aegypti, which is found in tropic and subtropic regions. This area includes parts of:"
# Abstracts[4]="Dengue (DEN-gee) fever is caused by four similar viruses spread by mosquitoes of the genus Aedes, which are common in tropical and subtropical areas worldwide."
# Abstracts[0]="Dengue has caused by mosquitoes"
# Abstracts[0]="late-infantile metachromatic leukodystrophy"

Abstracts2 = list()
def AbstactsFill():
    documents = documents_extract()
    # documents =list()
    # documents.append("C:/Users/HP/Desktop/project/pyNew/data/disease_relations.txt")
    doc_read =list()
    for document in documents:
        print("Current Document : "+ str(document))
        # doc_path ="C:/Users/HP/Desktop/project/crawlers/Spider-master/documents/answers/_breast_cancer_pictures_slideshow_article_htm_para_doc_answers.txt"
        file = open(document,"r", encoding="ISO-8859-1")
        # file = open(doc_path,"r")
        doc_read = file.readlines()
        for eachline in doc_read:
            # print(eachline)
            Abstracts2.append(eachline)
        file.close()
    return  doc_read

# class XX:
#     prev_word =''
#     prev_tag=''
# x=XX()




def getNER(sent):

    sen = []
    tagg = []
    # sen = "Hepatitis A virus can be transmitted to others by contaminated stools"
    sen=str(sent)

    # sen = 'Dengue is caused by mosquitoes'

    # print()
    beforeNouns = [];


    # Combining Chunked BOI contents
    #sp = []
    #print(st.tag('Dengue is caused by mosquitoes'.split()))
    # tagged=st.tag('Dengue is caused by mosquitoes'.split())
    print(sent)

    # regex_pattern = "[a-zA-Z'\"]+"
    # words = regexp_tokenize(sen, regex_pattern)
    # tagged = st.tag(words)

    # tagged = st.tag(word_tokenize(str(sen)))
    tagged = st.tag(sen.rstrip(".").split())
    print(tagged)
    tag = [["" for _ in range(2)] for _ in range(len(tagged))]
    #tag=[]
    # print(tag)
    k = 0
    for t in range(len(tagged)):
        # if not tagged with O (out of the chunk)
        if((tagged[t][1]!="O")):
            # if about to tag list is empty fill it with entity respect to the tag
            if(tag[k][0]==""):
                tag[k][0]=tagged[t][0]
            # if about to tag list is not empty append it with entity respect to the tag
            else:
                tag[k][0] = tag[k][0] +" "+ tagged[t][0]
            # Filter Bs and Is from initial tag make it single tagg e.g B-DISEASE converted into DISEASE
            tag[k][1] = str(tagged[t][1]).split("-")[1]
            if(t==len(tagged)-1):
                break
            # Identify chunks Before Inside pattern
            if(str(tagged[t+1][1]).startswith('I')):
                k=k;
            # if out of the chunk(not stating with I or starting with B) get next NE
            else:
                k=k+1;

    # print("tag: "+str(tag))

    # print("len tagged: "+str(len(tagged)))

    bigram_failed = True
    for n in range(0, len(tagged)):
        if((tagged[n][1]!="O")):
            tagg.append(tagged[n])
    # print(tagg)
    sp=[[0 for x in range(len(tagg))]]
    for n in range(0,k):
            # Catching two entities at a time
            if((str(tag[n][1])!='O')&(str(tag[n+1][1])!="")):
                sp=find_between(sen,tag[n][0],tag[n+1][0])
                regex = "([^.?!]*[\\?\\&\\!\\@\\$\\,\\&])"
                # print(sp)
                # print(re.match(regex, "& "))
                if re.match(regex, sp) is None:

                    final_rel=getRelationship(sp)
                    if final_rel != "none":
                        # print("final_rel "+str(final_rel))
                        relationship=""
                        for z in final_rel:
                           relationship=str(relationship)+""+str(z)
                        # print("tag correctly " + str(tag))
                        sub=tag[n][0]
                        obj=tag[n+1][0]
                        ontoUpdate(str(sub),str(tag[n][1]),str(obj),str(tag[n+1][1]),str(relationship))
                        bigram_failed = False

    if(bigram_failed==True):
        bow = BagOfWordsClassfication()
        predicted_word = str(bow.singlePredict(sen))
        # print(sen)
        # print("Prediction: "+str(predicted_word))
        relationship =bow.singlePredict(sen)
        if(relationship=='is_caused_by'):
            classification = 'cause'
            relationship = 'caused by'
        elif (relationship == 'cause_symptom'):
            classification = 'symptom'
            relationship = 'cause symptom'
        elif (relationship == 'has_treatment'):
            classification = 'treatment'
            relationship = 'has symptom'
        elif (relationship == 'disease_is'):
            classification = 'disease'
            relationship = 'disease is'
        # elif (relationship == 'other'):
        #     classification = 'treatment'
        #     relationship = 'has_treatment'

        else :
            return
        if (predicted_word != "other"):
            identified = chunker(str(sen),classification,relationship)
            # print("other Identified: "+str(identified))

        # print("tag n "+ str(tag))
        # Priorotizing tags
        sub = tag[0][0]
        sub_tag = tag[0][1]
        if classification != 'disease':
            for i,prority_tag in enumerate(tag):
                # print("prority_tag "+str(prority_tag[1]))
                if(prority_tag[1]=="DISEASE"):
                    sub = prority_tag[0]
                    sub_tag = prority_tag[1]

        for i in range (0,len(tag)-1):
            # print("TAG")
            # print(tag[i][0])
            if tag[i][0] in set(identified):
                identified.remove(tag[i][0])
        # print("Identified: " + str(identified))

        obj=""
        obj = " ".join(identified)
        # print(obj)
        # print(getattr(x, 'prev_word'))
        # print(getattr(x, 'prev_tag'))
        # print("Subject === "+str(sub))
        if sub!='' and obj!='':

            ontoUpdate(str(sub), str(sub_tag), str(obj), str(classification), str(relationship))
        # elif(XX.prev_word!=''):
        #     print("From Prev")
        #     ontoUpdate(XX.prev_word,XX.prev_tag , str(obj), str(classification), str(relationship))
    # print("print this "+str(tagg))
    # XX.prev_word=str(tag[0][0])
    # XX.prev_tag=str(tag[0][1])
                #print(tag[n])
                #print(relationship)
                #print(tag[n+1])
    #print(sp)
    #print(tagg)
def chunker(sent,classification, relationship):
    # grammar = "NP: {<JJ>+<NN|NNS>|<NN>}"
    # grammar = "NP: {<JJ>?<NN|NNS>}"
    if classification=="symptom":
        grammar = "NP: {<JJ>?<DT>?<NNP|NN>?<NN>" \
                  "|<IN>?<JJ>?<DT>?<NN.?>|<VBN><TO>?" \
                  "|<MD>?<VB>" \
                  "|<VB.?><JJ>" \
                  "|<VBZ><RB>" \
                  "|<IN>" \
                  "|<TO><NN.?>?<NN.?>}"
        # print("Symptom-grammar")
    elif classification=="treatment":
        grammar = "NP: {<JJ>?<DT>?<NNP|NN>?<NN>" \
                  "|<IN>?<JJ>?<DT>?<NN.?>" \
                  "|<VBN><TO>?" \
                  "|<MD>?<VB>" \
                  "|<VB.?><JJ>" \
                  "|<VBZ><RB>" \
                  "|<IN>" \
                  "|<TO><NN.?>?<NN.?>}"
        # print("treatment")
    else:
        grammar = "NP: {<JJ>?<NN.?>?<NN.?>" \
                  "|<VB.><IN>" \
                  "|<IN>" \
                  "|<VB.>?<JJ>}"
    grammar = "NP: {<DT>?<JJ>*<NN>}"



    pos_tags = nltk.pos_tag(word_tokenize(str(sent)))
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(pos_tags)
    def filt(x):
        return x.label()=='NP'
    nouns = list()
    for subtree in result.subtrees(filter =  filt): # Generate all subtrees
            i = 0
            raw =""
            for i in range(0,len(subtree)):
                raw += subtree.leaves()[i][0] + " "
                # print(subtree.leaves()[i][0]+subtree.leaves()[i+1][0])
            nouns.append(raw.rstrip(" "))
    # print(nouns)
    return nouns

relation=[]
verbsRelations=[]
# afterNouns = [token for token, pos in nltk.pos_tag(str(after)) if pos.startswith('N')]
def getRelationship(relationship):
    relation=str(relationship)
    if(relation.__contains__("caused by")
           |relation.__contains__("spread by")
           |relation.__contains__("occurs by")):
        return "caused by"
    elif(relation.__contains__("is a")
             |relation.__contains__("is euivalent to")
             |relation.__contains__("also known as")
             |relation.__contains__("is also called")):
        return  "is"
    elif(relation.__contains__("such as")
             |relation.__contains__("for example")
             |relation.__contains__("including")
             |relation.__contains__("for instance")
             |relation.__contains__("especially")
             |relation.__contains__("e.g.")):
        return "similar to"

    else:
        verbsRelations = [token for token, pos in nltk.pos_tag(word_tokenize(str(relation))) if (pos.startswith(('V'))|pos.startswith(('R')))]

        # Maximum relation length
        if len(verbsRelations)>6:
            return  "none"

        if " ".join(verbsRelations) == "":
            return "none"
        else:

            return (" ".join(verbsRelations))


mainClasses = set()
mainProperties = list()
classifiedWords = list()
relationshipSet = list()

def ontoUpdate(sub,subType,obj,objType,rela):
    cw=[[sub.rstrip('.'),subType],[obj.rstrip('.'),objType]]
    rs=[[sub.rstrip('.'),rela.rstrip(' &'),obj.rstrip('.')]]
    print(cw)
    print(rs)
    # mainClasses.add('cause','disease','biology','nn','treatment','microorgnism','symptom')
    AllClasses = ['cause', 'disease', 'biology', 'nn', 'microorganism', 'symptom']
    # mainClasses.add(cw[0][1].lower())
    # mainClasses.add(cw[1][1].lower())
    #
    # mainProperties.append([rs[0][1].lower(),cw[0][1].lower(),cw[1][1].lower()])
    #
    # classifiedWords.append([cw[0][0].lower(),cw[0][1].lower()])
    # classifiedWords.append([cw[1][0].lower(), cw[1][1].lower()])
    #
    # relationshipSet.append([ rs[0][0].lower(), rs[0][1].lower(), rs[0][2].lower()])

    mainClasses.add(str(re.sub('[^a-zA-Z]+', '_', cw[0][1].lower())).rstrip("_"))

    mainClasses.add(str(re.sub('[^a-zA-Z]+', '_', cw[1][1].lower()).rstrip("_")))

    if str(re.sub('[^a-zA-Z]+', '_', cw[0][0].lower()).rstrip("_")) in AllClasses:
        cw[0][0]=cw[0][0]+"_sub"
        rs[0][0] = rs[0][0] + "_sub"
    if str(re.sub('[^a-zA-Z]+', '_', cw[1][0].lower()).rstrip("_")) in AllClasses:
        cw[0][0]=cw[1][0]+"_sub"
        rs[0][2] = rs[0][2] + "_sub"
    if str(re.sub('[^a-zA-Z]+', '_', rs[0][1].lower()).rstrip("_")) in AllClasses:
        rs[0][1]= rs[0][1] +"_sub"

    mainProperties.append([str(re.sub('[^a-zA-Z]+', '_', rs[0][1].lower()).rstrip("_")),
                           str(re.sub('[^a-zA-Z]+', '_', cw[0][1].lower()).rstrip("_")),
                           str(re.sub('[^a-zA-Z]+', '_', cw[1][1].lower().rstrip("_")))])



    classifiedWords.append([str(re.sub('[^a-zA-Z]+', '_', cw[0][0].lower()).rstrip("_")),
                            str(re.sub('[^a-zA-Z]+', '_', cw[0][1].lower()).rstrip("_"))])
    classifiedWords.append([str(re.sub('[^a-zA-Z]+', '_', cw[1][0].lower()).rstrip("_")),
                            str(re.sub('[^a-zA-Z]+', '_', cw[1][1].lower()).rstrip("_"))])

    relationshipSet.append([str(re.sub('[^a-zA-Z]+', '_', rs[0][0].lower()).rstrip("_")),
                            str(re.sub('[^a-zA-Z]+', '_', rs[0][1].lower()).rstrip("_")),
                            str(re.sub('[^a-zA-Z]+', '_', rs[0][2].lower()).rstrip("_"))])

    # print(mainClasses)
    # print(mainProperties)
    # print(classifiedWords)
    # print(relationshipSet)

    saveToOntology()
    mainClasses.clear()
    del mainProperties[:]
    del classifiedWords[:]
    del relationshipSet[:]



owl = OntologyMaker()
def saveToOntology():

    # mainClasses = ['Disease', 'Cure', 'Cause', 'Prevention', 'Symptom', 'Treatment']
    # # Introduce properties in list with domain and range
    # mainProperties = [['data Prop', 'Disease', 'Prevention'], ['has_cause', 'Disease', 'Symptom']]
    # # Introduce word concepts(instances) with classifications
    # classifiedWords = [['influenza', 'Disease'], ['HIV', 'Disease'], ['arthritis', 'Disease'], ['arthritis', 'Disease'],
    #                    ['arthritis', 'Disease'], ['arthritis', 'Disease'],
    #                    ['immune_system_dysfunction', 'Symptom'], ['injury', 'Cause']]
    # # semantic template
    # relationshipSet = [['arthritis', 'has_cause', 'injury']]

    owl.ClassDefiner(mainClasses)
    owl.PropertyDefiner(mainProperties)
    owl.updateClassifications(classifiedWords)
    owl.relationshipBuilder(relationshipSet)
    owl.saveOnto()

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


# for ab in Abstracts:
#     sentence=[]
#     sentence=nltk.sent_tokenize(ab)
#     for se in sentence:
#         if len(se) > 250:
#             continue
#         getNER(se)
AbstactsFill()
for ab in Abstracts2:
    sentence=[]
    sentence=nltk.sent_tokenize(ab)
    for se in sentence:
        if len(se) > 250:
            continue
        getNER(se)


print(" ")
print(list(mainClasses))
print(list(mainProperties))
print(list(classifiedWords))
print(list(relationshipSet))
# saveToOntology()
print("--- %s seconds ---" % (time.time() - start_time))
