import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import reportar

def grafico_barras(df,col,que_quiero,nombre_fichero,titulo):
    npais=df.country_name.value_counts().index[0]
    plt.subplots(figsize=(15,6))
    sns.countplot(col,data=df,palette='inferno',order=que_quiero)
    plt.xticks(rotation=90)
    plt.title(titulo.format(npais))
    plt.savefig(nombre_fichero)
    return

def grafico_vs(df):
    npais=df.country_name.value_counts().index[0]
    coun_terror=df['country_name'].value_counts()[:15].to_frame()
    coun_terror.columns=['Ataques']
    coun_kill=df.groupby('country_name')['muertos'].sum().to_frame()
    coun_terror.merge(coun_kill,left_index=True,right_index=True,how='left').plot.bar(width=0.9)
    fig=plt.gcf()
    fig.set_size_inches(18,6)
    plt.title('Ataques vs muertos {}'.format(npais))
    fig.savefig('ataques.png', dpi=fig.dpi)
    return

def nograf(df):
    plt.subplots(figsize=(18,6))
    sns.barplot(df['country_name'].value_counts()[:15].index,df['country_name'].value_counts()[:15].values,palette='Blues_d')
    plt.title('Top atentados por pais')
    plt.savefig('paises.png')

def ppalbandaxmes(df):
    cel=df.gname.value_counts().index[0]
    if cel=="Unknown":
        cel=df.gname.value_counts().index[1]
    d=df[df["gname"]==cel]
    plt.subplots(figsize=(15,6))
    sns.countplot('imonth',data=d,palette='inferno',order=None)
    plt.xticks(rotation=90)
    plt.title('Actos cometidos por la principal organización por meses')
    plt.savefig('meses.png')
