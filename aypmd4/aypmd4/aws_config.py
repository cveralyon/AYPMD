import sys
import io
import boto3
import pandas as pd
import pyarrow.parquet as pq
from botocore.exceptions import ClientError


client = boto3.client(
    's3',
    aws_access_key_id='AKIATG5KAWOPKFLZDZXK',
    aws_secret_access_key='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',
    
)
athena = boto3.client('athena', region_name="us-east-1", 
    aws_access_key_id='AKIATG5KAWOPKFLZDZXK',
    aws_secret_access_key='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')

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
     


s3 = boto3.resource('s3',
                    aws_access_key_id= 'AKIATG5KAWOPKFLZDZXK',
                    aws_secret_access_key='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')

#s3 = boto3.client('s3')
#bucket = s3.Bucket('grupo4-aypmd')


# -------- CODIGO COMUNA REGION --------------------------
buffer = io.BytesIO()
s3_object = s3.Object('grupo4-aypmd', 'tablas/codigo_comuna_region/codigo_comuna_region.parquet')
s3_object.download_fileobj(buffer)
table = pq.read_table(buffer)
df_ccr = table.to_pandas()
#print(df_ccr)

# -------- CODIGO DESTINO --------------------------
buffer = io.BytesIO()
s3_object = s3.Object('grupo4-aypmd', 'tablas/codigo_destino/codigo_destino.parquet')
s3_object.download_fileobj(buffer)
table = pq.read_table(buffer)
df_cd = table.to_pandas()
#print(df_cd)

results = athena.get_query_results(QueryExecutionId=query_execution_id)
print(results)
for a in results.get("ResultSet").get("Rows"):
    print(a)

dicc = {}
i =0;
for d in results['ResultSet']['Rows']:
  lista = []
  for elem in d['Data']:
      lista.append(elem['VarCharValue'])
  dicc[i] = lista
  i+=1

print(dicc)    
#print(athena_job_query)
#print(athena_job_status_query['QueryExecution']['Status']['State'])





