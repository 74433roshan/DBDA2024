# For marthon dataset .. Find the conditional probability of finish within 3 hours given that
#space < 8 minute per mile

import pandas as pd
df_2015=pd.read_csv("D:/advanced Analystics/DBDA-AtulKahate/marathon_results_2015.csv")
df_2016=pd.read_csv("D:/advanced Analystics/DBDA-AtulKahate/marathon_results_2016.csv")
df_2017=pd.read_csv("D:/advanced Analystics/DBDA-AtulKahate/marathon_results_2017.csv")

df=pd.concat([df_2015,df_2016,df_2017])


#converts hours,minutes and seconds column to integer
df[['Hours','Minutes','Seconds']] = df['Official Time'].str.split(':',expand=True)


df['Hours']=df['Hours'].astype(int)
df['Minutes']=df['Minutes'].astype(int)
df['Seconds']=df['Seconds'].astype(int)

#manualiy calculate total timein seconds
df['finish_time_in_seconds']=df['Hours']*3600+df['Minutes']*60+df['Seconds']



df[['Hours','Minutes','Seconds']] = df['Pace'].str.split(':',expand=True)


#converts hours,minutes and seconds column to integer
df['Hours']=df['Hours'].astype(int)
df['Minutes']=df['Minutes'].astype(int)
df['Seconds']=df['Seconds'].astype(int)

#manualiy calculate total timein seconds
df['pace_in_seconds']=df['Hours']*3600+df['Minutes']*60+df['Seconds']

#define the conditions
condition_A=df['finish_time_in_seconds']<=3*60*60 #finish in 3 hours
condition_B=df['pace_in_seconds']<8*60 #pace less than 8 minutes per kilometer

#calculate the probablities
P_B=len(df[condition_B])/len(df)

P_A_and_B=len(df[condition_A & condition_B])/len(df)

#Conditional probabilitiesP(A|B)
P_A_given_B=P_A_and_B/ P_B

print(f"P(A | B)= {P_A_given_B:.4f}")


















