
import boto3
import time


client = boto3.client(
    's3',
    aws_access_key_id='AKIATG5KAWOPKFLZDZXK',
    aws_secret_access_key='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',

)
athena = boto3.client('athena', region_name="us-east-1", 
    aws_access_key_id='AKIATG5KAWOPKFLZDZXK',
    aws_secret_access_key='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')

'''athena_job_query = athena.start_query_execution(
        QueryString='SELECT * from codigo_comuna_region LIMIT 10 ',
        QueryExecutionContext={
            'Database': 'grupo4-database'
        },
        ResultConfiguration={
            'OutputLocation': 's3://aypmd-grupo4/athena/'
        }
    )
query_execution_id = athena_job_query['QueryExecutionId']
athena_job_status_query = athena.get_query_execution(QueryExecutionId=query_execution_id)'''



s3 = boto3.resource('s3',
                    aws_access_key_id= 'AKIATG5KAWOPKFLZDZXK',
                    aws_secret_access_key='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')


#time.sleep(6)
#print("slepea 6")
#results = athena.get_query_results(QueryExecutionId=query_execution_id)

#print(results)


'''dicc = {}
i =0;
for d in results['ResultSet']['Rows']:
  lista = []
  for elem in d['Data']:
      lista.append(elem['VarCharValue'])
  dicc[i] = lista
  i+=1'''

#print(dicc)

def toDic(result):
    dicc = {}
    i =0
    for d in result['ResultSet']['Rows']:
        lista = []
        for elem in d['Data']:
            if len(elem)  != 0:
                lista.append(elem['VarCharValue'])
            else:
                lista.append('')
        if i != 0:
            if  (lista[5]) !='':                 
                sup = float(lista[5])
                precio = float(lista[1])
                div = round(precio/sup,1)
                lista.append(div)     
            else:
                lista.append("No puntuado")       
        dicc[i] = lista
        i+=1
    dicc.pop(0)
    return dicc

def AthenaQuery(query):
    athena_job_query = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': 'grupo4-database'
        },
        ResultConfiguration={
            'OutputLocation': 's3://aypmd-grupo4/athena/'
        }
    )
    query_execution_id = athena_job_query['QueryExecutionId']
    athena_job_status_query = athena.get_query_execution(QueryExecutionId=query_execution_id)
    time.sleep(12)
    print("---SLEPEA 15 AEN aws_config.py---")
    results = athena.get_query_results(QueryExecutionId=query_execution_id)
    #print(results)
    dic = toDic(results)
    #print(dic)
    return dic

print("VEO EL DICT  Y LO MANIPULO")

def ConvertToList(result):
    comunas = []
    for d in result['ResultSet']['Rows']:
        for elem in d['Data']:
            comunas.append(elem['VarCharValue'])
    comunas.pop(0)
    return comunas

def GetComunas():
    athena_job_query = athena.start_query_execution(
        QueryString='SELECT DISTINCT comuna from codigo_comuna_region ASC',
        QueryExecutionContext={
            'Database': 'grupo4-database'
        },
        ResultConfiguration={
            'OutputLocation': 's3://aypmd-grupo4/athena/'
        }
    )
    query_execution_id = athena_job_query['QueryExecutionId']
    athena_job_status_query = athena.get_query_execution(QueryExecutionId=query_execution_id)
    time.sleep(5)
    print("---SLEPEA 15 AEN aws_config.py---")
    results = athena.get_query_results(QueryExecutionId=query_execution_id)
    comunas = ConvertToList(results)
    return comunas

def GetPeriodo():
    athena_job_query = athena.start_query_execution(
        QueryString='SELECT DISTINCT periodo from fija ASC',
        QueryExecutionContext={
            'Database': 'grupo4-database'
        },
        ResultConfiguration={
            'OutputLocation': 's3://aypmd-grupo4/athena/'
        }
    )
    query_execution_id = athena_job_query['QueryExecutionId']
    athena_job_status_query = athena.get_query_execution(QueryExecutionId=query_execution_id)
    time.sleep(5)
    print("---SLEPEA 15 AEN aws_config.py---")
    results = athena.get_query_results(QueryExecutionId=query_execution_id)
    periodos = ConvertToList(results)
    return periodos

def GetRegiones():
    athena_job_query = athena.start_query_execution(
        QueryString='SELECT DISTINCT cod_region from codigo_comuna_region ORDER BY cod_region ASC',
        QueryExecutionContext={
            'Database': 'grupo4-database'
        },
        ResultConfiguration={
            'OutputLocation': 's3://aypmd-grupo4/athena/'
        }
    )
    query_execution_id = athena_job_query['QueryExecutionId']
    athena_job_status_query = athena.get_query_execution(QueryExecutionId=query_execution_id)
    time.sleep(5)
    print("---SLEPEA 15 AEN aws_config.py---")
    results = athena.get_query_results(QueryExecutionId=query_execution_id)
    regiones = ConvertToList(results)
    return regiones

def AvgAvaluoFiscal(query):
    athena_job_query = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': 'grupo4-database'
        },
        ResultConfiguration={
            'OutputLocation': 's3://aypmd-grupo4/athena/'
        }
    )
    query_execution_id = athena_job_query['QueryExecutionId']
    athena_job_status_query = athena.get_query_execution(QueryExecutionId=query_execution_id)
    time.sleep(10)
    print("---SLEPEA 10 avaluo fiscalAEN aws_config.py---")
    results = athena.get_query_results(QueryExecutionId=query_execution_id)
    avg = round(float(ConvertToList(results)[0]),2)
    return avg


