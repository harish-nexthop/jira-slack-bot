import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()


def get_open_tickets():
    base_url = os.getenv("JIRA_BASE_URL")
    email = os.getenv("JIRA_EMAIL")
    apiToken = os.getenv("JIRA_API_TOKEN")

    getUrl = base_url + "/rest/api/3/search/jql"
    jql = {
        "jql": "project = IT AND status != Done"
    }

  
    get_request = requests.get(getUrl, params = jql, auth = (email, apiToken))
    values = get_request.json()
    print(values)
    print (values["issues"])

    


get_open_tickets()



    


    