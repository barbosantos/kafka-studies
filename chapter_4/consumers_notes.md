## Kafka Consumers

Read data from topics

## Consumers and Consumer groups

You can have many consumers reading data from a same topic. In that scenario, we say they belong to the same consumer group.
Consumers read data from partitions.
For example. If you have a topic that has 4 partitions and only one consumer in consumer group,
then that consumer will read data from all partitions.
If you have two consumers, then partitions are divided between them. 
Meaning that one consumer will read data from 2 partitions. Now, if we have more consumers than number of partitions (e.g. 5), then
one consumer will be idle. This is important, so we should consider the number of partitions important when creating the topics. It's a good idea to have
a reasonable number, in case we want to scale the consumer rate.

We can have multiple consumers subscribing to the same topic. Usually we create a consumer group on an application level. E.g. application that reads a topic and send the values to Ml model. Then we can have a consumer group focused on this.

## Consumer Groups and Partition Rebalance

There are different scenarios when partition needs to be rebalanced for a consumer group.
For example, when a consumer dies, or when a new consumers come and so on. 

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

### Static Group Membership

The normal behavior of rebalance is that when a consumer leaves and comes back a new consumer ID is assigned, and probably it will consume different partitions from before.
With static consumer group, the consumer will have a static ID, so that when it comes back it can be reassinged to its older partitions.
Advantage is that no rebalance will be needed. However, we need to make sure that when it comes back it will be able to catch up with the new messages and not lag behind. We also need to have in mind about
timeout, how long should we wait until the consumer comes back? If it takes too long (more than ```session.timeout.ms```) we need to assign the idle partition to another consumer (rebalance).


## Creating a kafka consumer

Similar to producers. But we instead user consumer class. 3 parameters obligatory to its properties:
- broker configuration
- key.deserializer
- value.deserializer

Alternatively, we can send in the group id (name of consumer group)

```python
# TODO: Add example code here later

```

### Poll method

After creating a consumer object, we use the ```Poll()``` method to read messages from the kafka topic. ```Poll()``` return a list of records if any found.
Another important factor had to do with consumer lifetime. As we saw on last sessions, if the consumer stops sending hearbeats to the kafka broker it will be considered dead,
and the partitions it had ownership will be reassigned (rebalance). The method responsible for sending the heartbeats is ```Poll()```. 

The paramater ```max.poll.interval.ms``` is used to configure how long the broker will wait to receive heartbeats from ```Poll()``` before considering the consumer dead.

> **_NOTE:_** There are more specific parameters to deal with consumer life/heartbeats. For example,  ```heartbeat.interval.ms```, which controls how frequently
the Kafka consumer will send a heartbeat to the group coordinator, and
```session.timeout.ms``` which controls how long a consumer can go without sending a heartbeat.

```Poll(0)``` is a method to force Kafka to get the metadata without consuming any records (a rather common hack).

### Thread safety

One thread per consumer. 





