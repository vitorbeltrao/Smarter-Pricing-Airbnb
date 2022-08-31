# Import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

# Create a function of the bar graph to reuse later
def barplot(figsize, title, data, x, y, xlabel, ylabel):
  # Plot the graph
  plt.figure(figsize=figsize)

  # Title
  plt.title(title, fontsize = 20)

  # Graph
  ax = sns.barplot(data = data, x = x, y = y,
                   ci = None, palette = "Blues_d")
  ax.margins(x=0, y=0.2)  # remove the margin spacing

  # Label
  plt.xlabel(xlabel, fontsize=14)
  plt.xticks(fontsize=14, rotation=30)
  plt.ylabel(ylabel, fontsize=14)
  plt.yticks(fontsize=14)

  for p in ax.patches:
      ax.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                  ha='center', va='center', fontsize=14, color='black', xytext=(0, 20),
                  textcoords='offset points')

  plt.show()