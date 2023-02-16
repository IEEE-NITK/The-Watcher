#!/bin/bash

set -e

BUCKET_NAME='<ENTER_YOU_BUCKET_NAME_HERE>'
LOG_FILE='cron_logs.txt'

## This will create a cron job that will run every 30 minutes and upload the image to the bucket
*/30 */6 * * * python3 s3/upload_to_bucket.py $BUCKET_NAME image-1.png image-1.png > $LOG_FILE



