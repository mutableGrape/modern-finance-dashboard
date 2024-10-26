import pandas as pd

class Account:
    def __init__(self, name: str, data: pd.DataFrame):
        self.name = name
        self.data = data
