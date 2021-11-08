import pandas as pd;

if __name__ == '__main__':
    #guardo en variables los nombres que voy a usar para acceder y bucar en el excel
    archivo = "retodiario1.xlsx"
    hoja = "Hoja 1"
    columna = "email"


    #creo un dataframe del excel sobre la columna email
    df = pd.read_excel(io = archivo, sheet_name= hoja, usecols= ["email"])
    
    #como en set se recogen solamente datos únicos convierto el dataframe en un set
    email = set(df["email"])
    
    
    #imprimo el set
    for i in email:
        print (i)