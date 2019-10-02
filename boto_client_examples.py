"""Boto3 Client Examples"""

import Utils.utils as utils
import boto3
import json

if __name__ == "__main__":
    client = boto3.client('rds')
    rds_instances = client.describe_db_instances()
    for db_instance in rds_instances['DBInstances']:
        # print(repr(db_instance))
        # print(json.dumps(db_instance, default=utils.datetime_serializer))
        db_inst_id = utils.get_key_value(db_instance, 'DBInstanceIdentifier')
        db_inst_status = utils.get_key_value(db_instance, 'DBInstanceStatus')
        print(f'DBInstanceIdentifier - {db_inst_id} \t DBInstanceStatus - {db_inst_status}')
