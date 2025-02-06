# finalproject.py (final project pI and pII)
#
#

import math


def clean_text(txt):
    '''helper function for the TextModel class, takes a string of text txt as a parameter and 
    returns a list containing the words in txt after it has been “cleaned”'''
    txt = txt.lower()
    for word in txt:
        for symbol in """.,?"'!;:""":
            txt = txt.replace(symbol, "")
    txt = txt.split()

    return txt
#final project part III
def stem(s):
    '''accepts a string as a parameter and returns the strings stem'''
    
    special_cases = {"better":"better","queue":"queue","northwest":"northwest","southwest":"southwest"}
    
    #special cases
    if s in special_cases:
        s = special_cases[s]
    #words ending in e
    elif s[-1] == "e":
        if len(s) >=4:
            s = s[:-1]
    #words ending in y
    elif s[-1] == "y":
        s = s[:-1] + "i"  
    #plural
    elif s[-2:] == "es":
        s = s[:-2]
    elif s[-1] == "s":
        s = s[:-1]
    #ing case
    elif s[-3:] == "ing" and len(s)>=6: #bring, sing, ring
        #double not l
        if s[-5] == s[-4] and s[-4] != 'l':
            s = s[:-4]
        #regular and double l
        else:
            s = s[:-3]
    #ed and er cases
    elif s[-2:] == 'ed' or s[-2:] == 'er':
        if len(s) >= 5:
            if s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
    #est case
    elif s[-3:] == "est" and len(s) >=6: # best, zest, crest
        #double not l
        if s[-4]== s[-5] and s[-4] == 'l': #fullest
            s = s[:-4]
        else:
            s = s[:-3]
    #ly case
    elif s[-2:] == "ly" and len(s) >= 4: 
        #double l
        if s[-3] == s[-2]:
            s = s[:-1]
        else:
            s = s[:-2]
        #ful case
    elif s[-3:] == "ful":
        s = s[:-3]
    #tion and sion cases
    elif s[-4:] == "tion" or s[-4:] == "sion":
        s = s[:-3]
    else:
        s = s
        
    return s
        
#final project part IV
def compare_dictionaries(d1, d2):
    '''take two feature dictionaries d1 and d2 as inputs and return their log similarity score'''
    if d1 == {}:
        return -50
    
    #find total # of words in d1
    total_words = 0
    for s in d1:
        total_words += d1[s]

    #test if word is in d1 and d2
    probabilities = []
    for word in d2:
        if word in d1:
            numerator = d1[word]
            percentage = numerator / total_words
            log = math.log(percentage)
            probability = log * d2[word]
            probabilities += [probability]
        else:
            percentage = 0.5/total_words
            log = math.log(percentage)
            probability = log * d2[word]
            probabilities += [probability]
            
    score = sum(probabilities)
    return score




