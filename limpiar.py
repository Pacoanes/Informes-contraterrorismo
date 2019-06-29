import pandas as pd


def eliminar_columnas(df, col):
    df.drop(columns=[col], inplace=True)
    return df

def renombrar(df, col, nombre):

    df.rename(columns={col: nombre}, inplace=True)
    return df

def columna_de_sumar_dos(df, nuevo, col1, col2 ):
    df[nuevo]= df[col1]+ df[col2]
    return df