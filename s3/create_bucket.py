from s3.aws_s3 import create_bucket 

import sys

# get bucket name and region from args
bucket_name = sys.argv[1]
region = sys.argv[2]

# create bucket
create_bucket(bucket_name, region)