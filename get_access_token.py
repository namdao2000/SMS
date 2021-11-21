from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint

# Defining host is optional and default to https://tapi.telstra.com/v2
api_instance = Telstra_Messaging.AuthenticationApi(Telstra_Messaging.ApiClient())
client_id = '' # str |
client_secret = '' # str |
grant_type = 'client_credentials' # str |  (default to 'client_credentials')
scope = 'scope_example' # str | NSMS (optional)

try:
    # Generate OAuth2 token
    api_response = api_instance.auth_token(client_id, client_secret, grant_type, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_token: %s\n" % e)
