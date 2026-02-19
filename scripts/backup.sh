#!/bin/bash

BACKUP_DIR=/var/backups/web
SOURCE_DIR=/opt/pyweb

DATE=$(date +%Y_%m_%d_%H%M)


#creation of tar archive
tar -czf $BACKUP_DIR/web_backup_$DATE.tar.gz $SOURCE_DIR

echo the exit code of tar is : $?
#deletion of backups more than 7 days old
find $BACKUP_DIR -type f -name "*.tar.gz" -mtime +7 -print -delete
