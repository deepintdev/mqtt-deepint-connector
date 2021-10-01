#!usr/bin/python

# Copyright 2021 Deep Intelligence
# See LICENSE for details.


import deepint
import pandas as pd
from typing import Dict, List, Any

from mqtt_deepint_connector import serve_application_logger


logger = serve_application_logger()


class DeepintProducer:
    """Produces to Deep Intelligence the given data, updating a source.

    Attributes:
        conn: connection to a deepint.net source.

    Args:
        auth_token: Authentication token for Deep Intelligence.
        organization_id: Deep intelligence organization's id, where source is located.
        workspace_id: Deep intelligence workspace's id, where source is located.
        source_id: Deep intelligence source's id, where data will be dumped.
    """

    def __init__(self, auth_token: str, organization_id: str, workspace_id: str, source_id: str) -> None:
        logger.info('Authenticating against deepint.net')
        credentials = deepint.Credentials.build(token=auth_token)
        self.conn = deepint.Source.build(credentials=credentials, organization_id=organization_id, workspace_id=workspace_id, source_id=source_id)

    def produce(self, data: List[Dict[str, Any]]) -> None:
        """Produces the given data to Deep Intelligence
        
        Args:
            data: JSON formatted data to dump into Deep Intelligence.
        """

        # create dataframe and send it to deep intelligence
        df = pd.DataFrame(data=json_data)
        self.conn.instances.update(data=df)