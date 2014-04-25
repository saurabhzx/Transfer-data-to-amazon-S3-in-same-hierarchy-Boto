import os
 
import boto
 
from boto.s3.key import Key
 
 
 
rootDir = '/path/media'   #Your path ,it will basically upload the data in s3 in same hierarchy
 
 
 
"""If you have not set up your environment variables by your security credentials than you have to pass your security credentials"""
 
 
 
#s3 = boto.connect_s3('your_access_key_here','your_secret_key_here')
 
 
 
"""else you can simply make the connection it will get security credentials from your environment variables or bash.cfg file"""
 
 
 
#s3 = boto.connect_s3()
 
 
 
bucket = s3.get_bucket("your_bucket_name")
 
count = 0
 
 
 
#count the number of files to be uploaded
 
 
 
for dirName, subdirList, fileList in os.walk(rootDir):
 
    for fname in fileList:
 
        count = count + 1
 
 
 
#upload the files on the AWS s3
 
for dirName, subdirList, fileList in os.walk(rootDir):
 
    for fname in fileList:
 
        key_name = fname
 
        path = dirName
 
        full_key_name = os.path.join(path, key_name)
 
        full_key_name = full_key_name.decode('unicode-escape')
 
        key = bucket.new_key(full_key_name)
 
        key.set_contents_from_filename(full_key_name, policy='public-read')
 
        count = count - 1
 
        print("Files Remaining",count)
 
        print(full_key_name)
