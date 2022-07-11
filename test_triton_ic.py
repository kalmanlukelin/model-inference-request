
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


triton_files = [
    "body.json",
]

url_triton = "http://localhost:8080/v2/models/ic_full/infer"


def test_ic_triton_api(files, url):
    for file in files:
        with open(file, "rb") as image_file:
            response = requests.post(url, json=json.load(image_file))
        print(response.json())


test_ic_triton_api(triton_files, url_triton)
