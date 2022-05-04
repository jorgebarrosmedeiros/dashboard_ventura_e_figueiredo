#importando as bibliotecas
from urllib import response

from matplotlib.pyplot import bar
from help_functions import data_transform, calculos, convert_data_frame
import streamlit as st
import pandas as pd
from decimal import Decimal
import locale
import plotly.express as px
import plotly.graph_objects as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

from io import StringIO

#settando 
st.set_page_config(layout="wide")
locale.setlocale(locale.LC_ALL, 'pt_BR')


def main():
	# front end elements of the web page 
    st.sidebar.image("file.png")

    job_filter = st.sidebar.selectbox("Páginas", ['Balancete','Dashboard'])

    if job_filter == "Balancete":
        html_temp = """ 
        <div style ="background-color:white;padding:13px"> 
        <h1 style ="color:black;text-align:center;">Balancete Contábil V&F</h1> 
        </div> 
        """

        # display the front end aspect
        st.markdown(html_temp, unsafe_allow_html = True) 
    
    else:
        html_temp = """ 
        <div style ="background-color:white;padding:13px"> 
        <h1 style ="color:black;text-align:center;">Dashboard Contábil V&F</h1> 
        </div> 
        """

        # display the front end aspect
        st.markdown(html_temp, unsafe_allow_html = True) 



    company_type = st.selectbox("Tipo de Empresa", ["Prestadora de Serviço","Comércio"])

    #inportando arquivo
    if job_filter == 'Balancete':
        #uploaded_file = st.file_uploader("Upload do Balancete")
        uploaded_files = st.file_uploader("Upload do Balancete", type="csv", accept_multiple_files=True)

        try:

            if uploaded_files is not None:
                # Can be used wherever a "file-like" object is accepted:                
                raw_data = [pd.read_csv(file,sep = ";",header=None,encoding='ISO-8859-1', skiprows = 4,names=list(range(11))) for file in uploaded_files]                
                #dataframe = pd.concat(raw_data, axis = 0)
                dataframe_final = pd.DataFrame()
                dataframe = pd.DataFrame()
                dataframe_calculos = pd.DataFrame()

                for file in raw_data:
                    dataframe = pd.DataFrame(file)
                    df = data_transform(dataframe)
                    #st.dataframe(df)
                    dataframe_final = pd.concat([dataframe_final,df],join = "outer")
                    
                    response_calculos = calculos(df)
                    response_calculos['mes'] =  df['mes'].values[0]
                    #st.dataframe(response_calculos)
                    dataframe_calculos = pd.concat([dataframe_calculos,response_calculos],join = "outer")

                mes_dict = {'Janeiro':1,'Fevereiro':2,'Março':3,'Abril':4,'Maio':5,'Junho':6,'Julho':7,'Agosto':8,'Setembro':9,'Outubro':10,'Novembro':11,'Dezembro':12}
                dataframe_calculos['depara_mes'] = dataframe_calculos['mes'].map(mes_dict)
                dataframe_calculos = dataframe_calculos.sort_values("depara_mes", ascending = False)

                cols_to_show = ['margem_lucro_bruta', 'margem_lucro_liquido', 'aliquota_efetiva',
                                'despesas_custos_adm_rl','depreciacao', 'ebtida', 'ccl', 'ilc', 'ils', 'ilg', 'ilm',
                                'endividamento_cp', 'endividamento_lp', 'receita_operacional_bruta',
                                'gastos', 'despesa_com_pessoal', 'impostos', 'despesa_financeira',
                                'lucro_liquido', 'outras_despesas', 'disponivel', 'obrigacoes', 'mes']
                
                dataframe_calculos = dataframe_calculos[cols_to_show]

                st.dataframe(dataframe_final)
                st.dataframe(dataframe_calculos)


                fig = go.Figure(data=[go.Table(
                    header=dict(values=list(df.columns),
                                fill_color='darkslategray',
                                align='left',
                                font=dict(color='white', size=11)),
                    cells=dict(values=[df.codigo, df.atributo, df.classificacao, df.saldo_anterior, df.debito, df.credito, df.movimento, df.saldo, df.mes],
                               fill_color='white',
                               align='left'))
                ])
                
                #calculos
                #response_calculos = calculos(df)
                if company_type == "Prestadora de Serviço":
                    columns_to_drop = ["aliquota_efetiva","ils"]
                    response_calculos = response_calculos.drop(columns = columns_to_drop, axis = 1)
                    csv = convert_data_frame(dataframe_calculos)
                    #st.dataframe(response_calculos)
                else:
                    csv = convert_data_frame(dataframe_final)
                    #st.dataframe(response_calculos)
                st.download_button(
                   "Download do Arquivo",
                   csv,
                   "balancete.csv",
                   "text/csv",
                   key='download-csv'
                ) 
        except:
            pass

    else: 
        uploaded_files = st.file_uploader("Upload do Balancete", type="csv", accept_multiple_files=True)

        
        
        if uploaded_files is not None:

            raw_data = [pd.read_csv(file,sep = ";",header=None,encoding='ISO-8859-1', skiprows = 4,names=list(range(11))) for file in uploaded_files] 
            #dataframe = pd.concat(raw_data, axis = 0)
            dataframe_final = pd.DataFrame()
            dataframe = pd.DataFrame()
            dataframe_calculos = pd.DataFrame()

            for file in raw_data:
                dataframe = pd.DataFrame(file)
                df = data_transform(dataframe)
                #st.dataframe(df)
                dataframe_final = pd.concat([dataframe_final,df],join = "outer")
                
                response_calculos = calculos(df)
                response_calculos['mes'] =  df['mes'].values[0]
                #st.dataframe(response_calculos)
                dataframe_calculos = pd.concat([dataframe_calculos,response_calculos],join = "outer")

            mes_dict = {'Janeiro':1,'Fevereiro':2,'Março':3,'Abril':4,'Maio':5,'Junho':6,'Julho':7,'Agosto':8,'Setembro':9,'Outubro':10,'Novembro':11,'Dezembro':12}
            dataframe_calculos['depara_mes'] = dataframe_calculos['mes'].map(mes_dict)
            dataframe_calculos = dataframe_calculos.sort_values("depara_mes", ascending = False)

            cols_to_show = ['margem_lucro_bruta', 'margem_lucro_liquido', 'aliquota_efetiva',
                            'despesas_custos_adm_rl','depreciacao', 'ebtida', 'ccl', 'ilc', 'ils', 'ilg', 'ilm',
                            'endividamento_cp', 'endividamento_lp', 'receita_operacional_bruta',
                            'gastos', 'despesa_com_pessoal', 'impostos', 'despesa_financeira',
                            'lucro_liquido', 'outras_despesas', 'disponivel', 'obrigacoes', 'mes','depara_mes']
            
            response_calculos = dataframe_calculos[cols_to_show]
            response_calculos = pd.DataFrame(response_calculos.iloc[0,:]).T

            response_to_charts = dataframe_calculos[cols_to_show]

            #barplot
            bar_chart = response_to_charts[['gastos','receita_operacional_bruta','lucro_liquido']]
    

            def convert_df(df):
               return df.to_csv().encode('utf-8')

            csv = convert_df(df)

            st.download_button(
               "Download do Arquivo",
               csv,
               "relatorio_contabil.csv",
               "text/csv",
               key='download-csv'
            ) 

            response_to_charts = response_to_charts[['impostos','despesa_financeira','outras_despesas',"despesa_com_pessoal",'gastos','lucro_liquido','receita_operacional_bruta','ebtida','disponivel','mes','depara_mes','ccl','depreciacao']]
            response_to_charts['ebtida'] = response_to_charts['ebtida'].apply(lambda x : x.replace("R$ ", "")  if "R$ " in x else x)
            response_to_charts['ebtida'] = response_to_charts['ebtida'].apply(lambda x : x.replace(",", "x").replace(".","").replace("x",".") if "," in x else x)
            response_to_charts['ebtida'] = response_to_charts['ebtida'].astype(float)

            response_to_charts['impostos'] = response_to_charts['impostos'].apply(lambda x : x.replace("R$ ", "")  if "R$ " in x else x)
            response_to_charts['impostos'] = response_to_charts['impostos'].apply(lambda x : x.replace(".", "x")  if "." in x else x)
            response_to_charts['impostos'] = response_to_charts['impostos'].apply(lambda x : x.replace(",", ".")  if "," in x else x)
            response_to_charts['impostos'] = response_to_charts['impostos'].apply(lambda x : x.replace("x", "")  if "x" in x else x)
            response_to_charts['impostos'] = response_to_charts['impostos'].astype(float)

            response_to_charts['despesa_financeira'] = response_to_charts['despesa_financeira'].apply(lambda x : x.replace("R$ ", "") if "R$ " in x else x)
            response_to_charts['despesa_financeira'] = response_to_charts['despesa_financeira'].apply(lambda x : x.replace(",", "x").replace(".","").replace("x",".") if "," in x else x)
            response_to_charts['despesa_financeira'] = response_to_charts['despesa_financeira'].astype(float)

            response_to_charts['despesa_com_pessoal'] = response_to_charts['despesa_com_pessoal'].apply(lambda x : x.replace("R$ ", "") if "R$ " in x else x)
            response_to_charts['despesa_com_pessoal'] = response_to_charts['despesa_com_pessoal'].apply(lambda x : x.replace(",", "x").replace(".","").replace("x",".") if "," in x else x)
            response_to_charts['despesa_com_pessoal'] = response_to_charts['despesa_com_pessoal'].astype(float)

            response_to_charts['disponivel'] = response_to_charts['disponivel'].apply(lambda x : x.replace("R$ ", "") if "R$ " in x else x)
            response_to_charts['disponivel'] = response_to_charts['disponivel'].apply(lambda x : x.replace(",", "x").replace(".","").replace("x",".") if "," in x else x)
            response_to_charts['disponivel'] = response_to_charts['disponivel'].astype(float)

            response_to_charts['ccl'] = response_to_charts['ccl'].apply(lambda x : x.replace("R$ ", "") if "R$ " in x else x)
            response_to_charts['ccl'] = response_to_charts['ccl'].apply(lambda x : x.replace(",", "x").replace(".","").replace("x",".") if "," in x else x)
            response_to_charts['ccl'] = response_to_charts['ccl'].astype(float)

            lucro_acumulado_lista = []
            for i in range(len(response_to_charts)):
                lucro_acumulado_lista.append(response_to_charts['lucro_liquido'].values[i])
            lucro_acumulado =sum(lucro_acumulado_lista)

            #st.write(response_to_charts)

            ########################################################## COLUNA 1 ################################################################
            if len(response_to_charts) > 1:
                fig_01 = go.Figure()
                fig_01.add_trace(go.Indicator(
                    mode = "number+delta",
                    value = response_to_charts['lucro_liquido'].values[0],
                    title = {"text": "Lucro Líquido<br><span style='font-size:0.8em;color:gray'>Comparativo mês anterior</span><br><span style='font-size:0.8em;color:gray'></span>"},
                    delta = {'reference': round(response_to_charts['lucro_liquido'].values[1],2), 'relative': True},
                    domain = {'x': [0.5, 0.5], 'y': [0, 0]}))

                fig_02 = go.Figure()
                fig_02.add_trace(go.Indicator(
                    mode = "number",
                    value = lucro_acumulado,
                    title = {"text": "Lucro Acumulado<br><span style='font-size:0.8em;color:gray'></span><br><span style='font-size:0.8em;color:gray'></span>"},
                    domain = {'x': [0.5, 0.5], 'y': [0, 0]}))

                fig_03 = go.Figure()
                fig_03.add_trace(go.Indicator(
                    mode = "number+delta",
                    value = response_to_charts['ccl'].values[0],
                    title = {"text": "Capital de Giro<br><span style='font-size:0.8em;color:gray'>Comparativo mês anterior</span><br><span style='font-size:0.8em;color:gray'></span>"},
                    delta = {'reference': response_to_charts['ccl'].values[1], 'relative': True},
                    domain = {'x': [0.5, 0.5], 'y': [0, 0]})) 

            else:
                fig_01 = go.Figure()
                fig_01.add_trace(go.Indicator(
                    mode = "number",
                    value = response_to_charts['lucro_liquido'].values[0],
                    title = {"text": "Lucro Líquido<br><span style='font-size:0.8em;color:gray'>Comparativo mês anterior</span><br><span style='font-size:0.8em;color:gray'></span>"},
                    domain = {'x': [0.5, 0.5], 'y': [0, 0]}))

                fig_02 = go.Figure()
                fig_02.add_trace(go.Indicator(
                    mode = "number",
                    value = lucro_acumulado,
                    title = {"text": "Lucro Acumulado<br><span style='font-size:0.8em;color:gray'>Comparativo mês anterior</span><br><span style='font-size:0.8em;color:gray'></span>"},
                    domain = {'x': [0.5, 0.5], 'y': [0, 0]}))

                fig_03 = go.Figure()
                fig_03.add_trace(go.Indicator(
                    mode = "number",
                    value = response_to_charts['disponivel'].values[0],
                    title = {"text": "Disponível<br><span style='font-size:0.8em;color:gray'>Comparativo mês anterior</span><br><span style='font-size:0.8em;color:gray'></span>"},
                    domain = {'x': [0.5, 0.5], 'y': [0, 0]})) 


            cols = st.columns(3)
            cols[1].plotly_chart(fig_01)
            cols[0].plotly_chart(fig_02)
            cols[2].plotly_chart(fig_03)

             ########################################################## COLUNA 2 ################################################################
            
        

            ########################################################## COLUNA 3 ################################################################
            response_to_charts_ascending = response_to_charts.sort_values("depara_mes", ascending = True)

            fig_04 = go.Figure()
            fig_04.add_trace(go.Bar(x= list(response_to_charts_ascending['mes']), y=list(response_to_charts_ascending['receita_operacional_bruta']), xaxis='x2', yaxis='y2',
                            marker=dict(color='#7294a8'),      
                            name='Receita Operacional Bruta'))
            fig_04.add_trace(go.Bar(x= list(response_to_charts_ascending['mes']), y=list(response_to_charts_ascending['gastos']), xaxis='x2', yaxis='y2',
                            marker=dict(color='#2984a8'),      
                            name='Gastos'))
            
            fig_04.update_layout(
                    title_text = 'Comparativo Mensal',
                    height = 500,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    margin = {'t':75, 'l':50},
                    yaxis = {'domain': [0, .45]},
                    xaxis2 = {'anchor': 'y2'},
                    yaxis2 = {'domain': [.15, 1], 'anchor': 'x2', 'title': ''})

            fig_05 = go.Figure()
            fig_05.add_trace(go.Line(x= list(response_to_charts_ascending['mes']), y=list(response_to_charts_ascending['lucro_liquido']), xaxis='x2', yaxis='y2',
                            marker=dict(color='#7294a8'),      
                            name='Lucro Líquido'))

            fig_05.update_layout(
                    title_text = 'Lucro Líquido',
                    height = 500,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    margin = {'t':75, 'l':50},
                    yaxis = {'domain': [0, .45]},
                    xaxis2 = {'anchor': 'y2'},
                    yaxis2 = {'domain': [.15, 1], 'anchor': 'x2', 'title': ''})
