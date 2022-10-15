import pandas as pd
from datetime import datetime


df = pd.read_csv('d:\\test.csv',parse_dates=['DOB'])


df



today = datetime.today()
df['Age'] = df['DOB'].apply(
               lambda x: today.year - x.year - 
               ((today.month, today.day) < (x.month, x.day)) 
               )


df





