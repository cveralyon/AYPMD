class ApplicationController < ActionController::Base
  require 'aws-sdk'

  # retrieve the access key and secret key
  access_key_id = ENV["AKIATG5KAWOPKFLZDZXK"]
  secret_access_key = ENV["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"]

  # create an instance of the s3 client
  s3 = AWS::S3.new(access_key_id: access_key_id, secret_access_key: secret_access_key)

  # get the bucket
  bucket = s3.buckets['grupo4-aypmd']
  puts("reconocio el bucket")

  # retrieve the objects
  #bucket.objects.each do |object|
  # puts object.key
  # puts object.read
  #end
end
