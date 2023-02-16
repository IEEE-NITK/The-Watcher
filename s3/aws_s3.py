import os 
import boto3


from dotenv import load_dotenv
load_dotenv()

# Environment variables
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

s3 = boto3.client('s3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
)

response = s3.list_buckets()

s3 = boto3.client('s3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

def create_bucket(bucket_name, region = 'ap-south-1'):
    try:
        s3.list_buckets()
        if bucket_name in [bucket['Name'] for bucket in s3.list_buckets()['Buckets']]:
            print(f"Bucket {bucket_name} already exists\n")
            return True 
        location = {'LocationConstraint': region}
        s3.create_bucket(Bucket=bucket_name, 
                            CreateBucketConfiguration=location)
        print(f"Bucket {bucket_name} created successfully\n")
        return True
    except Exception as e:
        print(f"Error in creating bucket : {e}")
        return False
    
# Use like this:        
# to create bucket in the region asia pacific south 1
# create_bucket('my-bucket-1-vinayak', 'ap-south-1')

# upload file to s3 bucket
def upload_file(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"File {file_name} uploaded successfully\n")
        return True
    except Exception as e:
        print(f"Error in uploading file : {e}\n")
        return False

# Use like this:
# to upload file to s3 bucket named my-bucket-1-vinayak, object name is what you want to name the file in s3 bucket
# upload_file('test.txt', 'my-bucket-1-vinayak', 'test.txt')



# download file from s3 bucket
def download_file(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    try:
        s3.download_file(bucket_name, object_name, file_name)
        print(f"File {file_name} downloaded successfully\n")
        return True
    except Exception as e:
        print(f"Error in downloading file : {e}\n")
        return False

# Use like this:
# to download file from s3 bucket
# download_file('test.txt', 'my-bucket-1-vinayak', 'test.txt')