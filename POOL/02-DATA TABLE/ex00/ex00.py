import pandas as pd

import pandas as pd
from pandas import DataFrame
from typing import Optional

def load(path: str) -> Optional[DataFrame]:
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        print(df.to_string(index=False)) 
        return df
    except Exception as e:
        return None

def main():
    print(load("file.csv"))
if __name__ == "__main__":
    main()