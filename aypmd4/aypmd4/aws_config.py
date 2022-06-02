import sys
import boto3
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



my_bucket=s3.Bucket('grupo4-aypmd')
bucket_list = []
for file in my_bucket.objects.filter(Prefix = 'data-sucia'):
    print(file)
    #print("ll")
    file_name=file.key
    if file_name.find(".parquet")!=-1:
        bucket_list.append(file.key)
length_bucket_list=print(len(bucket_list))
print(bucket_list[0:10])
