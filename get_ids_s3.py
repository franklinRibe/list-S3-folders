#         maintainer: @fribeiro-vibrent

#### IMPORT LIBS
import boto3

### VARIABLES
SESSION  = boto3.session.Session()
BUCKET   = 'vrpk8s-prod-hda' 
   
def list_buckets(prefix):
    s3       = boto3.client('s3')
    response = s3.list_buckets()
    response = s3.list_objects(Bucket=BUCKET, Prefix=prefix, Delimiter='/')
    for sub in response.get('CommonPrefixes'):
      subPath = sub.get('Prefix')
      
      if 'FITBIT' in prefix: 
        rs = s3.list_objects(Bucket=BUCKET, Prefix=subPath, Delimiter='/')
      
        for s1 in rs.get('CommonPrefixes'):
            path = s1.get('Prefix')
            print(path)
      else:
          print(subPath)    
      
def main():

    prefix = ['APPLE_HEALTHKIT/HEALTHKIT_DATA/', 'FITBIT/']
    for p in prefix:
      list_buckets(p)

if __name__ == '__main__':
    main()