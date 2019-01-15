#!/usr/bin/python3
"""Compress before sending"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder"""
    time_created = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(
             time_created))
        return "versions/web_static_{}.tgz".format(time_created)
    except Exception:
        return None
