import pandas as pd#importing pandas library

data = {
    "exams":[23,54,67],
    "dates":["1 Jun","4 May","7 Aug"]
}
df = pd.DataFrame(data,index=["Enes","Yasin","Yavuz"])#converting into a data frame
print(df)
print(df.iloc[2])
print(df.loc["Yavuz"])
#with iloc use number,with loc use exact value if you want to access rows
print(df["exams"])#for accessing columns u can use value
print(df.loc["Enes","dates"])#for specific value