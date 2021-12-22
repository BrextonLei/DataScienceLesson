#!/usr/bin/env python
# coding: utf-8

# In[73]:


#main function
In=input("input the poly:(EX:請在每項未知數前加上系數，包括1 如1X -1X 1Y)")
Io=[]
In=In.strip('(').strip(')')
In=In.replace(')(',',')
Io=In.split(',')
if len(Io)==2:
    if '-' in Io[0]:
        Io[0]=Io[0].replace('-','+-')
    Io[0]=Io[0].split('+')
    if '-' in Io[1]:
        Io[1]=Io[1].replace('-','+-')
    Io[1]=Io[1].split('+')
elif len(Io)==3:
    if '-' in Io[0]:
        Io[0]=Io[0].replace('-','+-')
    Io[0]=Io[0].split('+')
    if '-' in Io[1]:
        Io[1]=Io[1].replace('-','+-')
    Io[1]=Io[1].split('+')
    if '-' in Io[2]:
        Io[2]=Io[2].replace('-','+-')
    Io[2]=Io[2].split('+')
print(Io)
#plus(Io)
if len(Io)==2:
    print(EquX(Io[0],Io[1]))
#if len(Io)==3:
    #sum=''
    #sum=EquX(Io[1],Io[2]).replace('*','')
    #print(EquX(Io[0],sum))


# In[58]:


def Sep(a):
    b=[]
    i=0
    #在a[i]之前的數都是參數
    while(a[i].isdigit() or a[i]=='-'):
        #print(a[i])
        i+=1
    a=a.replace(a[i],' '+a[i])
    b=a.split(' ')
    #print(b)
    return b
#Sep('154C5') 

def X(a,b):
    #代表有平方
    if(('^'in Sep(a)[1] or '^'in Sep(b)[1]) and (Sep(a)[1][:-2]==Sep(b)[1][:-2] or Sep(a)[1]==Sep(b)[1][:-2] or Sep(a)[1][:-2]==Sep(b)[1]) ):
        print("XD")
    else:
        if(Sep(a)[1]!=Sep(b)[1]):
            return (str(int(Sep(a)[0])*int(Sep(b)[0]))+Sep(a)[1]+'*'+Sep(b)[1])
        else:
            return (str(int(Sep(a)[0])*int(Sep(b)[0]))+Sep(a)[1]+'^2')
#print(X('12C878','12C88^4'))


# In[59]:


#一個數和一個式子相乘相加
def plus(a,b):
    sum=''
    for i in range(0,len(b)):
         sum+=X(str(a),str(b[i]))
         if(i!=len(b)-1 and X(str(a),str(b[i+1]))[0]!='-'):
            #print(X(str(a),str(b[i]))[0])
            sum+='+'
    return sum
print(plus(Io[0][0],Io[1]))


# In[60]:


#兩個式子相乘相加,都用a當基準去乘b
def EquX(a,b):
    sum=''
    for i in range(0,len(a)):
        sum+=plus(a[i],b)
        if(i!=len(a)-1):
            sum+='+'
    return '('+sum+')'
EquX(Io[0],Io[1])


# In[ ]:





# In[ ]:




