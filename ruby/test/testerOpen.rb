class TesterOpen
  require "aws-sdk-s3"
  require 'csv'
  require "parquet"

  # retrieve the access key and secret key
  access_key_id = ENV["AKIATG5KAWOPKFLZDZXK"]
  secret_access_key = ENV["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"]

  # create an instance of the s3 client
  Aws.config.update({
                      credentials: Aws::Credentials.new('AKIATG5KAWOPKFLZDZXK', 'FVmBpznSreeuzsyB91uD1tFuUcZ3v5W7GpRQgC7D'),
                      region: 'us-east-1'
                    })
  s3 = Aws::S3::Client.new(
    access_key_id: access_key_id,
    secret_access_key: secret_access_key
  )
  #s3 = Aws::S3.new(access_key_id: access_key_id, secret_access_key: secret_access_key)

  b3 = Aws::S3::Resource.new
  puts(s3)
  puts (b3)
  # get the bucket
  #b = b3.list_buckets.buckets['grupo4-aypmd']
  bucket = b3.bucket('grupo4-aypmd')
  puts("reconocio el bucket")

  # retrieve the objects
  #bucket.objects.each do |obj|
    # puts "#{obj.key} => #{obj.etag}"
    #end

  table = Arrow::Table.load(bucket("tablas/fija/part-0-fija.parquet"))
  # Process data in table
  #table.save("/dev/shm/data-processed.parquet")
  puts(table)


end
