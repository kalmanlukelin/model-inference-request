import json, base64, sys


filename = "mug.jpg" if len(sys.argv) == 1 else sys.argv[1]
with open(filename, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    image = encoded_string.decode('utf-8')
    
    with open("body.json", "w") as fp:
        query = { "maxResults": 5, "image": { "data": image } }
        request = {
            "inputs": [ {"name": "REQUEST", "shape": [ 1 ], "datatype": "BYTES", "data": [ json.dumps(query) ] } ],
            "outputs": [ {"name": "RESPONSE"} ]
        }

        json.dump(request, fp)
