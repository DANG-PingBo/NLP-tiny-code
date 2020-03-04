
import pprint

def load_corpus(path):
    lines=open(path).read().split("\n")
    return [line for line in lines]

def get_ngram(line, num):
    temp_ngram=[]
    for pos in range(0, len(line)-num+1):
        line_patch=line[pos:pos+num]
        temp_ngram.append(line_patch)
    return temp_ngram

#path="1w_corpus"
path="10"
lines=load_corpus(path)

get_ngram(lines[0],2)

class SimpleTrie:
    def __init__(self):
        self.dic={}
        self.end=True
    def add_dict(self,word):
        _=self.dic
        for c in word:
            if c not in _:
                _[c]={}
            _=_[c]
        if word in _:
            _[word]+=1
        else:
            _[word] = 1


from collections import defaultdict
def generate_grams(corpus, num):
    all_ngrams=[]
    for line in lines:
        ngrams=get_ngram(line,num)
        all_ngrams.extend(ngrams)


    return all_ngrams
gram_3=generate_grams(lines,3)
gram_2=generate_grams(lines,2)
all_grams=[]
all_grams.extend(gram_2)
all_grams.extend(gram_3)

def generate_trie(all_ngrams):
    simple=SimpleTrie()
    for one in all_ngrams:
        simple.add_dict(one)
    return simple
simple_trie=generate_trie(all_grams)
#print(simple_trie.dic)

pp=pprint.PrettyPrinter(width=50,compact=True)
#pp.pprint(simple_trie.dic)
def get_nextword(word):
    word_next = []
    words = []
    fre = []
    for one in simple_trie.dic[word]:
        #print(one, simple_trie.dic[word][one][word + one])
        words.append(one)
        fre.append(simple_trie.dic[word][one][word + one])

    dd = dict(zip(words, fre))
    dd = sorted(dd.items(), key=lambda x: x[1], reverse=True)
    return dd

word="你"
print("输入文字 {} 自动补全".format(word))
res=get_nextword(word)
print(res)


