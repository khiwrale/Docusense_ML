#!/usr/bin/env python
# coding: utf-8
# pip install boto3

import os
import shutil
from shutil import copyfile
import boto3
import pandas as pd
from PIL import Image
import io
import pysftp


class GetFiles():

   def get_awsfiles(self,bucket_name,region,id,key):
    try:
      s3 = boto3.resource(service_name='s3',region_name=region,aws_access_key_id=id,aws_secret_access_key=key)
      user_bucket = s3.Bucket(bucket_name)
    except:
      print('Error while fetching user S3 bucket')
    for file in user_bucket.objects.all():
      try:
        user_bucket.download_file(file.key,f'/content/sample_data/{file.key}')
      except:
        print('Could not download file - {}'.format(file.key))

    print('File download Completed')
    

    def get_localfiles(self,localfolder,storagefolderpath):
      try:
        folder = os.listdir(localfolder)
      except:
        print('No files in folder')
      for file in folder:
        try:
          file_name = os.path.join(localfolder, file)
          if os.path.isfile(file_name):
              shutil.copy(file_name, storagefolderpath + file)
        except:
          print('Could not download file')
      print('File Transfer Completed')
