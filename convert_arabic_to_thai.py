import pandas as pd
from io import BytesIO

REP = {"0": "๐", "1": "๑", "2": "๒", "3": "๓", "4": "๔",
           "5": "๕", "6": "๖", "7": "๗", "8": "๘", "9": "๙"}

def convert(x: BytesIO) -> BytesIO:
    tmp = BytesIO()
    df = pd.read_excel(x, header=None)
    df.replace(REP, regex=True, inplace=True)
    df.to_excel(tmp, index=False, header=False)
    tmp.seek(0)
    return tmp