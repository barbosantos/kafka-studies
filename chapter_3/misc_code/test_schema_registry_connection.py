from confluent_kafka.schema_registry import SchemaRegistryClient


def test_schema_registry_connection(schema_registry_url):
    try:
        # Create a SchemaRegistryClient instance
        sr_client = SchemaRegistryClient({"url": schema_registry_url})

        # Check the connection to the Schema Registry
        subjects = sr_client.get_subjects()
        print("Connection to Schema Registry successful.")
        print("Subjects available in the Schema Registry:")
        '''for subject in subjects:
            print(subject)

        return True'''
    except Exception as e:
        print(f"Error connecting to Schema Registry: {e}")
        return False


# Define the URL of the Schema Registry (change to your local Schema Registry URL)
schema_registry_url = "http://0.0.0.0:8081"

# Test the connection to the Schema Registry
test_schema_registry_connection(schema_registry_url)
