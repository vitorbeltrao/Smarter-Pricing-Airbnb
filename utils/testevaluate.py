import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


def predict_evaluate(best_estimator, X_test, y_test, confidence_level):
    '''Função que faz novas predições e avalia o resultado no conjunto de testes.
    As únicas métricas ativas são RMSE e R2.

    :param best_estimator: (machine learning models or SKlearn pipeline)
    Parâmetros do modelo de machine learning um pipeline do SKlearn.

    :param X_test: (dataframe or numpy array)
    Dataframe ou array com o conjunto de dados independente.

    :param y_test: (series or numpy array)
    Coluna ou vetor com o conjunto de dados da variável alvo.

    :param confidence_level: (number)
    Nível de confiança que você queira nos seus resultados de avaliação do RMSE.
    Geralmente varia entre 0.90, 0.95 e 0.99.

    :return:
    print dos resultados do RMSE, R2 e do intervalo de confiança para o RMSE.
    '''
    # Avaliar o modelo final no conjunto de teste
    final_model = best_estimator

    # Fazer predições com os dados de teste
    final_predictions = final_model.predict(X_test)

    # Avaliar as predições nos dados de teste
    final_mse = mean_squared_error(y_test, final_predictions)
    final_rmse = np.sqrt(final_mse).astype(str)


    final_r2 = r2_score(y_test, final_predictions).astype(str)


    # Intervalo de confiança para o erro de generalização
    confidence = confidence_level
    squared_errors = (final_predictions - y_test) ** 2
    confidence_interval = np.sqrt(stats.t.interval(confidence, len(squared_errors) - 1,
                                                   loc=squared_errors.mean(),
                                                   scale=stats.sem(squared_errors))).astype(str)
    return {'RMSE':final_rmse, 'R²':final_r2, 'Confidence Interval':confidence_interval}