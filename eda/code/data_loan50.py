import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)




# -----------------
# Data
# -----------------

ROOT = "https://raw.githubusercontent.com/kirenz/datasets/master/"
DATA = "loan50.csv"
df = pd.read_csv(ROOT + DATA)

df_describe = df.describe().transpose()