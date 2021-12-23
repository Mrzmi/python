##txt=open("命运.txt",'r').read()
##for ch in '，。？：':
##    txt=txt.replace(ch,'')
##d={}
##for ch in txt:
##    d[ch]=d.get(ch,0)+1
##ls=list(d.items())
##ls.sort(key=lambda x:x[1],reverse=True)
##a,b=ls[0]
##print("{}:{}".format(a,b))
##for i in ls:
##    print(i)


##txt=open("命运.txt",'r').read()
##for ch in '\n':
##    txt=txt.replace(ch,'')
##d={}
##for ch in txt:
##    d[ch]=d.get(ch,0)+1
##ls=list(d.items())
##ls.sort(key=lambda x:x[1],reverse=True)
##
##for i in range(10):
##    print(ls[i][1],end='##')
####    print(str(ls[i])[2],end='....')

txt=open("命运.txt",'r').read()
for ch in '\n':
    txt=txt.replace(ch,'')
d={}
for ch in txt:
    d[ch]=d.get(ch,0)+1
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
string=''
for i in range(len(ls)):
    s=str(ls[i]).strip("()")
    string=string+s[1]+':'+s[5:]+','
f=open("命运-频次排序.txt",'w')
f.write(string)
f.close()
