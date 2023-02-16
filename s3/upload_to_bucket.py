from s3.aws_s3 import upload_file 

import sys

# get bucket name, file name, object name from args
bucket_name = sys.argv[1]
file_name = sys.argv[2]
object_name = sys.argv[3]

# upload file
upload_file(file_name, bucket_name, object_name)
