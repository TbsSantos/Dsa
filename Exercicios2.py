#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# In[ ]:


# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.


# In[6]:


lista = list(range(1,11))
lista


# In[ ]:


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela



# In[7]:


lista2 = ["THAYSSA",88,False,{1:'Ezo',2:'Sueli'},0.5]
lista2


# In[ ]:


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string


# In[8]:


str1 = 'Vamos aprender ciêcia de dados '
str2 = 'Para ter um futuro melhor'
str3 = str1 + str2
str3


# In[ ]:


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla


# In[10]:


tupla = (1, 2, 2, 3, 4, 4, 4, 5)
tupla.count(4)


# In[ ]:


# Exercício 5 - Crie um dicionário vazio e imprima na tela


# In[12]:


dic1 = {}
dic1


# In[ ]:


#Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela


# In[18]:


fullname = {'nome':'Thiago','meio':'Barbosa','sobrenome':'santos'}
print(f'{fullname["nome"]} {fullname["meio"]} {fullname["sobrenome"]} ')
print('\n')
fullname


# In[ ]:


#Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela


# In[19]:


fullname['removido']='Silva'
fullname


# In[ ]:


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.


# In[20]:


hero = {'hp':39,'mp':10,'sorte':[2,8]}
hero


# In[ ]:


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.


# In[21]:


variado = ['Kilma',('verde','azul'),{1:'First',2:'Second'},1.3]
variado


# In[22]:


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[1:18]

