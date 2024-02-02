from Models import BASE, AID, endpoint
from connector import super_httpx, http_error_handler

aid = AID(aid=1111)

class ThousandEyes:

    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization' : 'Bearer ' + self.token, 'Content-Type' : 'application/json'}
        # Initialize an instance of Agents and provide it with the token
        self.account_groups = self.AccountGroups(headers=self.headers)
        self.agents = self.Agents(headers=self.headers)
        

    class AccountGroups:

        def __init__(self, headers):

            self.headers = headers
            
        @http_error_handler
        def list(self):
           
           endpoint_url = str(BASE.URL) + endpoint.list_account_groups

           result = super_httpx.get(endpoint_url, headers=self.headers)

           return result.json()

    class Agents:

        def __init__(self, headers):
            self.headers = headers

        def create(self, aid):
            # Your implementation to create an agent with the given id
            print(f"Creating agent with aid {aid} and token {self.headers}")
            print((id))

        def list(self, aid):
            # Your implementation to create an agent with the given id
            print(f"list agents with aid {aid} and token {self.headers}")
            print((aid))


# Instantiate the ThousandEyes class
thousandeyes = ThousandEyes(token="3a11313a-d05f-4a2b-bfca-79b44bbe8f4e")

# Now, you can call the agents.create method without passing the token explicitly
print(thousandeyes.account_groups.list())
