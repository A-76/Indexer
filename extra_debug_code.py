''''
    #These two functions are used for testing the delta encoding to reduce space

    def addToIndex(self,word,position):
        #Each token/word needs to have a list of documents that it is present in along with the tf-idf score.
        if(word not in self.index.keys()):
            self.index[word] = []
            new_entry = [self.docID,position]
            self.index[word].append(new_entry)

        else:
            #print(self.index[word])
            if(self.index[word][-1][0]  == self.docID):  #This line is going to check the docID of the previous insertion, if same as currID then add to same list
                        self.index[word][-1].append(position)
            else:                    
                new_entry = [self.docID,position]
                self.index[word].append(new_entry)
        return

    def delta_encode(self):
        #first index of all the lists 
        #remaining all indices of the list 
        self.encodedIndex = self.index
        for word in self.index:
            for i in range(len(self.index[word])):
                for j in range(2,len(self.index[word][i])):
                    self.encodedIndex[word][i][j] -=  self.encodedIndex[word][i][j-1] 

        print()
        for word in self.encodedIndex:
            print("The word is " + word + " and the list is ")
            print(self.encodedIndex[word])
            print()

        return


    def delta_decode(self):
        self.decodedIndex = self.encodedIndex
        for word in self.encodedIndex:
            for i in range(len(self.encodedIndex[word])):
                for j in range(2,len(self.encodedIndex[word][i])):
                    self.decodedIndex[word][i][j] +=  self.encodedIndex[word][i][j-1] 

        print()
        for word in self.decodedIndex:
            print("The word is " + word + " and the list is ")
            print(self.decodedIndex[word])
            print()


        return
    '''

    def displayIndex(self):
        print()
        for word in self.index:
            print("The word is " + word + " and the list is ")
            print(self.index[word])
            print()
        return


    def addToIndex(self,word,position):
        #Each token/word needs to have a list of documents that it is present in along with the tf-idf score.
        if(word not in self.index.keys()):
            self.index[word] = []
            new_entry = [self.docID,position]
            self.index[word].append(new_entry)

        else:
            #print(self.index[word])
            if(self.index[word][-1][0]  == self.docID):  #This line is going to check the docID of the previous insertion, if same as currID then add to same list
                    #print("The length of the list is ")
                    #print(self.index[word][-1])
                    if(len(self.index[word][-1])==2):
                        self.index[word][-1].append(position)

                    else:
                        val_to_add = position - self.index[word][-1][-1]
                        self.index[word][-1].append(val_to_add)
            else:                    
                new_entry = [self.docID,position]
                self.index[word].append(new_entry)
        return


    def read_index_from_file(self):
        #self.displayIndex()
        self.index.clear()
        if(not self.write_binary):
            with open("./TotalIndex.json", "r") as readfile:
                self.index = json.load(readfile)
        else:
            with open("./TotalIndex.json", "r") as outfile:
                x = outfile.read()
            self.index = self.decoder.decode(x)
        self.displayIndex()
        return

    def write_num_words_to_file(self):
        with open("./num_words.txt", "w") as outfile:
            outfile.write(str(len(self.index.keys())))
        return


    def write_index_to_file(self):
        if(not self.write_binary):
            json_object = json.dumps(self.index, indent = 4) 

            with open("./TotalIndex.json", "w") as outfile:
                outfile.write(json_object)
        else:
            a = self.encoder.encode(self.index)
            with open("./TotalIndex.json", "ab") as outfile:
                outfile.write(a)
        return

def compute_tf_idf_score(self):
        print("cocmputed the tf idf score")
        #Executed at the end once the entire corpus is indexed
        for word in self.index:
            num_document_occurrences = len(self.index[word])   #Number of documents in which the word occurred

            idf = np.log((self.docID+1)/num_document_occurrences)

            #now computing tf for every document in which the word occurred
            for document in self.index[word]:
                num_occurrences_in_doc =  len(document) - 1 # -1 because the first element in the list is the docID
                num_words_in_doc = self.document_info[document[0]]
                tf = float(num_occurrences_in_doc)/num_words_in_doc
                tf_idf = float(tf*idf)
                document.append(tf_idf)

        return 