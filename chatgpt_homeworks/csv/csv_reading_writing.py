import pandas as pd

df = pd.read_csv(r"C:\Users\Enes\Desktop\PythonVScode\chatgpt_homeworks\csv\data.csv",header= None)#we have to say full path in order to see it
print(df.to_string())

df[6] = ["a","g","f","h","k","i","y"]

new_df = df.drop(6,axis =0)
print(new_df)
new_df.to_csv(r"C:\Users\Enes\Desktop\PythonVScode\chatgpt_homeworks\csv\data_2.csv")
print(pd.read_csv(r"C:\Users\Enes\Desktop\PythonVScode\chatgpt_homeworks\csv\data_2.csv",header = None))