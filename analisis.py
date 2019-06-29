import matplotlib.pyplot as plt
import seaborn as sns
#ataque por año
plt.subplots(figsize=(15,6))
sns.countplot('Year',data=bd,palette='RdYlGn_r',edgecolor=sns.color_palette('dark',7))
plt.xticks(rotation=90)
plt.title('Number Of Terrorist Activities Each Year')
plt.show()



def guarda_plot(plot):
    return plot.figure.savefig('../output/Plot pipelines'+'.png')