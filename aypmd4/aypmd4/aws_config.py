import sys
import io
import boto3
import pandas as pd
import pyarrow.parquet as pq
from botocore.exceptions import ClientError
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
    i =0;
    for d in result['ResultSet']['Rows']:
        lista = []
        for elem in d['Data']:
            lista.append(elem['VarCharValue'])
        dicc[i] = lista
        i+=1
    return dicc

def AthenaQuery():
    athena_job_query = athena.start_query_execution(
        QueryString='SELECT * from codigo_comuna_region LIMIT 10 ',
        QueryExecutionContext={
            'Database': 'grupo4-database'
        },
        ResultConfiguration={
            'OutputLocation': 's3://aypmd-grupo4/athena/'
        }
    )
    query_execution_id = athena_job_query['QueryExecutionId']
    athena_job_status_query = athena.get_query_execution(QueryExecutionId=query_execution_id)
    time.sleep(6)
    print("---SLEPEA 6 AEN aws_config.py---")
    results = athena.get_query_results(QueryExecutionId=query_execution_id)
    dic = toDic(results)
    return dic

print("VEO EL DICT  Y LO MANIPULO")
print(AthenaQuery())






