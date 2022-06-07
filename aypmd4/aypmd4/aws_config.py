import sys
import io
import boto3
import pandas as pd
import pyarrow.parquet as pq
from botocore.exceptions import ClientError


athena = boto3.client('athena', region_name="us-east-1", 
    aws_access_key_id='AKIATG5KAWOPKFLZDZXK',
    aws_secret_access_key='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')

def AthenaQuery(query):
    athena_job_query = athena.start_query_execution(
            QueryString='SELECT * from fija LEFT OUTER JOIN codigo_comuna_region on fija.cod_com = codigo_comuna_region.cod_com WHERE codigo_comuna_region.comuna = "ARICA"',
            QueryExecutionContext={
                'Database': 'grupo4-database'
            },
            ResultConfiguration={
                'OutputLocation': 's3://aypmd-grupo4/athena/'
            }
        )

    query_execution_id = athena_job_query['QueryExecutionId']
    results = athena.get_query_results(QueryExecutionId=query_execution_id)
    data = CreateDicc(results)
    return data
    
def CreateDicc(result):
    dicc = {}
    i =0
    for d in result['ResultSet']['Rows']:
        lista = []
        for elem in d['Data']:
            lista.append(elem['VarCharValue'])
        dicc[i] = lista
        i+=1
    return dicc

  





