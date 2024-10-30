import pandas as pd
df_read = pd.read_csv(r'Nombre de signalements de troubles musculo-squelettiques (TMS) - hommes et femmes.csv')

prevalence_rate_Women = (df_read.iloc[:, 3])
colonne_taux_prevalence = df_read['Taux de prévalence standardisé troubles musculo-squelettique F 2022']
# print(colonne_taux_prevalence) 
# print(df_read.columns) 
# détail des entêtes des colonnes

x = 0
while x < len(prevalence_rate_Women):
        # print(prevalence_rate_Women[x])
        
        value = prevalence_rate_Women[x]
        # print(value)
        
        try:
              float_value = float(value)  
        except:
               pass
        print("Ce n'est pas une valeur de type float")
        # print(float_value)
        # print(type(value))
        # if isinstance(float_value,float):
        #         print(float_value)
        x = x+1 
                
 


        
   
# colonne_taux_prevalence = df_read['Taux de prévalence standardisé troubles musculo-squelettiques 2022']

# print(colonne_taux_prevalence)     
# print(df_read.iloc[list(df_read['Taux de prévalence standardisé troubles musculo-squelettique F 2022'] > 1)])
# df = pd.read_csv(r'Nombre de signalements de troubles musculo-squelettiques (TMS) - hommes et femmes.csv')
# print(df) 
# df = imprime le DataFrame soit le format des données rencontré
# en économie, des tableaux à deux dimensions avec des variables
# en colonnes et des observations en ligne. Les colonnes et lignes des dataframes
# sont indexées. 
