import pandas as pd

csv1 = pd.read_csv('/home/subin/AAA/test.txt', dtype=str)
csv2 = pd.read_csv('/home/subin/AAA/test1.txt', dtype=str)
new_df = csv1[~csv1['MSISDN'].isin(csv2['MSISDN'])]


if new_df.size==0:
    new_df.to_csv('/home/subin/AAA/Opp.txt', index=False,line_terminator="")
else:
    k= new_df.loc[0:new_df.size-2]
    k.to_csv('/home/subin/AAA/Opp.txt',index=False)
    k= None
    last_line=new_df.loc[new_df.size - 2:new_df.size]
    last_line.to_csv('/home/subin/AAA/Opp.txt',header= False, encoding='utf-8', index=False,mode='a',line_terminator="")
    last_line = None
    del last_line,k
csv1 = csv2 = new_df = None
del csv1,csv2,new_df




