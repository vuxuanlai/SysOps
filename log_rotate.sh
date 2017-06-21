#!/bin/bash

DATE=`date +%Y-%m-%d`
MONTH=`date +%m`
cd /your/log/directory

# Find all log have created before $DATE not include compressed files
find . ! -newermt $DATE -and ! -name "*.tar.gz"

# Compress all log and delete logs
tar -cvfz your_tar_file_name$MONTH.tar.gz "${files[@]}"
rm "${files[@]}"

# Regis ter in crontab run every first day of month:
# 0 0 1 * * /monitor/log_rotate.sh
