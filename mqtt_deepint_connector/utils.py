#!usr/bin/python

# Copyright 2021 Deep Intelligence
# See LICENSE for details.


from time import sleep
from typing import Dict, List, Any

from mqtt_deepint_connector import DeepintProducer, MQTTConsumer, serve_application_logger


def connect(
        mqtt_broker: str
        , mqtt_port: int
        , mqtt_user: str
        , mqtt_password: str
        , mqtt_topics: List[str]
        , deepint_auth_token: str
        , deepint_organization_id: str
        , deepint_workspace_id: str
        , deepint_source_id: str
        , mqtt_client_id: str = None
        , mqtt_num_message_limit: int = 10
    ):
    """Util function to wrap the usage fo producer and consumer

    Args:
        deepint_auth_token: Authentication token for Deep Intelligence.
        deepint_organization_id: Deep intelligence organization's id, where source is located.
        deepint_workspace_id: Deep intelligence workspace's id, where source is located.
        deepint_source_id: Deep intelligence source's id, where data will be dumped.
        mqtt_broker: MQTT's broker IP.
        mqtt_port: MQTT's broker port.
        mqtt_user: MQTT's broker user.
        mqtt_password: MQTT's broker password.
        mqtt_topics: topics from data comes from.
        mqtt_client_id: MQTT's client id. If not provided, an UUIDv4 will be generated.
        mqtt_num_message_limit: number of messages to store before dumpt to Deep Intelligence. If set to 0 each message is send.
    """

    producer = DeepintProducer(auth_token=deepint_auth_token
            , organization_id=deepint_organization_id
            , workspace_id=deepint_workspace_id
            , source_id=deepint_source_id
        )

    consumer = MQTTConsumer(deepint_producer=producer
            , mqtt_broker=mqtt_broker
            , mqtt_port=mqtt_port
            , mqtt_user=mqtt_user
            , mqtt_password=mqtt_password
            , mqtt_topics=mqtt_topics
            , mqtt_client_id=mqtt_client_id
            , num_message_limit=mqtt_num_message_limit
        )

    failed = True
    while failed:
        try:
            consumer.loop()
            failed = False
        except:
            logger.warning('MQTT connection failed, trying in 5 seconds again ...')
            sleep(5)
            failed = True