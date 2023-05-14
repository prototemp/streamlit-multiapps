import pandas as pd
import numpy as np
# import app 
from apps.input_data import app

def create_table(n=7):
    df = pd.DataFrame({"x": range(1, 11), "y": n})
    df['x*y'] = df.x * df.y
    return df
    # pass