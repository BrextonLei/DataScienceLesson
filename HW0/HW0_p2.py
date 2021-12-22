#!/usr/bin/env python
# coding: utf-8

# In[9]:


I020=[line.strip("\n").split(",") for line in open("IMDB-Movie-Data.csv")]


# In[ ]:


#此次database資料缺項頗多


# In[75]:


#1
I020a=[]
for i in range(1,len(I020)):
    I020a.append([I020[i][1],I020[i][7]])
sorted(I020a, key = lambda s: s[1])
print("Top 1 movie:",I020a[0][0],",Rating:",I020a[0][1])
print("Top 2 movie:",I020a[1][0],",Rating:",I020a[1][1])
print("Top 3 movie:",I020a[2][0],",Rating:",I020a[2][1])


# In[95]:


#2
I020=[line.strip("\n").split(",") for line in open("IMDB-Movie-Data.csv")]
#b1先抓出所有演員的名字陣列
I020b1=[]
#b2[i][0]=演員名字 [i[1]=所有演過的電影個別票房
I020b2=[]
for i in range(1,len(I020)):
    temp=[]
    temp=I020[i][4].split("|")
    for p in range(len(temp)):
        if str(temp[p])[0]==' ':
            temp[p]=temp[p].strip(' ')
    I020b1.append(temp)
#print(I020b1)
for i in range(0,len(I020b1)):
    for j in range(0,len(I020b1[i])):
        if I020b1[i][j] in I020b2:
            ("")
        else:
            if str(I020b1[i][j])[0]==' ':
                I020b1[i][j]=I020b1[i][j].strip(' ')
            else:
                I020b2.append([I020b1[i][j],[],0])
x=0
#print(I020b2)
for i in range(1,len(I020)):
    I020[i][4]=I020[i][4].split("|")
    for j in range(len(I020[i][4])):
        if str(I020[i][4][j])[0]==' ':
            I020[i][4][j]=I020[i][4][j].strip(' ')
            #print("OK")
        #print(I020b2[x][0])
        #print(I020[i][4][j])
        for x in range(0,len(I020b2)):
            if I020b2[x][0]==I020[i][4][j]:
                #print(I020b2[x][0])
                #print(I020[i][4][j])
                if I020[i][9]!='':
                    I020b2[x][1].append(float(I020[i][9]))
                

for x in range(len(I020b2)):
    #print('x=',x)
    if I020b2[x][1]!=[]:
        num=len(I020b2[x][1])
        Sum=sum(I020b2[x][1])
        Avg=Sum/num
    else:
        Avg=0
    I020b2[x][2]=Avg
    #I020b2[x][2]/=len(I020b2[x][1])
    #print(I020b2[x][2])

###再弄個b3只抓人+AVG排列即可
I020b3=[]
for i in range(len(I020b2)):
    I020b3.append([I020b2[i][0],int(I020b2[i][2])])
    #I020b3.append(I020b2[i][2])
Ans=sorted(I020b3,key=lambda I020b3:I020b3[1], reverse=True)
print("The actor generating the highest average revenue is",Ans[0][0],", Avg revenue is",Ans[0][1],"(Millions).")


# In[106]:


#3
I020=[line.strip("\n").split(",") for line in open("IMDB-Movie-Data.csv")]
for i in range(1,len(I020)):
    I020[i][4]=I020[i][4].split("|")
    for j in range(len(I020[i][4])):
        if str(I020[i][4][j])[0]==' ':
            I020[i][4][j]=I020[i][4][j].strip(' ')
#print(I020)
I020c=[]
for i in range(1,len(I020)):
    if 'Emma Watson' in I020[i][4]:
        I020c.append([I020[i][1],I020[i][7]])
Sumc=0
for i in range(0,len(I020c)):
    Sumc+=float(I020c[i][1])
AvgRating=(Sumc/len(I020c))
print('The average rating of Emma Watson’s movies is',AvgRating,'points.')


# In[260]:


#4
I020=[line.strip("\n").split(",") for line in open("IMDB-Movie-Data.csv")]
for i in range(1,len(I020)):
    I020[i][4]=I020[i][4].split("|")
    for j in range(len(I020[i][4])):
        if str(I020[i][4][j])[0]==' ':
            I020[i][4][j]=I020[i][4][j].strip(' ')
