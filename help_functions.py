import pandas as pd
from decimal import Decimal
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')


def convert_data_frame(df):
    return df.to_csv().encode('utf-8')

def data_transform(file_):

    #read file
    df = file_.copy()
    
    #retirando a primeira coluna que diz o nome da empresa
    columns_to_be_drop = list(df.columns)[0]
    df = df.drop(columns = columns_to_be_drop, axis = 1)

    #filtrando as linhas para que o cabeçalho seja modifcado
    df = df[df.index > 3]
    df = df.drop(columns = [5,9], axis = 1)

    #inserindo coluna mes

    #rename columns
    df.columns = ['codigo',"atributo","classificacao","saldo_anterior","debito","credito","movimento", "saldo"]

    #drop null values from classificacao
    df = df.dropna(subset = ["classificacao"])

    df = df[df['saldo_anterior'] != "Débito"]

    #Limpando os Dados
    df['saldo_anterior'] = df['saldo_anterior'].apply(lambda x: x.replace(".", " ").replace(" ","").replace(",",".")).replace(")", " ").replace("(", " ").replace(",",".")
    df['debito'] = df['debito'].apply(lambda x: x.replace(".", " ").replace(" ","").replace(",","."))
    df['movimento'] = df['movimento'].apply(lambda x: x.replace(".", " ").replace(" ","").replace(",","."))
    df['movimento'] = df['movimento'].apply(lambda x: x.replace("(", " ").replace(" ","").replace(",","."))
    df['movimento'] = df['movimento'].apply(lambda x: x.replace(")", " ").replace(" ","").replace(",","."))
    df['credito'] = df['credito'].apply(lambda x: x.replace(".", " ").replace(" ","").replace(",","."))
    df['saldo'] = df['saldo'].apply(lambda x: x.replace(".", " ").replace(" ","").replace(",","."))
    
    df['saldo'] = df['saldo'].apply(lambda x : x.replace("(", "") if "(" in x else x)
    df['saldo'] = df['saldo'].apply(lambda x : x.replace(")", "") if ")" in x else x)

    df['saldo_anterior'] = df['saldo_anterior'].apply(lambda x : x.replace("(", "") if "(" in x else x)
    df['saldo_anterior'] = df['saldo_anterior'].apply(lambda x : x.replace(")", "") if ")" in x else x)

    df['debito'] = df['debito'].apply(lambda x : x.replace("(", "") if "(" in x else x)
    df['debito'] = df['debito'].apply(lambda x : x.replace(")", "") if ")" in x else x)

    df['credito'] = df['credito'].apply(lambda x : x.replace("(", "") if "(" in x else x)
    df['credito'] = df['credito'].apply(lambda x : x.replace(")", "") if ")" in x else x)
 
    #transformando o tipo dos dados
    df = df[df['saldo'] != 'Saldo']
    df['saldo'] = df['saldo'].astype(float)
    df['saldo_anterior'] = df['saldo_anterior'].astype(float)
    df['credito'] = df['credito'].astype(float)
    df['debito'] = df['debito'].astype(float)
    df['movimento'] = df['movimento'].astype(float)

    df2 = file_.copy()

    mes = pd.to_datetime(df2[1][0][10:20], dayfirst = True).month

    df['mes'] = mes

    depara_mes = {1: "Janeiro",
     2: "Fevereiro",
     3: "Março",
     4: "Abril",
     5: "Maio",
     6: "Junho",
     7: "Julho",
     8: "Agosto",
     9: "Setembro",
     10: "Outubro",
     11: "Novembro",
     12: "Dezembro"

    }

    df['mes'] = df['mes'].map(depara_mes)

    return df

