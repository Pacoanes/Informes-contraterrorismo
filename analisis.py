import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#ataque por año

def grafico_barras(col,que_quiero,nombre_fichero,titulo):
    plt.subplots(figsize=(15,6))
    sns.countplot(col,data=bd,palette='inferno',order=que_quiero)
    plt.xticks(rotation=90)
    plt.legend("")
    plt.title(titulo)
    plt.savefig(nombre_fichero)
    return

def grafico_vs():
    coun_terror=bd['NCountry'].value_counts()[:15].to_frame()
    coun_terror.columns=['Ataques']
    coun_kill=bd.groupby('NCountry')['killed'].sum().to_frame()
    coun_terror.merge(coun_kill,left_index=True,right_index=True,how='left').plot.bar(width=0.9)
    fig=plt.gcf()
    fig.set_size_inches(18,6)
    plt.title('Ataques vs muertos {}'.format(npais))
    fig.savefig('ataques.png', dpi=fig.dpi)
    return