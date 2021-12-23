##t=eval(input())
##if t>10 and t<pow(10,8):
##    print("{:=^25}".format(t))
##else:
##    print("输入错误")

##s=input("请输入一个正整数")
##cd=0
##for c in s:
##    cd +=int(c)
##print("{:=25}".format(cd))

##s=input()
##s=s[::-1]
##cs=0
##for c in s:
##    if c==".":
##        break
##    cs+=eval(c)
##print ("{:*>10}".format(cs))

##a=[3,6,9]
##b=eval(input())
##s=0
##for i in range(3):
##    s=s+(a[i]*b[i])
##print(s)


import jieba
s=input()
n=len(s)
m=len(jieba.lcut(s))
print("{},{}",format(n,m))
