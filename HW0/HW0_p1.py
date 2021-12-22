#!/usr/bin/env python
# coding: utf-8

# In[150]:


#1 Io[i][j][k][l], Io[i][j][0]==系數 Io[i][j][1][0]=未知數 Io[i][j][1][1]=次方
In=input("input the poly:")
Io=[]
In=In.strip('(').strip(')')
In=In.replace(')(',',')
Io=In.split(',')
#print(Io)
for i in range(len(Io)):
    if '-' in Io[i]:
        Io[i]=Io[i].replace('-','+-')
    Io[i]=Io[i].split('+')
#print(Io)
for i in range(len(Io)):
    for j in range(len(Io[i])):
        if Io[i][j][0].isdigit() or (Io[i][j][0]=='-' and Io[i][j][1].isdigit()):
            Io[i][j]=Io[i][j].split('*')
        elif Io[i][j][0]=='-' and Io[i][j][1].isdigit()==0:
            Io[i][j]=Io[i][j].split('-')
            Io[i][j][0]=-1
        else:
            Io[i][j]=['1',Io[i][j]]
#print(Io)
for i in range(len(Io)):
    for j in range(len(Io[i])):
        if '^' in Io[i][j][1]:
            Io[i][j][1]=Io[i][j][1].split('^')
            #[Io[i][j][1]]=Io[i][j][1]
        else:
            Io[i][j][1]=[Io[i][j][1],1]
#print(Io)


# In[151]:


ans=[]
for i in range(len(Io[0])):
    for j in range(len(Io[1])):
        #print(Io[0][i][1][0],Io[1][j][1][0])
        if Io[0][i][1][0]!=Io[1][j][1][0]:
            ans.append([(int(Io[0][i][0])*int(Io[1][j][0])),str(Io[0][i][1][0])+'^'+str(Io[0][i][1][1])+str(Io[1][j][1][0])+'^'+str(Io[1][j][1][1]),1])
        #次方相加
        else:
            ans.append([(int(Io[0][i][0])*int(Io[1][j][0])),str(Io[0][i][1][0]),int(Io[0][i][1][1])+int(Io[1][j][1][1])])
#print(ans)
Ans=''
for i in range(len(ans)):
    for j in range(len(ans[i])):
        if j==0:
            if int(ans[i][0])==1:
                Ans+='+'
            elif int(ans[i][0])>1:
                Ans+='+'+str(ans[i][j])+'*'
            elif int(ans[i][0])==-1:
                Ans+='-'
            elif int(ans[i][0])<-1:
                Ans+=str(ans[i][j])+'*'
        elif j==1:
            if '^1' in str(ans[i][j]):
                ans[i][j]=ans[i][j].replace('^1','')
                #print('wewe')
                Ans+=str(ans[i][j])
            else:
                Ans+=str(ans[i][j])
        elif j==2:
            if int(ans[i][j])==1:
                ("")
            else:
                Ans+='^'+str(ans[i][j])
if Ans[0]=='+':
    Ans=Ans[1:]
print(Ans)


# In[ ]:




