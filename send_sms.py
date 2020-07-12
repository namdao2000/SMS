from __future__ import print_function
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
import credentials # You will need to provide your own file.

class SMSender():
    client_id = credentials.CLIENT_ID  # str |
    client_secret = credentials.CLIENT_SECRET  # str |
    grant_type = 'client_credentials'  # str |  (default to 'client_credentials')

    def __init__(self):
        self.configuration = Telstra_Messaging.Configuration()
        self.configuration.access_token = credentials.ACCESS_TOKEN

    def authenticate_client(self):
        api_instance = Telstra_Messaging.AuthenticationApi(Telstra_Messaging.ApiClient(self.configuration))

        try:
            # Generate OAuth2 token
            self.api_response = api_instance.auth_token(self.client_id, self.client_secret, self.grant_type)

        except ApiException as e:
            print("Exception when calling AuthenticationApi->auth_token: %s\n" % e)

    def provision_client(self):
        api_instance = Telstra_Messaging.ProvisioningApi(Telstra_Messaging.ApiClient(self.configuration))
        provision_number_request = Telstra_Messaging.ProvisionNumberRequest()

        try:
            # Create Subscription
            api_response = api_instance.create_subscription(provision_number_request)
            api_response = api_instance.get_subscription()

        except ApiException as e:
            print("Exception when calling ProvisioningApi->create_subscription: %s\n" % e)

    def send_sms(self, msg_to, msg_body):
        api_instance = Telstra_Messaging.MessagingApi(Telstra_Messaging.ApiClient(self.configuration))
        send_sms_request = Telstra_Messaging.SendSMSRequest(to=msg_to, body=msg_body)

        try:
            # Send SMS
            api_response = api_instance.send_sms(send_sms_request)
            # pprint(api_response)
            return True

        except ApiException as e:
            print("Exception when calling MessagingApi->send_sms: %s\n" % e)

Messaging = SMSender()
Messaging.send_sms("phone number", "message")