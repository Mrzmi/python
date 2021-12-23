##n=eval(input("请输入整数"))
##print("{:->20,}".format(n))

##import random
##brandlist=["华为","三星","苹果"]
##txt=random.choice(brandlist)
##print(txt)

##netxt=input("请输入4个数字")
##nls=netxt.split()
##x0=eval(nls[0])
##x1=eval(nls[1])
##y0=eval(nls[2])
##y1=eval(nls[3])
##r=pow(pow(x1-x0,2)+pow(y1-y0,2),0.5)
##print("{:.2f}".format(r))

##s=input("请输入一串字符串")
##print("{:=^20}".format(s))

##s=eval(input("请输入字符"))
##print("{:*>15}".format(s))

##
##n=eval(input("请输入整数"))
##print("{:=^14}".format(n))

##n=eval(input("请输入整数"))
##print("{:=>25,}".format(n))

##n=eval(input("请输入整数"))
##print("{:\"^30x}".format(n))

##txt=input()
##txts=txt.split(',')
##for i in txts:
##    print("{:>10}".format(i),end="")

t=eval(input())
input("{:0>2}{}".format(t,(t+1)*">"))
