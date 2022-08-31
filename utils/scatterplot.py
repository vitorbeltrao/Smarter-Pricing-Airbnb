# Import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

def scatter(figsize, title, data, x, y, hue, xlabel, ylabel):

  # Plot the graph
  plt.figure(figsize=figsize)

  # Title
  plt.title(title, fontsize=20)

  # Graph
  sns.scatterplot(data = data, x = x, y = y, hue=hue, palette = "rocket")

  # Label
  plt.xlabel(xlabel, fontsize=14)
  plt.xticks(fontsize=14)
  plt.ylabel(ylabel, fontsize=14)
  plt.yticks(fontsize=14)
  plt.show()