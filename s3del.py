import boto3

def delete_all_objects(bucket_name):
    # Set up S3 client
    s3 = boto3.client('s3')

    # Retrieve the list of all objects in the specified bucket
    objects = s3.list_objects_v2(Bucket=bucket_name)

    # Check if there are any objects in the bucket
    if 'Contents' in objects:
        # Iterate through each object in the bucket and delete it
        for obj in objects['Contents']:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            print(f"Deleted object: {obj['Key']}")
        
        # If the number of objects exceeds 1000, call the function recursively
        while objects['KeyCount'] >= 1000:
            objects = s3.list_objects_v2(Bucket=bucket_name)
            for obj in objects['Contents']:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Deleted object: {obj['Key']}")
    else:
        print("No objects to delete.")

# Name of the bucket from which you want to delete all objects
bucket_name = 'your-bucket-name'

# Call the function to delete objects from the bucket
delete_all_objects(bucket_name)
