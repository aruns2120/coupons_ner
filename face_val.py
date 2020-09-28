import re
import os
import pandas as pd

def find_faceValue(offerDetails: str):
    f = re.findall(r"save\s*\$\s*\.*\d+[\.\d]*|\$\s*\.*\d+[\.\d]*\s*off|"
                   r"save\s*\d+[\.\d]*\s*Â*¢|\d+[\.\d]*\s*Â*¢\s*off", offerDetails, flags=re.IGNORECASE)
    if f:
    	f = f[0]
    else:
    	f= ''
    f = re.sub('save', '', f, flags=re.IGNORECASE)
    f = re.sub('off', '', f, flags=re.IGNORECASE).strip()
    if '¢' in f:
        drop = 1
        if 'Â' in f:
            drop = 2
        cent = re.findall(r"\d+[\.\d]*\s*Â*¢", f, flags=re.IGNORECASE)[0]
        f = re.sub(r"\d+[\.\d]*\s*Â*¢", '$'+str(int(cent[:-drop])/100), f)
    # print(f)
    return f

df = pd.read_csv('coupons_ner.csv', names=['offerDetails'])
df['faceValue'] = df['offerDetails'].apply(find_faceValue)
df.to_csv('facevalue.csv', index=False)