class TextModel:
    '''a data type for a model of a body of text'''
    def __init__(self, model_name):
        '''constructs a new TextModel object by accepting a string model_name as a parameter'''
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.adjacent_words = {}
        #to connect words - self.adjacent_words[w1+"_"+w2] = 1
        
    def __repr__(self):
        '''returns a string that includes the name of the model + the 
        sizes of the dictionaries for each feature of the text'''
        
        s = "text model name: " + self.name + "\n"
        s += "  number of words: " + str(len(self.words)) + "\n"
        s += "  number of word lengths: " + str(len(self.word_lengths)) + "\n"
        s += "  number of stems: " + str(len(self.stems)) + "\n"
        s += "  number of sentence lengths: " + str(len(self.sentence_lengths)) + "\n"
        s += "  number of adjacent word : " + str(len(self.adjacent_words)) + "\n"
        return s
    
    def add_string(self, s):
        """Analyzes the string s and adds its pieces
           to all of the dictionaries in this text model.
        """
        #split paragraph into sentences
        sl = s[:]
        sl = sl.split()
        s_e_w = 0
        for w in range(len(sl)):
            if sl[w][-1] in "!.?":
                new_s_e_w = w + 1 #plus 1 because indices start at 0 not 1
                s_length = new_s_e_w - s_e_w
                if s_length not in self.sentence_lengths:
                    self.sentence_lengths[s_length] = 1
                else:
                    self.sentence_lengths[s_length] += 1
                s_e_w = new_s_e_w
                
        
        # Add code to clean the text and split it into a list of words.
        # *Hint:* Call one of the functions you have already written!
        word_list = clean_text(s)
        #self.words and self.stems
        for w in word_list:
            # Update self.words to reflect w
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
            stems = stem(w)  
            if stems not in self.stems:
                self.stems[stems] = 1
            else:
                self.stems[stems] += 1
    
            # Add code to update self.word_length
        for word in range(len(word_list)):
            if len(word_list[word]) not in self.word_lengths:
                self.word_lengths[len(word_list[word])] = 1
            else:
                self.word_lengths[len(word_list[word])] += 1
                
                
        #my feature
        for i in range(len(word_list)-1):#last word doesn't have an adj word
            adj = word_list[i] + "_" + word_list[i + 1]
            if adj not in self.adjacent_words:
                self.adjacent_words[adj] = 1
            else:
                self.adjacent_words[adj] += 1
    
                
    def add_file(self, filename):
        '''adds all of the text in the file identified by filename to the model'''
        file = open(filename, 'r', encoding='utf8', errors='ignore')
        
        for line in file:
            self.add_string(line)
            
    #part II
    def save_model(self):
        '''saves the TextModel object self by writing its various feature dictionaries to files'''
        word = self.words
        file = open(self.name + '_' + 'words', "w")
        file.write(str(word))             
        file.close()
        
        length = self.word_lengths
        file2 = open(self.name + '_' +'word_lengths', "w")
        file2.write(str(length))             
        file2.close()
        
        length1 = self.sentence_lengths
        file3 = open(self.name + '_' +'sentence_lengths', "w")
        file3.write(str(length1))             
        file3.close()
        
        stem = self.stems
        file4 = open(self.name + '_' +'stems', "w")
        file4.write(str(stem))             
        file4.close()
        
        adj = self.adjacent_words
        file5 = open(self.name + '_' +'adjacent_words', "w")
        file5.write(str(adj))             
        file5.close()
        
    def read_model(self):
        '''reads the stored dictionaries for the called TextModel object from their 
        files and assigns them to the attributes of the called TextModel'''
        file = open(self.name + '_' + 'words', "r")    
        d_str = file.read()           
        file.close()
        self.words = dict(eval(d_str))      
        
        file2 = open(self.name + '_' +'word_lengths', "r")
        d_str = file2.read()           
        file2.close()
        self.word_lengths = dict(eval(d_str))
        
        file3 = open(self.name + '_' +'sentence_lengths', "r")
        d_str = file3.read()           
        file3.close()
        self.sentence_lengths = dict(eval(d_str))
        
        file4 = open(self.name + '_' +'stems', "r")
        d_str = file4.read()           
        file4.close()
        self.stems = dict(eval(d_str))
        
        file5 = open(self.name + '_' +'adjacent_words', "r")
        d_str = file5.read()           
        file5.close()
        self.adjacent_words = dict(eval(d_str))
    
    #part IV
    def similarity_scores(self, other):
        '''computes and returns a list of log similarity scores measuring the 
        similarity of self and other – one score for each type of feature'''
        scores = []
        #words
        words_score = compare_dictionaries(other.words, self.words)
        scores += [words_score]
        #word_lengths
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        scores += [word_lengths_score]
        #stems
        stems_score = compare_dictionaries(other.stems, self.stems)
        scores += [stems_score]
        #sentence_lengths
        sentence_lengths_score =  compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        scores += [sentence_lengths_score]
        #adjacent_words
        adjacent_words_score = compare_dictionaries(other.adjacent_words, self.adjacent_words)
        scores += [adjacent_words_score]
        
        return scores
    
    def classify(self, source1, source2):
        '''compares self's scores to two other “source” TextModel object's 
        and determines which of these is the more likely source of self'''
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        print("scores for ", source1.name, ": ", scores1)
        print("scores for ", source2.name, ": ", scores2)
        
        s1= 0
        s2 = 0
        
        #finds which source wins the most sets
        for x in range(len(scores1)):
            if scores1[x] > scores2[x]:
                s1 += 1
            else:
                s2 += 1
        if s2 > s1:
            print(self.name, "is more likely to have come from", source2.name )
        else:
            print(self.name, "is more likely to have come from", source1.name )
            
def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')


    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
    
def run_tests():
    """ your docstring goes here """
    source1 = TextModel('ncis')
    source1.add_file('ncis_s5.txt')
    
    source2 = TextModel('criminal minds')
    source2.add_file('cm_s5.txt')
    
    new1 = TextModel('cme3')
    new1.add_file('cm_ep3.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('ncise3')
    new2.add_file('ncis_ep3.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('arch.essay')
    new3.add_file('Essay_1_Final.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('syllabus')
    new4.add_file('syllabus.txt')
    new4.classify(source1, source2)
    
    new5 = TextModel('test')
    new5.add_file('cm_s5.txt')
    new5.classify(source1, source2)
    
    
        
        
        


   
        
        
            
    
    
        




