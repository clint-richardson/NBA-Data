#helper functions to get new data from the existing data (i.e. composite data) generally returns data frames holding just the high-level info made by each function

import pandas as pd
import numpy as np

def getPlayerAccuracy(df,player):
    nmade = len(df[ (df['player_name']==player) & ( df['SHOT_RESULT']=='made') ])
    ntot = len(df[ (df['player_name']==player)])
    accuracy = float(nmade)/ float(ntot)
    return accuracy

def getListOfPlayers(df):

    names = df['player_name'].unique()
    return names

def getPlayerAccuracyDF(df):
    namesdf = df['player_name'].unique()
    acc = []
    dists=[]
    shots=[]
    for name in namesdf:
        acc.append(getPlayerAccuracy(df,name))
        distarr = df[(df['player_name']==name)].SHOT_DIST.values
        dists.append( np.mean(distarr))
        shots.append(len(df[df['player_name']==name]))

    retDF = pd.DataFrame(namesdf,columns=['player_name'])
    retDF['AVG_SHOT_DIST']=dists
    retDF['ACCURACY']=acc
    retDF['N_SHOTS']=shots
    print retDF.head()
    return retDF
