#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
notion_back - backup notion automagically
Author: pronex
"""

import os
import datetime

import json
import requests

import structlog

from config import initialize_global_config, GLOBAL_CONFIG

_logger = structlog.get_logger()  # logging
initialize_global_config()  # initialize global config

# setup requests
headers = {
'Authorization': f'Bearer {GLOBAL_CONFIG.notion_token}',
'Notion-Version': '2022-06-28',
'Content-Type': 'application/json',
}

# setup path
BCK_FOLDER_NAME = "bck_out_"
BCK_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), BCK_FOLDER_NAME)

# main
# following https://notionbackups.com/blog/automated-notion-backup-api
def backup() -> None:
    """
    Run the backup process.
    """
    # setup folder
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    folder = BCK_FOLDER_PATH + timestamp

    os.mkdir(folder)

    # search all pages that can be found
    response = requests.post('https://api.notion.com/v1/search', headers=headers, timeout=10)

    # retrieve block children
    for block in response.json()['results']:
        with open(f'{folder}/{block["id"]}.json', 'w', encoding="utf-8") as file:
            file.write(json.dumps(block))

        child_blocks = requests.get(f'https://api.notion.com/v1/blocks/{block["id"]}/children',
                                    headers=headers, timeout=10)
        if child_blocks.json()['results']:
            os.mkdir(folder + f'/{block["id"]}')

            for child in child_blocks.json()['results']:
                with open(f'{folder}/{block["id"]}/{child["id"]}.json',
                          'w', encoding="utf-8") as file:
                    file.write(json.dumps(child))


# entrypoint for the app
if __name__ == "__main__":
    _logger.info("Starting ...")
    try:
        backup()
    except: # pylint: disable=bare-except
        _logger.error("Backup failed!")
    _logger.info("Finished.")
