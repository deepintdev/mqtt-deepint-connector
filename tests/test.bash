#!usr/bin/python

# Copyright 2021 Deep Intelligence
# See LICENSE for details.


# Connection data comes from the environment: never commit real hosts, users, passwords or tokens.
MQTT_BROKER="${MQTT_BROKER:?set MQTT_BROKER in the environment}"
MQTT_PORT="${MQTT_PORT:?set MQTT_PORT in the environment}"
MQTT_USER="${MQTT_USER:?set MQTT_USER in the environment}"
MQTT_PASSWORD="${MQTT_PASSWORD:?set MQTT_PASSWORD in the environment}"
MQTT_TOPICS="${MQTT_TOPICS:?set MQTT_TOPICS in the environment}"
DEEPINT_AUTH_TOKEN="${DEEPINT_AUTH_TOKEN:?set DEEPINT_AUTH_TOKEN in the environment}"
DEEPINT_ORGANIZATION_ID="${DEEPINT_ORGANIZATION_ID:?set DEEPINT_ORGANIZATION_ID in the environment}"
DEEPINT_WORKSPACE_ID="${DEEPINT_WORKSPACE_ID:?set DEEPINT_WORKSPACE_ID in the environment}"
DEEPINT_SOURCE_ID="${DEEPINT_SOURCE_ID:?set DEEPINT_SOURCE_ID in the environment}"
MQTT_CLIENT_ID="example-id"
MQTT_NUM_MESSAGE_LIMIT="1"
QUIET_MODE_SET="False"


sudo python3 -m pip install pip --upgrade
sudo python3 -m pip install . --upgrade
sudo mqtt-deepint-connector "${MQTT_BROKER}" "${MQTT_PORT}" "${MQTT_USER}" "${MQTT_PASSWORD}" "${MQTT_TOPICS}" "${DEEPINT_AUTH_TOKEN}" "${DEEPINT_ORGANIZATION_ID}" "${DEEPINT_WORKSPACE_ID}" "${DEEPINT_SOURCE_ID}" "${MQTT_CLIENT_ID}" "${MQTT_NUM_MESSAGE_LIMIT}" "${QUIET_MODE_SET}"
