import json
import os

import requests

from demographics.constants import *
from demographics.normalize import normalize
from demographics.schema import Appplication


class Townscript:

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": os.getenv('TOWNSCRIPT_AUTH')
    }

    @classmethod
    def get_pending(cls) -> list[dict]:
        """get_pending_application returns a dictionary of pending applications

        Returns:
            dict: dictionary of pending applications
        """
        applications_url = "https://www.townscript.com/api/transaction/getapplicationswithpagination?eventId=302058&status=APPLICATION%20PENDING&&startIndex={start_index}&maxResults=10"

        start = 0
        page = True

        data = []

        while page:
            response = requests.post(applications_url.format(start_index=start), headers=cls.headers)
            
            response = response.json()
            response["data"] = json.loads(response["data"])
            data += response["data"]
            start += 10
            if len(response["data"]) == 0:
                page = False
        
        records = []
        for application in data:
            form = {}
            
            temp = application["registrationList"][0]["formAnswers"]
            
            
            for field in temp:
                form[field['questionId']] = field['answer']

            record = {
                "job_title": form[ROLE],
                "organization": normalize(form[ORG]),
                "city": form[CITY],
                "gender": form[GENDER],
                "no_of_devfest": form[NO_OF_DEVFESTS] if int(form[NO_OF_DEVFESTS]) < 10 else 0,
                "gdsc": form[IS_GDSC],
                "gde": form[IS_GDE],
                "wtm": form[IS_WTM],
                "gdg": form[IS_GDG],
                "confirmation": form[CONFIRMATION]
                
            }
            
            schema = Appplication(**record)
            records.append(schema.dict())

        return records


    @classmethod
    def get_approved(cls) -> list[dict]:
        registrations_url = "https://www.townscript.com/api/registration/getRegisteredUsers?eventCode=devfest-2022-chennai"
        
        response = requests.get(registrations_url, headers=cls.headers)
            
        response = response.json()
        response["data"] = json.loads(response["data"])
        data = response["data"]

        
        records = []
        for application in data:
            form = {}
            temp = application["answerList"]

            for field in temp:
                form[field['uniqueQuestionId']] = field['answer']

            record = {
                "job_title": form[ROLE],
                "organization": normalize(form[ORG]),
                "city": form[CITY],
                "gender": form[GENDER],
                "no_of_devfest": form[NO_OF_DEVFESTS] if int(form[NO_OF_DEVFESTS]) < 10 else 0,
                "gdsc": form[IS_GDSC],
                "gde": form[IS_GDE],
                "wtm": form[IS_WTM],
                "gdg": form[IS_GDG],
                "confirmation": form[CONFIRMATION]
            }

            schema = Appplication(**record)
            records.append(schema.dict())
        
        return records
