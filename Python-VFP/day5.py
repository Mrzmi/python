##data=input()
##n=0
##age=0
##num=0
##while data:
##    n=n+1
##    ls=data.split()
##    age=age+int(ls[2])
##    if ls[1]=='男':
##        num=num+1
##    data=input()
##avg=age/n
##print("平均年龄是{:.2f} 男性人数是{}".format(avg,num))

names=input()
t.names.split()
d={}
for i in range(len(t)):
    d[t[i]]=d.get([t[i],0])+1
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for k in ls:
    print("{},{}".format(k[0],k[1])
