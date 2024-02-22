def custom_hash(input_str):
    # Using a custom hash function for illustration purposes
    hash_value = 0
    prime = 31  # A common prime number used in hash functions

    for char in input_str:
        hash_value = (hash_value * prime + ord(char)) % (2**32)  # 32-bit hash

    return hash_value

# Example usage:
input_data = "test"
hashed_value = custom_hash(input_data)
print(f"Hash value for '{input_data}': {hashed_value}")

# 2971996522