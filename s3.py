import boto3
s3 = boto3.resource("s3")
for bucket in s3.buckets.all():
    print(bucket.name)

import boto3

s3 = boto3.resource("s3")
bucket = s3.Bucket("xim-aws-cli-test-996621491488")

bucket.download_file("hello.txt", "hello_from_s3.txt")
print("다운로드 완료")
