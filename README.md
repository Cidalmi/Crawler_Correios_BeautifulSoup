# Crawler Correios

Este repositório contém a solução desenvolvida para coletar todas as faixas de CEP dos [Correios](http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm), retirando as duplicatas e gerando um id único. Ao obter esses dados será gerado um arquivo jsonl com a localidade, faixa de cep e id gerado.

## Iniciando
Essa são instruções de como você pode configurar seu projeto localmente. Para obter uma cópia local instalada e funcionando, siga estas etapas a seguir.

### Requisitos

* Python 3.7
* Pip (ou outro instalador de pacotes)


O arquivo requirements.txt tem todas as bibliotecas em Python das quais são necessárias para executar o projeto e serão instaladas usando:

```
pip install -r requirements.txt
```
#### Bibliotecas usadas
* beautifulsoup4
* pandas
* requests

### Uso

Baixar o projeto na sua máquina:
* Branch main
  
    ```
    git clone https://github.com/Cidalmi/Crawler_Correios_BeautifulSoup.git
    ```
* Branch dev
    
    ```
    git clone --branch dev https://github.com/Cidalmi/Crawler_Correios_BeautifulSoup.git
    ```

#### Executando o scrapy:
 
    cd crawler_correios_BeautifulSoup
    python consult_correios.py


## Descrição

A solução foi desenvolvida em Python 3.7 usando o beautifulsoup para efetuar o tratamento do dado HTML consultado pelo request.

Iniciamos com um loop em todos os estados de forma síncrona para efetuar o post. Utilizaremos o beautifulsoup para obter os dados das tabelas de todos os estados e municípios. Todos esses dados serão inseridos em um dataframe e depois verificamos se existe paginação no estado.

Em uma próxima etapa, será efetuar o tratamento dos dados, onde usaremos o pandas para filtrar os campos de id, localidade e faixa de cep, depois removemos os duplicados e transformamos o dataframe em json lines para que seja criar o arquivo.


O arquivo output.jsonl será criado na raiz do projeto. 
