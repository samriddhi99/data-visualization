import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(df, x_column, y_columns):
    try:
        df.plot(x=x_column, y=y_columns, kind='bar')

        plt.title(f"bar plot")
        plt.xlabel(x_column)
        plt.ylabel(", ".join(y_columns))
        plt.savefig(f'pngs/plot1.png')

        df.plot(x=x_column, y=y_columns, kind='line')

        plt.title(f"line plot")
        plt.xlabel(x_column)
        plt.ylabel(", ".join(y_columns))
        plt.savefig(f'pngs/plot2.png')


        df.plot(x=x_column, y=y_columns, kind='scatter')

        plt.title(f"scatter plot")
        plt.xlabel(x_column)
        plt.ylabel(", ".join(y_columns))
        plt.savefig(f'pngs/plot3.png')



    except:
        print("Invalid graph type or data format.")
        return
