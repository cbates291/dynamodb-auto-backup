# dynamodb-auto-backup
Use cron or lambda to schedule this script and it will automatically backup DynamoDB Tables based on a Tag

* You will want to update the account number field to be your AWS account number.

* If you want to backup an DynamoDB Table, use one of the following tags. You can have the table backed up Daily by using the Tag below. You can set this script to run on a cron to take backups as often as you want.

| Key                 | Value     | Explanation                         | Required?   |
|-------------------- |-----------|-------------------------------------|-------------|
| Backup              | True      | Used to allow Daily Backups         | YES         |

*  If you are using Lambda (AWS) you will want to edit the end of the script to call the handler you are using within Lambda, and you can set a CloudWatch Event to set a cron to run the backup when you want.
