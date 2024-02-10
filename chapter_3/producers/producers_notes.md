## Producers

Need 3 main components in its configuration:
- Topic name
- key.serializer
- value.serializer

## Avro Producer

- Utilizes confluent avro serializer
- Writes schemas to Schema Registry.
- Schema registry needs to be running. Can use confluent library and access localhost to access it.


## Synchronous Kafka Producer

- In a synchronous approach, the producer waits for the acknowledgment from the Kafka broker after sending each message.
- The producer sends messages one by one and blocks until it receives confirmation (ack) from the broker that the message has been successfully received and replicated by the Kafka cluster.
- This approach ensures that messages are sent and processed in order and provides stronger delivery guarantees but may result in slower throughput due to waiting for acknowledgments.

## Asynchronous Kafka Producer


- In an asynchronous approach, the producer does not wait for acknowledgments after sending messages.
- The producer sends messages in batches or individually without waiting for acknowledgments from the broker.
- This approach allows for higher throughput as the producer can continue sending messages without waiting for acknowledgments, but it may result in potential message loss if the producer fails before receiving acknowledgments.
- Developers need to handle error cases and retries in asynchronous producers to ensure message delivery.