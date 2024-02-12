## Producers
Two types of producers: Synchronous and Asynchronous

Parameters for producers can affect performance like max size, throughput, latency.

Brokers receive the messages and send acks back. TCP protocol used. The quotas and throttling depends on how fast producers send data. If too fast the producer client can save in memory (buffer) while waiting for the broker to be available. If runout goes, a timeout exception is thrown.

We can adjust quotas parameters in the Kafka configuration for the cluster, which will make all brokers restart to implement the changes (need to bear in mind running applications). Or dynamically via Kafka.sh command line.

## Serialization

Before sending data to the Kafka broker, the producer needs to serialise it. Meaning, convert the record object to byte arrays. This is so data can be sent via network to the broker server.

There are different types of serializers. For example string serializer, json serializer, avro serializer and so on. Avro serializer is implemented from confluent and provides schema registry handling. Saves a new schema if doesn’t exist and returns schema id together with the data record, in a serialized byte array.

### Avro 

Avro is a fast and compact data serialization framework used for storing and communicating data. It uses schemas to define data structures, supports dynamic typing, binary encoding for efficiency, and is language-independent. Avro's schema evolution feature enables backward and forward compatibility between different versions of schemas.

Avro has schema validation bultin. On "avro_hello_world.py" file, if we change the schema when writing to the avro file, and it's not matching, an exception is thrown.

## Partitioning

Partitions are also important in Kafka. They can enable ordering of the data (data ordered withing partitions). For that, we need to send the keys together with the value when producing the records. If keys are null the records are gonna be assigned to the partition using round-robin algorithm (load balancer circular), using the defaultPartioner Kafka method. 
If the keys are not null, Kafka hashes them and makes sure the same keys end up in the same partition (for ordering). This mapping involves taking the hash and using modulus operator % by total number of partitions. 
This means that if we want to increase the number of partitions for the topic we won’t guarantee the keys will end in the same partition. Suggested to create a new topic if we want to change the number of partitions and use streams processor to process the messages to the new topic. 

The way of ordering by always sending the same key to the same partition means that if we have a popular key, we can have a partition with more data (skewed partiton). We can build custom partitioners to deal with that. Or use existing partitioners such as sticky and round robin partitioners that deal with the skew problem (but ordering is not guaranteed). 

The need of ordering comes down to our application needs. If not needed, it might be wise to distribute skew keys across partitions.

## Schema Registry

Schema registry can be used for storing our schemas. Used for data quality and governance.
We can use it locally via confluent library poiting the url to localhost

```python

from confluent_kafka.schema_registry import SchemaRegistryClient
schema_registry_url = 'http://localhost:8083'

```

We can also use kafka cloud schema registry, or it's version on kubernetes (e.g. strimzi https://github.com/lsst-sqre/strimzi-registry-operator) and more.