#
            cols_2 = st.columns(2)
            cols_2[0].plotly_chart(fig_04)
            cols_2[1].plotly_chart(fig_05)

            bar_plot = response_to_charts.rename(columns = {'impostos': "Impostos",'despesa_financeira':"Despesa Financeira","outras_despesas":"Outras Despesas",
                                                           "despesa_com_pessoal": "Despesa com Pessoal","lucro_liquido": "Lucro Líquido"})
            bar_plot = bar_plot[['Impostos','Despesa Financeira','Outras Despesas','Despesa com Pessoal','Lucro Líquido']]
            response_pie_chart = pd.DataFrame(bar_plot.iloc[0,:6]).reset_index()
            response_pie_chart.columns = ['gasto','valor']
            
            for i in range(len(response_pie_chart)):
                response_pie_chart.loc[i, 'percentual_valor'] = (response_pie_chart['valor'].loc[i] / response_pie_chart['valor'].sum())*100

            fig_06 = go.Figure()
            response_pie_chart = response_pie_chart.sort_values("percentual_valor", ascending = True)
            fig_06.add_trace(go.Bar(x= list(response_pie_chart['percentual_valor']), y=list(response_pie_chart['gasto']), xaxis='x2', yaxis='y2',
                            marker=dict(color='#2984a8'),
                            orientation='h',      
                            name='Distribuição de Gastos'))
           
            fig_06.update_layout(
                    title_text = 'Distribuição de Gastos',
                    height = 500,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    margin = {'t':75, 'l':50},
                    yaxis = {'domain': [0, .45]},
                    xaxis2 = {'anchor': 'y2'},
                    yaxis2 = {'domain': [.15, 1], 'anchor': 'x2', 'title': 'Valor'})

            col1, col2 = st.columns([2, 2])
            col1.plotly_chart(fig_06)
            col2.plotly_chart(fig_06)
            #cols_3[0].plotly_chart(fig_06)


            table = response_to_charts[['impostos','despesa_com_pessoal','despesa_financeira','outras_despesas','lucro_liquido','mes']]
            table = table.rename(columns = {'impostos': "Impostos",'despesa_financeira':"Despesa Financeira","outras_despesas":"Outras Despesas",
                                 "despesa_com_pessoal": "Despesa com Pessoal","lucro_liquido": "Lucro Líquido"})
        

        else:
            pass
       
if __name__ == "__main__":
	main()   