I020d=[]
for i in range(1,len(I020)):
    I020d.append([I020[i][3],I020[i][4]])
#print(I020d)
for i in range(len(I020d)):
    for j in range(len(I020d)):
        if I020d[j][0]==I020d[i][0] and i!=j:
            for k in range(len(I020d[j][1])):
                #print(i,j,k)
                I020d[i][1].append(I020d[j][1][k])
    unique_set = set(I020d[i][1])
    unique_list = list(unique_set)
    I020d[i][1]=unique_list
    I020d[i].append(len(unique_list))

#print(I020d) 
Ansd=sorted(I020d,key=lambda I020d:I020d[2], reverse=True)
print('Top-1 directors who collaborate with the most actors is',Ansd[0][0],',num=',Ansd[0][2])
print('Top-2 directors who collaborate with the most actors is',Ansd[8][0],',num=',Ansd[8][2])
print('Top-3 directors who collaborate with the most actors is',Ansd[14][0],',num=',Ansd[14][2])


# In[356]:


#5
I020=[line.strip("\n").split(",") for line in open("IMDB-Movie-Data.csv")]
I020e=[]
for i in range(1,len(I020)):
    I020[i][4]=I020[i][4].split("|")
    I020[i][2]=I020[i][2].split("|")
    for j in range(len(I020[i][4])):
        if str(I020[i][4][j])[0]==' ':
            I020[i][4][j]=I020[i][4][j].strip(' ')
    for k in range(len(I020[i][4])):
        I020e.append([I020[i][4][k],I020[i][2]])
#print(I020e)
I020e1=I020e
for i in range(len(I020e)):
    for j in range(len(I020e1)):
        if I020e[i][0]==I020e1[j][0]:
            #print(I020e[i][0],I020e[j][0],i,j)
            #print(I020e[i][1],I020e1[j][1])
            I020e[i][1]+=I020e1[j][1]
            #print(I020e[i][1])
            #print(I020e[i][1])
            #for k in range(len(I020e[j][1])):
                #print(i,j,k)
                #I020e[i][1].append(I020e[j][1][k])
    #print(I020e[i][0],i)
    unique_set = set(I020e[i][1])
    unique_list = list(unique_set)
    I020e[i][1]=unique_list
    I020e[i].append(len(unique_list)) 
    #print(I020e[i])
#print(I020e) 
Anse=sorted(I020e,key=lambda I020e:I020e[2], reverse=True)
#print(Anse)

print('Top-1 actors playing in the most genres of movies is',Anse[0][0],',num=',Anse[0][2])
print('Top-2 actors playing in the most genres of movies is',Anse[1][0],',num=',Anse[1][2])
print('Top-3 actors playing in the most genres of movies is',Anse[2][0],',num=',Anse[2][2])


# In[343]:


#6
I020=[line.strip("\n").split(",") for line in open("IMDB-Movie-Data.csv")]
I020f1=[]
for i in range(1,len(I020)):
    I020[i][4]=I020[i][4].split("|")
    I020[i][2]=I020[i][2].split("|")
    for j in range(len(I020[i][4])):
        if str(I020[i][4][j])[0]==' ':
            I020[i][4][j]=I020[i][4][j].strip(' ')
    for k in range(len(I020[i][4])):
        if I020[i][4][k] not in I020f1:
            I020f1.append(I020[i][4][k])
for i in range(len(I020f1)):
    I020f1[i]=[I020f1[i]]
    I020f1[i]=[I020f1[i],[]]
    [I020f1[i][0]]=I020f1[i][0]
#print(I020f1)
for i in range(1,len(I020)):
    for j in range(len(I020[i][4])):
        for k in range(len(I020f1)):
            if I020f1[k][0]==I020[i][4][j]:
                I020f1[k][1].append(int(I020[i][5]))
#print(I020f1)
for i in range(len(I020f1)):
    I020f1[i].append(max(I020f1[i][1])-min(I020f1[i][1]))
Ansf=sorted(I020f1,key=lambda I020f1:I020f1[2], reverse=True)
print("Those 53 actor's movies leading the largest maximum gap of years(10 years):")
for i in range(53):
    print(Ansf[i][0])


# In[ ]:




