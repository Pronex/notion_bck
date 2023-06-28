#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
notion_back - backup notion automagically
Author: pronex
"""

import os
import sys

import structlog

from config import initialize_global_config, GLOBAL_CONFIG

_logger = structlog.get_logger()  # logging
initialize_global_config()  # initialize global config

# main
def main():
    pass


# entrypoint for the app
if __name__ == "__main__":
    _logger.info("Starting ...")