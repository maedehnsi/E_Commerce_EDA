# utils.py
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()


def plot_bar_plot(df, x_col, height_col, x_label, y_label, title):
    fig = plt.figure(figsize=(10, 5))
    plt.bar(df[x_col], df[height_col], color='green', width=0.5)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


