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
print("pasa222")

s3 = boto3.resource('s3',
                    aws_access_key_id= 'AKIATG5KAWOPKFLZDZXK',
                    aws_secret_access_key='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')

#s3 = boto3.client('s3')
#bucket = s3.Bucket('grupo4-aypmd')


buffer = io.BytesIO()
#s3 = boto3.resource('s3')
#s3_object = s3.Object('bucket-name', 'key/to/parquet/file.gz.parquet')
#s3_object.download_fileobj(buffer)
#table = pq.read_table(buffer)
#df = table.to_pandas()

s3_object = s3.Object('grupo4-aypmd', 'tablas/codigo_comuna_region/codigo_comuna_region.parquet')
s3_object.download_fileobj(buffer)
table = pq.read_table(buffer)
df = table.to_pandas()
print(df)
print("METODO")

#my_bucket=s3.Bucket('grupo4-aypmd')
#bucket_list = []
#for file in my_bucket.objects.filter(Prefix = 'tablas'):
#    print(file)
#    file_name=file.key
#    if file_name.find(".parquet")!=-1:
#        file.download_fileobj(buffer)
#        table = pq.read_table(buffer)
#        df = table.to_pandas()
#        print("TERMINA 1 TABLA")
#        bucket_list.append(file.key)
#length_bucket_list=print(len(bucket_list))
#print(bucket_list[0:10])

