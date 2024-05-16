import requests
import json
from sql import logger

logging = logger(__name__)


class APIInterface:
    @staticmethod
    def post(route, data=None, headers=None):
        try:
            url = route
            print("POST request sent")
            print(f"url = {url}, data = {data}")
            response = requests.post(url, json=data, headers=headers)
            if response.status_code >= 400:
                raise Exception(
                    f"Call to {route} failed with {response.status_code} and response {response.text}"
                )
            return json.loads(response.text), response.status_code
        except Exception as error:
            print(f"Error in the POST API request : {error}")

    @staticmethod
    def get(route, params=None, headers=None):
        try:
            url = route
            print("GET request sent")
            print(f"url = {url}, params = {params}")
            response = requests.get(url, params=params, headers=headers)
            if response.status_code >= 400:
                raise Exception(
                    f"Call to {route} failed with {response.status_code} and response {response.text}"
                )
            return json.loads(response.text), response.status_code
        except Exception as error:
            print(f"Error in GET API request: {error}")

    @staticmethod
    def put(route, data=None, headers=None):
        try:
            url = route
            print("PUT request sent")
            print(f"url = {url}, data = {data}")
            response = requests.put(url, json=data, headers=headers)
            if response.status_code >= 400:
                raise Exception(
                    f"Call to {route} failed with {response.status_code} and response {response.text}"
                )
            return json.loads(response.text), response.status_code
        except Exception as error:
            print(f"Error in PUT API request: {error}")

    @staticmethod
    def delete(route, headers=None):
        try:
            url = route
            print("DELETE request sent")
            print(f"url = {url}")
            response = requests.delete(url, headers=headers)
            if response.status_code >= 400:
                raise Exception(
                    f"Call to {route} failed with {response.status_code} and response {response.text}"
                )
            return response.status_code
        except Exception as error:
            print(f"Error in DELETE API request: {error}")
