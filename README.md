## Test Your Model Server

```bash
# body.json contains the image data pre-generated from load-test-low-res-image_computer.jpg
# to generate the body.json using a different image, run following command first.
python generate.py IMAGE.jpg

# inference request for fast api
python test_fast_ic.py

# inference request for triton
python test_triton_ic.py
```