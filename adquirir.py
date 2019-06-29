import pandas as pd

def cargardatos(f):
    df = pd.read_csv(f, encoding="ISO-8859-1")
    return df

def nuevodf():
    df = pd.DataFrame()
    return df

def rellenar_nuevodf(df,nombre_col,col):
    df[nombre_col]=col
    return df

def mergear(df1, df2, col1, col2):
    df = df1.merge(df2, left_on = col1, right_on = col2)
    return df
