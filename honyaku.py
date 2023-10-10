

from deep_translator import GoogleTranslator
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
import pymsteams, re, time

translist=[]
translists=[]

f = open('masa3.txt', 'r')
intext = f.read()
f.close()



#split_text = [intext[x:x+100] for x in range(0, len(intext), 100)]
#print(split_text)


split_text = intext.split('. ')

for sourcetext in split_text:
    sourcetext = sourcetext.replace('\n+', ' ')
    sourcetext = re.sub('\s+', ' ', sourcetext)

    try:
        document = GoogleTranslator(source='auto',target='ja').translate(sourcetext)
    except:
        pass
    translist = document
    translist = str(sourcetext)+"\n"+ str(translist) + "\n\n"
    translists.append(translist)
    print(translist)


transresult = ''.join(translists)
print(transresult)


f = open('masaseihon3.txt', 'x')
f.write(transresult)
f.close()
