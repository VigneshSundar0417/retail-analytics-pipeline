import boto3

def upload_to_s3(local_file, bucket_name, s3_file):

    s3 = boto3.client("s3")

    s3.upload_file(local_file, bucket_name, s3_file)

    print(f"Uploaded {local_file} → S3 bucket {bucket_name}")
    # Cloud Storage Layer Simulation

bucket_name = "vicky-retail-raw-data"

upload_to_s3(
    "sales_raw.csv",
    bucket_name,
    "raw/sales_raw.csv"
)