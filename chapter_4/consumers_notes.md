## Kafka Consumers

Read data from topics

## Consumers and Consumer groups

You can have many consumers reading data from a same topic. In that scenario, we say they belong to the same consumer group.
Consumers read data from partitions.
For example. If you have a topic that has 4 partitions and only one consumer in consumer group,
then that consumer will read data from all partitions.
If you have two consumers, then partitions are splitted between them. 
Meaning that one consumer will read data from 2 partitions. Now, if we have more consumers than number of partitions (e.g. 5), then
one consumer will be idle. This is important, so we should consider the number of partitions important when creating the topics. It's a good idea to have
a reasonable number, in case we want to scale the consumer rate.

We can have multiple consumers subscribing to the same topic. Usually we create a consumer group on an application level. E.g. application that reads a topic and send the values to Ml model. Then we can have a consumer group focused on this.

## Consumer Groups and Partition Rebalance

There are different scenarios when partition needs to be rebalanced for a consumer group.
For example, when a consumer dies, or when a new consumers comes and so on. 

Consumers send heartbeat signals to kafka broker acting as a group coordinator. When the heartbeats stop after a period, the
coordinator knows that the consumer died.

There are two main methods for rebalancing:

### Eager rebalance

In this method, all partitions are revoked, meaning consumers lose their ownership of the partitions, for a short time.
During this short time no messages consumed. Then, after a while, a new reassignet is made for the consumers.

### Cooperative rebalance

Only a subset of the consumers is revoked ownership of their partitions. Then, reassign the missing partitions to the new consumers.
Advantage is that you don't need to stop everything and can still process the messages on the consumers that are still running.

### How consumers are elected?

When we create the consumer group, with its consumer spec, the first consumer to send the JoinGroup method to the group coordinator (broker) will be elected as group leader.
The leader receives the list of all consumers and assigns partitions to them. Then, the leader sends back the list of assigments to the coordinator.
If a consumer dies, the process of rebalancing is triggered again. With exception of the leader, consumers only see the partitions assigned to them (own assignments).




