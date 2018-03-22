import pandas as pd
import numpy as np
import csv

df = pd.read_csv('wiki_extract08.csv', delimiter='\t')


father = ['其父', '父親']
mather = ['其母', '母親']
husband = ['其夫', '丈夫', '前夫']
wife = ['其妻', '妻子', '前妻']
#s[s.str.contains('|'.join(searchfor))]



df['father1'] = df['Summary'].str.contains('|'.join(father))
df['father2'] = df['Content'].str.contains('|'.join(father))
#df['father2'] = df['Content'].str.contains('父親')



df['gfather1'] = df['Summary'].str.contains('祖父')
df['gfather2'] = df['Content'].str.contains('祖父')

df['mather1'] = df['Summary'].str.contains('|'.join(mather))
df['mather2'] = df['Content'].str.contains('|'.join(mather))

df['gmather1'] = df['Summary'].str.contains('祖母')
df['gmather2'] = df['Content'].str.contains('祖母')

df['husband1'] = df['Summary'].str.contains('|'.join(husband))
df['husband2'] = df['Content'].str.contains('|'.join(husband))

df['wife1'] = df['Summary'].str.contains('|'.join(wife))
df['wife2'] = df['Content'].str.contains('|'.join(wife))


#df['father1','father2','gfather1','gfather2','mather1','mather2','gmather1','gmather2'].astype(int)

df.to_csv('wiki08_ana.csv', sep='\t')