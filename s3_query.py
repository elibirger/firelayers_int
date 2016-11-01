__author__ = 'ebirger'

import boto
import boto.ec2
import csv

# use ~/.boto file for credentials
#aws_access_key_id = 'XXX'
#aws_secret_access_key = 'XXX'

conn = boto.ec2.connect_to_region('eu-west-1')
reservations = conn.get_all_instances()


with open('filename', 'wb') as myfile:
    fieldnames = ['Name', 'Public IP', 'Private IP', 'other tags']
    wr = csv.DictWriter(myfile, fieldnames=fieldnames)
    wr.writeheader()

    for reservation in reservations:
        for instance in reservation.instances:

            name = instance.tags.get('Name')
            pub_ip = instance.ip_address
            ip = instance.private_ip_address

            other_tags = list()
            for tag in instance.tags:
                if tag != 'Name':
                    other_tags.append(str(instance.tags.get(tag)))

            wr.writerow({'Name': str(name), 'Public IP': str(pub_ip), 'Private IP': str(ip), 'other tags': ", ".join(other_tags)})
            other_tags = []

