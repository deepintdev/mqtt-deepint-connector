#!usr/bin/python

# Copyright 2021 Deep Intelligence
# See LICENSE for details.

import json
import time
import uuid
import paho.mqtt.client as mqtt
from typing import Dict, List, Any

from mqtt_deepint_connector import DeepintProducer, serve_application_logger


producer = None
message_limit = 10
message_queue = []

logger = serve_application_logger()


class MQTTConsumer:
    """Consumes from a MQTT list of topics.

    Note: uses the global variables producer, message_limit and message_queue to run.

    Attributes:
        client: connection to MQTT broker.

    Args:
        deepint_producer: producer to send data to deepint on message received.
        mqtt_broker: MQTT's broker IP.
        mqtt_port: MQTT's broker port.
        mqtt_user: MQTT's broker user.
        mqtt_password: MQTT's broker password.
        mqtt_topics: topics from data comes from.
        mqtt_client_id: MQTT's client id. If not provided, an UUIDv4 will be generated.
        num_message_limit: number of messages to store before dumpt to Deep Intelligence. If set to 0 each message is send.
    """

    def __init__(self
            , deepint_producer: DeepintProducer
            , mqtt_broker: str
            , mqtt_port: int
            , mqtt_user: str
            , mqtt_password: str
            , mqtt_topics: List[str]
            , mqtt_client_id: str = None
            , num_message_limit: int = 10
        ):

        global producer, message_limit

        # save producer
        producer = deepint_producer
        message_limit = num_message_limit

        # instance client
        logger.info('Connecting to MQTT')
        mqtt_client_id = f'deepint-connector-{str(uuid.uuid4())}' if mqtt_client_id is None else mqtt_client_id
        self.client = mqtt.Client(mqtt_client_id, protocol=mqtt.MQTTv31)
        self.client.username_pw_set(mqtt_user, password=mqtt_password)
        self.client.connect(mqtt_broker, keepalive=60, port=mqtt_port)
        self.client.on_message = self._on_message

        # suscribe to channels
        for t in mqtt_topics:
            self.client.subscribe(t)

    @staticmethod
    def _on_message(client: Any, userdata: str, message: str) -> None:
        """"Consumes messages and dumps it into deepint when real time is set to true.
        """

        global message_queue, message_limit

        # extract data from message
        topic = message.topic
        content = json.loads(message.payload.decode("utf-8"))

        # add message to queue
        message_queue.append(content)

        # dump into deepint if neccesary
        if len(message_queue) >= message_limit:
            producer.produce(data=message_queue)
            message_queue.clear()

    def loop(self) -> None:
        """ Starts the MQTT consumer and produces messages to deepint for undefined time.
        """

        self.client.loop_start()
        self.client.loop()
        
        logger.info('Started consumer')

        # wait into the loop
        while True:
            time.sleep(4)