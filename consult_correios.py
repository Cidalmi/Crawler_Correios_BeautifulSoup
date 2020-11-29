# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

ufs = ['AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']
final_df = pd.DataFrame()
for uf in ufs:
    print("Consulta no Estado: ",uf)
    time.sleep(1)
    next_page = 0
    pagini = 1
    pagfim = 100
    loop = 1    
    while next_page != []:   
        time.sleep(1)     
        url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"
        payload={'UF': uf, 'Localidade': '', 'qtdrow': '100', 'pagini': pagini, 'pagfim': pagfim}        
        response = requests.request("POST", url, data=payload, allow_redirects=False)
        text_req = response.content        
        decoded_text = text_req.decode('ISO-8859-1')
        soup = BeautifulSoup(decoded_text, 'html.parser')
        
        #Primeiro Loop, pois tem duas tabelas
        if loop == 1:
            tables = soup.find_all("table")[1]
            df = pd.read_html(str(tables))
            final_df = final_df.append(df, ignore_index = True)
        else:
            tables = soup.find_all("table")
            df = pd.read_html(str(tables))
            final_df = final_df.append(df, ignore_index = True)

        pagini += 100
        pagfim += 100
        print("Pagina: ", loop) 
        loop += 1
        next_page = soup.find_all("a", href="javascript:document.Proxima.submit('Proxima')")                

final_df.index.names = ['id']
final_df = final_df.filter(items=['id','Localidade','Faixa de CEP'])
final_df = final_df.drop_duplicates()
json_records = final_df.reset_index().to_json(orient ='records', lines=True, force_ascii=False) 
with open('output.jsonl', 'w', encoding='utf8') as outfile:
    outfile.write(json_records)
    outfile.close()


