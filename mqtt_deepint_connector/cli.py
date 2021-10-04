#!usr/bin/python

# Copyright 2021 Deep Intelligence
# See LICENSE for details.

import typer
from typing import Dict, List, Any

from mqtt_deepint_connector import connect, serve_application_logger


app = typer.Typer()
logger = serve_application_logger()


@app.command()
def run(
    mqtt_broker: str = typer.Argument(default=None, help="MQTT's broker IP")
    , mqtt_port: int = typer.Argument(default=None, help="MQTT's broker port")
    , mqtt_user: str = typer.Argument(default=None, help="MQTT's broker user")
    , mqtt_password: str = typer.Argument(default=None, help="MQTT's broker password")
    , mqtt_topics: str = typer.Argument(default=None, help="topics from data comes from")
    , deepint_auth_token: str = typer.Argument(default=None, help="Authentication token for Deep Intelligence")
    , deepint_organization_id: str = typer.Argument(default=None, help="Deep intelligence organization's id, where source is located")
    , deepint_workspace_id: str = typer.Argument(default=None, help="Deep intelligence workspace's id, where source is located")
    , deepint_source_id: str = typer.Argument(default=None, help="Deep intelligence source's id, where data will be dumped")
    , mqtt_client_id: str = typer.Argument(default=None, help="MQTT's client id. If not provided, an UUIDv4 will be generated")
    , mqtt_num_message_limit: int = typer.Argument(default=10, help="number of messages to store before dumpt to Deep Intelligence. If set to 0 each message is send")
    , quiet_mode_set: bool = typer.Argument(default=False, help=" if set to true no logging information is provided.")) -> None:
    """While running dumps messages received from MQTT into deepint.
    """

    # check arguments

    if mqtt_broker is None \
        or mqtt_port is None \
        or mqtt_user is None \
        or mqtt_password is None \
        or mqtt_topics is None \
        or deepint_auth_token is None \
        or deepint_organization_id is None \
        or deepint_workspace_id is None \
        or deepint_source_id is None:
        
        print(f'ERROR: Any of mqtt_broker({mqtt_broker}), mqtt_user({mqtt_user}), mqtt_password({mqtt_password}), mqtt_topics({mqtt_topics}), deepint_auth_token({deepint_auth_token}), deepint_organization_id({deepint_organization_id}), deepint_workspace_id({deepint_workspace_id}) or deepint_source_id({deepint_source_id}) not provided.')
        return

    try:
        mqtt_topics = mqtt_topics.split(',')
    except:
        print(f'ERROR: the providen list of topics is empty or has no the correct format: {mqtt_topics}')
        return

    if not mqtt_topics:
        print(f'ERROR: the providen list of topics is empty or has no the correct format: {mqtt_topics}')
        return

    # disable logging if necceary
    if quiet_mode_set:
        logger.disabled = True

    # perform connection
    connect(
        mqtt_broker=mqtt_broker
        , mqtt_port=mqtt_port
        , mqtt_user=mqtt_user
        , mqtt_password=mqtt_password
        , mqtt_topics=mqtt_topics
        , deepint_auth_token=deepint_auth_token
        , deepint_organization_id=deepint_organization_id
        , deepint_workspace_id=deepint_workspace_id
        , deepint_source_id=deepint_source_id
        , mqtt_client_id=mqtt_client_id
        , mqtt_num_message_limit=mqtt_num_message_limit
    )


def run():
    app()
