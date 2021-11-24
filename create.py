import pysnow
import config
from pprint import pprint

c = pysnow.Client(instance=config.snow_instance, user=config.snow_username, password=config.snow_password)

incident = c.resource(api_path='/table/incident')
short_description = 'PySNOW is awesome!'
description = 'Incident created programmatically'

def incident_exists(short_description):
    result = incident.get(query={'short_description': short_description}, stream=True)
    return bool(result.first_or_none())

if not incident_exists(short_description):
    new_record = {
        'short_description': short_description,
        'description': description
    }
    result = incident.create(payload=new_record)
    if result:
        print('Created new incident!')
else:
    print(f'Incident with short description "{short_description}" already exists, doing nothing')
