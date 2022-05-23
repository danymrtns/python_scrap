#Importation des packages

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as web
import datetime as dt


#importation des données

#def des dates de début et de fin :

debut=dt.datetime(2019,11,16)                       #date de première apparition du Covid-19
fin=dt.datetime.now()                               #date d'aujourd'hui

#date debut 1er confinement FRANCE
debutdc=dt.datetime(2020,3,17)
findc=dt.datetime(2020,3,17)

#1er confinement FRANCE
debutc1=dt.datetime(2020,3,17)
finc1=dt.datetime(2020,5,11)

#2e confinement FRANCE
debutc2=dt.datetime(2020,10,30)
finc2=dt.datetime(2020,12,15)

#3e confinement FRANCE
debutc3=dt.datetime(2021,4,3)
finc3=dt.datetime(2021,5,3)

#date fin confinement FRANCE
debutfc=dt.datetime(2021,5,3)
finfc=dt.datetime(2021,5,3)

#création des jeux de données pour nos graphiques :

jeu1=web.DataReader('MRNA', 'yahoo',debut,fin)      # Moderna stock
jeu2=web.DataReader('PFE', 'yahoo',debut,fin)       # Pfizer stock
jeu3=web.DataReader('BNTX', 'yahoo',debut,fin)      # BioNTech stock
jeu4=web.DataReader('JNJ', 'yahoo',debut,fin)       # Johnson & Johnson stock
jeu5=web.DataReader('AZN', 'yahoo',debut,fin)       # AstraZeneca stock
jeu6=web.DataReader('NVAX', 'yahoo',debut,fin)      # Novavax stock
jeu7=web.DataReader('NFLX', 'yahoo',debut,fin)      # Netflix stock
jeu7dc=web.DataReader('NFLX', 'yahoo',debutdc,findc)
jeu7c1=web.DataReader('NFLX', 'yahoo',debutc1,finc1)
jeu7c2=web.DataReader('NFLX', 'yahoo',debutc2,finc2)
jeu7c3=web.DataReader('NFLX', 'yahoo',debutc3,finc3)
jeu7fc=web.DataReader('NFLX', 'yahoo',debutfc,finfc)
jeu8=web.DataReader('TKWY.AS', 'yahoo',debut,fin)   # Takeaway.com (Just Eat Takeaway) stock  ps: "Just Eat" sera utilisé comme legende
jeu9=web.DataReader('ROO.L', 'yahoo',debut,fin)     # Deliveroo stock
jeu10=web.DataReader('ZM', 'yahoo',debut,fin)       # Zoom Video Communications                     (source yahoo finance all)


#visualisation des données

fig=plt.figure(figsize=(16,9))

plt.subplots_adjust(wspace= 0.25, hspace= 0.25)


ax = fig.add_subplot(2,2,1) # graphique de comparaison de l'évolution des valeurs de fermeture des groupes pharmaceutiques début Covid-19 à maintenant

ax.plot(jeu1.index,jeu1['Close'], color= 'darkred',label='Moderna')
ax.plot(jeu2.index,jeu2['Close'], color= 'dodgerblue',label='Pfizer')
ax.plot(jeu3.index,jeu3['Close'], color= 'seagreen',label='BioNTech')
ax.plot(jeu4.index,jeu4['Close'], color= 'red',label='Johnson & Johnson')
ax.plot(jeu5.index,jeu5['Close'], color= 'orange',label='AstraZeneca')
ax.plot(jeu6.index,jeu6['Close'], color= 'purple',label='Novavax')

ax.set_xlabel('Date')
ax.set_ylabel('Valeur de fermeture')
ax.legend()


ax2 = fig.add_subplot(2,2,2) # graphique de comparaison de l'évolution des valeurs de fermeture des "Stay at Home" début Covid-19 à maintenant

ax2.plot(jeu7.index,jeu7['Close'], color= 'crimson',label='Netflix')
ax2.plot(jeu8.index,jeu8['Close'], color= 'darkorange',label='Just Eat')
ax2.plot(jeu9.index,jeu9['Close'], color= 'cyan',label='Deliveroo')
ax2.plot(jeu10.index,jeu10['Close'], color= 'cornflowerblue',label='Zoom')

ax2.set_xlabel('Date')
ax2.set_ylabel('Valeur de fermeture')
ax2.legend()

ax3 = fig.add_subplot(2,2,3) # graphique de comparaison de l'évolution des valeurs de fermeture des "Stay at Home" début Covid-19 à maintenant

ax3.plot(jeu1.index,jeu1['Close'], color= 'darkred',label='Moderna')
ax3.plot(jeu3.index,jeu3['Close'], color= 'seagreen',label='BioNTech')
ax3.plot(jeu6.index,jeu6['Close'], color= 'purple',label='Novavax')
ax3.plot(jeu7.index,jeu7['Close'], color= 'crimson',label='Netflix')
ax3.plot(jeu10.index,jeu10['Close'], color= 'cornflowerblue',label='Zoom')

ax3.set_xlabel('Date')
ax3.set_ylabel('Valeur de fermeture')
ax3.legend()



ax4 = fig.add_subplot(2,2,4, projection='3d')# graphique de comparaison 3D des géants

y1 = [0, 1, 2, 3]

for c in zip(y1):

    # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
    
    ax4.bar(jeu3.index,jeu3['Close'], zs=y1[0], zdir='y', color= 'seagreen',alpha=0.4, label='BioNTech')
    ax4.bar(jeu1.index,jeu1['Close'], zs=y1[1], zdir='y', color= 'darkred',alpha=0.4, label='Moderna')
    ax4.bar(jeu10.index,jeu10['Close'], zs=y1[2], zdir='y', color= 'cornflowerblue',alpha=0.4, label='Zoom')
    ax4.bar(jeu7.index,jeu7['Close'], zs=y1[3], zdir='y', color= 'crimson',alpha=0.4, label='Netflix')
    
    
    #NOTE#Rappel de construction :
    # ax.bar(jeu2.index,jeu2['Close'], zs=k, zdir='y', color= 'green',alpha=0.8)

ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')

# On the y axis let's only label the discrete values that we have data for.
# ax.set_y1(y1)

plt.show()