import matplotlib.pyplot as plot
import pandas as pd
from typing import Optional
from pandas import DataFrame
import numpy

def load(path: str) -> Optional[DataFrame]:
    try:
        data = pd.read_csv(path)
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def main():
    data = load("file.csv")
    if data is not None:
        xpoints = numpy.array(data["Name"])
        ypoints = numpy.array(data["Year"])
        print(data)
        plot.plot(xpoints, ypoints)
        plot.title("Year by Name")
        plot.xlabel("Name")
        plot.ylabel("Year")
        plot.tight_layout()
        plot.show()
    else:
        print("No data to plot.")

if __name__ == "__main__":
    main()
