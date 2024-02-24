### Broker Configuration Parameters:
**broker.id:** Unique identifier for the broker within the Kafka cluster.
**port:** Port number on which the broker listens for client connections.
**advertised.listeners:** Addresses (host/port) that clients can use to connect to the broker. This may differ from the listeners configuration to handle network configurations like NAT.
**log.dirs:** Directory where Kafka stores log data (committed messages).
**num.network.threads:** Number of threads the broker uses for handling network requests.
**num.io.threads:** Number of threads the broker uses for handling disk I/O.
**num.partitions:** Default number of partitions for topics.
**default.replication.factor:** Default replication factor for topic partitions.
**offsets.topic.replication.factor:** Replication factor for the internal Kafka topic used to store consumer group offsets.
**log.retention.hours:** Duration for which Kafka retains log segments before deleting them.
**zookeeper.connect:** Connection string for the ZooKeeper ensemble used by Kafka for cluster coordination (deprecated since Kafka 2.8, replaced by bootstrap.servers for brokers).
**listeners:** Comma-separated list of URIs the broker will listen on, specified in the form protocol://host:port.
**log.segment.bytes:** Maximum size of a log segment file on disk.
**log.retention.check.interval.ms:** Interval at which Kafka checks log retention policies and deletes expired segments.
**socket.send.buffer.bytes:** Socket send buffer size.
**socket.receive.buffer.bytes:** Socket receive buffer size.
**num.recovery.threads.per.data.dir:** Number of threads per data directory to be used for log recovery at startup.
**group.min.session.timeout.ms:** Minimum allowed session timeout for consumer groups.
**auto.create.topics.enable:** Whether automatic topic creation is allowed.
**compression.type:** Compression codec to use for messages on the broker (none, gzip, snappy, lz4, zstd).


### Cluster Configuration Parameters:
**zookeeper.connect:** ZooKeeper connection string listing the addresses of the ZooKeeper servers.
**group.initial.rebalance.delay.ms:** Delay before the initial consumer group rebalance occurs after a new consumer joins the group.
**min.insync.replicas:** Minimum number of in-sync replicas required for a partition to be considered writable.
**unclean.leader.election.enable:** Whether unclean leader election is allowed, i.e., allowing out-of-sync replicas to become leaders if no in-sync replicas are available.
**offsets.topic.num.partitions:** Number of partitions for the internal Kafka topic used to store consumer group offsets.
**offsets.topic.segment.bytes:** Maximum size of a segment file for the offsets topic.
**transaction.state.log.min.isr:** Minimum in-sync replicas required for the transaction state log.
**transaction.state.log.replication.factor:** Replication factor for the transaction state log.
**auto.leader.rebalance.enable:** Whether automatic leader rebalancing is enabled.
**log.flush.interval.messages:** Number of messages that need to be written to a log partition before a flush is initiated.


### Topic Configuration Parameters:
**cleanup.policy:** Policy for log compaction and deletion (delete, compact, compact,delete).
**retention.ms:** Duration for which Kafka retains log segments for the topic.
**segment.ms:** Interval at which Kafka creates a new log segment for the topic.
**max.message.bytes:** Maximum size of a message that can be written to the topic.
**min.insync.replicas:** Minimum number of in-sync replicas required for a partition to be considered writable.
**retention.bytes:** Maximum size of the log segment files for the topic before old log segments are deleted.
**message.format.version:** Message format version for the topic.
**preallocate:** Whether to preallocate files for new segments of the topic log.


