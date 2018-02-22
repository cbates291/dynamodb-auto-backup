import boto3
import time

dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
tag_key = "Backup"
tag_value = "True"
matching_tables = []
all_tables = []
region = "us-east-1"
account_number = "229884242446"
current_date = time.strftime("%Y-%m-%d")

#Function to pull all tables based on the tag Backup=True
def get_table_name_by_tag():
        paginator = client.get_paginator("list_tables")
        get_all_tables = paginator.paginate()
        for page in get_all_tables:
                for table in page["TableNames"]:
                        all_tables.append(table)
        for table in all_tables:
                arn = "arn:aws:dynamodb:{}:{}:table/{}".format(region, account_number, table)
                table_tags = client.list_tags_of_resource(
                        ResourceArn=arn
                        )
                for found_tag in table_tags["Tags"]:
                        if found_tag["Key"] == tag_key:
                                if found_tag["Value"] == tag_value:
                                        matching_tables.append(table)
        return matching_tables

def do_backup():
        for objects in matching_tables:
                backup = client.create_backup(
                        TableName= objects,
                        BackupName= objects + current_date
                )
        del matching_tables[:]

#Execute the function to pull all tables with the tag of Backup=True
get_table_name_by_tag()
#Execute the backup
do_backup()
        
