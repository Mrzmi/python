##import jieba
##f=open('data.txt','r',encoding='utf-8')
##lines=f.readlines()
##f.close()
##f=open('out.txt','w')
##for line in lines:
##    line=line.strip(' ')
##    print(line)
##    wordlist=jieba.lcut(line)
##    f.writelines('\n'.join(wordlist))
##  
##f.close()

import jieba
f=open('out.txt','r')
words=f.readlines()
##print(words)
f.close()
d={}
for w in words:
##    print(w)
    d[w[:-1]]=d.get(w[:-1],0)+1
print("{}".format(d["三国"]))
