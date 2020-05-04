import boto3
from testcontainer_python_minio import MinioContainer


def test_connection():

    config = MinioContainer()

    with config as container:
        endpoint_url = container.get_url()
        s3_client = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=container.accessKey(),
            aws_secret_access_key=container.secretKey(),
        )
        s3_client.create_bucket(Bucket="test")

        buckets = s3_client.list_buckets()
        assert len(buckets["Buckets"]) == 1
        assert buckets["Buckets"][0]["Name"] == "test"