def calculos(df):
    try:    
        x_2601 = df[df['codigo'] == '2601']['saldo'].values[0]
    except:
        x_2601 = 0
    try:
        x_2770 = df[df['codigo'] == '2770']['saldo'].values[0]
    except:
        x_2770 = 0
    try:
        x_4011 = df[df['codigo'] == '4011']['saldo'].values[0]
    except:
        x_4011 = 0
    try:
        x_3001 = df[df['codigo'] == '3001']['saldo'].values[0]
    except:
        x_3001 = 0
    try:
        x_3548 = df[df['codigo'] == '3548']['saldo'].values[0]
    except:
        x_3548 = 0
    try:
        x_3 = df[df['codigo'] == "3"]['saldo'].values[0]
    except:
        x_3 = 0
    try:
        x_4 = df[df['codigo'] == '4']['saldo'].values[0]
    except:
        x_4 = 0
    try:
        x_5 = df[df['codigo'] == '5']['saldo'].values[0]
    except:
        x_5 = 0
    try:
        x_6 = df[df['codigo'] == '6']['saldo'].values[0]
    except:
        x_6 = 0
    try:
        x_2 = df[df['codigo'] == '2']['saldo'].values[0]
    except:
        x_2 = 0
    try:
        x_1351 = df[df['codigo'] == '1351']['saldo'].values[0]
    except:
        x_1351 = 0
    try:
        x_502 = df[df['codigo'] == '502']['saldo'].values[0]
    except:
        x_502 = 0
    try:
        x_590 = df[df['codigo'] == '590']['saldo'].values[0]
    except:
        x_590 = 0
    try:
        x_1920 = df[df['codigo'] == '1920']['saldo'].values[0]
    except:
        x_1920 = 0
    try:
        x_4828 = df[df['codigo'] == '4828']['saldo'].values[0]
    except:
        x_4828 = 0
    try:
        x_4829 = df[df['codigo'] == '4829']['saldo'].values[0]
    except:
        x_4829 = 0
    try:
        x_3086 = df[df['codigo'] == '3086']['saldo'].values[0]
    except:
        x_3086 = 0
    try:
        x_3652 = df[df['codigo'] == '3652']['saldo'].values[0]
    except:
        x_3652 = 0
    try:
        x_2602 = df[df['codigo'] == '2602']['saldo'].values[0]
    except:
        x_2602 = 0
    try:
        x_2600 = df[df['codigo'] == '2600']['saldo'].values[0]
    except:
        x_2600 = 0
    try:
        x_4800 = df[df['codigo'] == '4800']['saldo'].values[0]
    except:
        x_4800 = 0
    try:
        x_3000 = df[df['codigo'] == '3000']['saldo'].values[0]
    except:
        x_3000 = 0
    try:
        x_4452 = df[df['codigo'] == '4452']['saldo'].values[0]
    except:
        x_4452 = 0
    try:
        x_4701 = df[df['codigo'] == '4701']['saldo'].values[0]
    except:
        x_4701 = 0
    try:
        x_4327 = df[df['codigo'] == '4327']['saldo'].values[0]
    except:
        x_4327 = 0

    try:
        x_4654 = df[df['codigo'] == '4654']['saldo'].values[0]
    except:
        x_4654 = 0
    #
    try:
        x_4695 = df[df['codigo'] == '4695']['saldo'].values[0]
    except:
        x_4695 = 0
    #create empty dict
    response = {}

    #margem lucro bruta
    try:
        margem_lucro_bruta = (x_2602 - x_2770 - x_3001 - x_3086 - x_3652) / (x_2602 - x_2770)

        #update dictionary
        response.update({"margem_lucro_bruta": margem_lucro_bruta})

    except:
        response.update({"margem_lucro_bruta": 0})

    #margem de lucro liquida
    try:
        lucro_liquido_exercicio = (x_2600 - x_3000 - x_4800) / (x_2602 - x_2770)

        #update dictionary
        response.update({"margem_lucro_liquido": lucro_liquido_exercicio})

    except:
        response.update({"margem_lucro_liquido": 0})

    #margem de lucro liquida
    try:
        lucro_liquido = (x_2600 - x_3000 - x_4800) 

        #update dictionary
        response.update({"lucro_liquido": lucro_liquido})

    except:
        response.update({"lucro_liquido": 0})

    #ALIQUOTA EFETIVA IR E CSLL (IR / LAIR)
    try:    
        aliquota_efetiva = (x_4828 + x_4829) / (x_2602 - x_2770)
        response.update({"aliquota_efetiva":aliquota_efetiva})

    except:
        response.update({"aliquota_efetiva":0})

    #PESO DAS DESPESAS / CUSTOS ADM / RL
    try:     
        despesas_custos_adm_rl = (x_4011) / (x_2602 - x_2770)
        response.update({"despesas_custos_adm_rl":despesas_custos_adm_rl})

    except:
        response.update({"despesas_custos_adm_rl":0})

    #ebitida
    try:
        ebtida = (x_2600 - x_3000) + (x_4452 + x_4701)
        valor = Decimal(ebtida)
        response.update({"ebtida":locale.currency(valor, grouping=True)})   
    except:
        response.update({"ebtida":0})

    #deprediacao
    try:
        deprediacao = x_4452
        valor = Decimal(deprediacao)
        response.update({"depreciacao":locale.currency(valor, grouping=True)})   
    except: 
        response.update({"depreciacao":0})

    #ccl
    try:
        ccl = x_2 - x_1351
        valor = Decimal(ccl)
        response.update({"ccl":locale.currency(valor, grouping=True)})   
    except:
        response.update({"ccl":0})

    #ILC
    try:
        ilc = x_2 / x_1351
        response.update({"ilc":ilc})   
    except:
        response.update({"ilc":0})

    #ILS
    try:
        ils = (x_2 - x_502) / x_1351
        response.update({"ils":ils})   
    except:
        response.update({"ils":0})

    #ILG
    try:
        ilg = (x_2 + x_590) / (x_1351 + x_1920)
        response.update({"ilg":ilg})   
    except:
        response.update({"ilg":0})

    #ILM
    try:
        ilm = (x_3 / x_1351)
        response.update({"ilm":ilm})   
    except:
        response.update({"ilm":0})
    #endividamento cp
    try:
        endividamento_cp = x_1351 / (x_1351 + x_1920)
        response.update({"endividamento_cp":endividamento_cp})   
    except:
        response.update({"endividamento_cp":0})

    #endividamento LP
    try:
        endividamento_lp = x_1920 / (x_1351 + x_1920)
        response.update({"endividamento_lp":endividamento_lp})   
    except:
        response.update({"endividamento_lp":0})
    
    #Receita operacional bruta
    try:
        receita_operacional_bruta = x_2601 
        response.update({"receita_operacional_bruta":receita_operacional_bruta})   
    except:
        response.update({"receita_operacional_bruta":0})       

    #GASTOS
    try:
        gastos = x_3000 + x_4800
        response.update({"gastos":gastos})   
    except:
        response.update({"gastos":0}) 

    #Despesa com Pessoal = 4327
    try:
        despesa_com_pessoal = x_3000 + x_4327
        valor = Decimal(despesa_com_pessoal)
        response.update({"despesa_com_pessoal":locale.currency(valor, grouping=True)})   
    except:
        response.update({"gastos":0}) 

    #impostos
    try:
        impostos = x_4800 + x_4654
        valor = Decimal(impostos)
        response.update({"impostos":locale.currency(valor, grouping=True)})   
    except:
        response.update({"impostos":0}) 

    #depesa financeira
    try:
        despesa_financeira = x_4695
        valor = Decimal(despesa_financeira)
        response.update({"despesa_financeira":locale.currency(valor, grouping=True)})   
    except:
        response.update({"despesa_financeira":0})   

    try:
        lucro_liquido = x_2600 - x_3000 - x_4800
        response.update({"lucro_liquido":lucro_liquido})   
    except:
        response.update({"lucro_liquido":0}) 

    #outras despesas
    try:
        outras_despesas = x_3000 - x_4327 - x_4654 
        response.update({"outras_despesas":outras_despesas})   
    except:
        response.update({"outras_despesas":0}) 

    #disponível
    try:
        disponivel = x_3
        valor = Decimal(disponivel)
        response.update({"disponivel":locale.currency(valor, grouping=True)})   
    except:
        response.update({"disponivel":0})      

    #disponível
    try:
        obrigacoes = (x_1351+ x_1920)
        valor = Decimal(obrigacoes)
        response.update({"obrigacoes":locale.currency(valor, grouping=True)})   
    except:
        response.update({"obrigacoes":0})         

    df = pd.DataFrame(response.items()).T
    new_header = df.iloc[0] #grab the first row for the header
    df = df[1:] #take the data less the header row
    df.columns = new_header

    return df

