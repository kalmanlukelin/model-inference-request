
"""
THIS FILE IS USED FOR TESTING THE DOCKER IMAGE ON LOCAL MACHINE
Follow the bellow steps:
1) Build docker image with latest code change
2) Run docker image at local port 8080, if port 8080 is unavailable run on different port
3) Change the port number in below 'url' if you ran docker on different port than 8080
4) Run this file in same machine as docker container is running
5) Output will be displayed on terminal
6) You can use different files for testing, just change 'input_data_path' according to the given format
"""
import requests
import base64
import json
import os
curr_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

fast_files = [
    "load-test-low-res-image_computer.jpg",
]

url_fast = "http://localhost:8080/predict"


def test_ic_fast_api(files, url):
    for file in files:
        with open(file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        body = {
            "features": [
                {
                    "featureType": "IMAGE_CLASSIFICATION",
                    "maxResults": 5,
                }
            ],
            "image": {"data": encoded_string.decode(), "maxResults": 5},
            "maxResults": 5
        }
        response = requests.post(url, json=body)
        result = json.loads(response.text)
        print(result)


test_ic_fast_api(fast_files, url_fast)
