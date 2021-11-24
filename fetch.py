import pysnow
import config
from pprint import pprint

c = pysnow.Client(instance=config.snow_instance, user=config.snow_username, password=config.snow_password)

incident = c.resource(api_path='/table/incident')

response = incident.get(query={'state': 1}, stream=True)

#for record in response.all():
#    pprint(record)

pprint(response.first_or_none())
