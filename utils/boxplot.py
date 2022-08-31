# Import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

# Create a function of the boxplot graph to reuse later
def boxplot(figsize, title, data, x, y, xlabel, ylabel):

  # Plot the graph
  plt.figure(figsize=figsize)

  # Title
  plt.title(title, fontsize = 20)

  # Graph
  sns.boxplot(x = x, y = y, data = data)

  # Label
  plt.xlabel(xlabel, fontsize=14)
  plt.xticks(fontsize=14, rotation=30)
  plt.ylabel(ylabel, fontsize=14)
  plt.yticks(fontsize=14)
  plt.show()