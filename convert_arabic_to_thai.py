import pandas as pd


def convert(x):
    REP = {"0": "๐", "1": "๑", "2": "๒", "3": "๓", "4": "๔",
           "5": "๕", "6": "๖", "7": "๗", "8": "๘", "9": "๙"}

    df = pd.read_excel(x, header=None)
    df.replace(REP, regex=True, inplace=True)
    # print(df)
    df.to_excel('out1.xlsx', index=False, header=False)


convert('data.xlsx')
