# Import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

def exclui_outliers(DataFrame, col_name):
    '''Função que utiliza a regra:
    Q1 - 1,5 x IQR (ou -2,7 sigma) / Q3 + 1,5 x IQR (ou 2,7 sigma) para excluir outliers.
    A função pega todos os valores que estão fora desse intervalo e o substituem para "nan".

    :param DataFrame: (dataframe)
    Dataframe que você quer aplicar a regra.

    :param col_name: (series)
    Coluna(s) quantitativas contínuas que você quer eliminar os outliers.
    Deve ser passada entre aspas ao chamar a função.

    :return: (dataframe)
    Dataset com as respectivas colunas sem os possíveis outliers.
    '''
    intervalo = 2.7 * DataFrame[col_name].std()
    media = DataFrame[col_name].mean()
    DataFrame.loc[DataFrame[col_name] < (media - intervalo), col_name] = np.nan
    DataFrame.loc[DataFrame[col_name] > (media + intervalo), col_name] = np.nan