# Python Testcontainer Minio

## Usage

```python
import boto3
from testcontainer_python_minio import MinioContainer

def test_something():
    config = MinioContainer()

    with config as container:
        endpoint_url = container.get_url()
        
        s3_client = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=container.accessKey(),
            aws_secret_access_key=container.secretKey(),
        )

        # do something...
``` 