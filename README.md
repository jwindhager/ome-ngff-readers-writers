# ome-ngff-readers-writers
Qualitative evaluation of OME-NGFF readers/writers  
Next generation bioimage analysis workflows hackathon 2023 in Zurich, Switzerland

[Dependency graph](https://drive.google.com/file/d/1N9tA_xWy38mv3tq1UXw0Btmj4H_XhcnT/view?usp=sharing)

[Evaluation sheet](https://docs.google.com/spreadsheets/d/1airVWkmQGaVopHgtW1tL8k4YJM55DO9I5QA6jnpu1nk/edit?usp=sharing)

## Example data

IDR0101A from https://idr.github.io/ome-ngff-samples/

https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457539.zarr

### Download using AWS CLI container

```bash
podman run -v ./aws:/aws amazon/aws-cli --endpoint-url https://uk1s3.embassy.ebi.ac.uk s3 --no-sign-request cp --recursive s3://idr/zarr/v0.4/idr0101A/13457539.zarr /aws
```

### Download using Python / boto3

```python
import os
import boto3
from botocore import UNSIGNED
from botocore.client import Config

endpoint_url = 'https://uk1s3.embassy.ebi.ac.uk'
source_bucket = 'idr'
source_key = 'zarr/v0.4/idr0101A/13457539.zarr'

s3_resource = boto3.resource('s3', endpoint_url=endpoint_url, config=Config(signature_version=UNSIGNED))
bucket = s3_resource.Bucket(source_bucket)

for obj in bucket.objects.filter(Prefix=source_key):
    if not os.path.exists(os.path.dirname(obj.key)):
        os.makedirs(os.path.dirname(obj.key))
    bucket.download_file(obj.key, obj.key) # save to same path
```
