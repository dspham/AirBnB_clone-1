#!/usr/bin/python3
"""Deploy archive"""

from fabric.api import run, local, put, env
from datetime import datetime
import os

env.hosts = ["35.237.214.104", "34.73.23.247"]
env.user = "ubuntu"

def do_deploy(archive_path):
    """Distributes the archive
    to the web servers"""
    if not os.path.exists(archive_path):
        return False
    print("Working0")
    put(archive_path, "/tmp/")
    print("Working2")
    filename_with_ext = archive_path.split("/")[1]
    filename_wo_ext = filename_with_ext.split(".")[0]
    archive_dest = "/data/web_static/releases/{}".format(filename_wo_ext)
    run("sudo mkdir -p /data/web_static/releases/{}/".format(filename_wo_ext))
    run("sudo tar -xzf /tmp/{} -C {}/".format(filename_with_ext, archive_dest))
    run("sudo rm -rf /tmp/{}".format(filename_with_ext))
    run("sudo mv {}/web_static/* {}".format(archive_dest, archive_dest))
    run("sudo rm -rf {}/web_static".format(archive_dest))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(archive_dest))
    print("WorkingFinal")
    return True




# returns false if path doesn't exist

# upload the archive to the folder /data/web_static_releases/<archive filename without extension> on web server
# delete the archive from the web server
# delete the symbolic link /data/web_static/current from the web server
# create a new symbolic link /data/web_static/current on the web server, linked to the new version of your code
#     /data/web_static/releases/<archive filename without extension>

# all remote commands must be executed on both web servers
#     env.hosts = ['<IP web-01>', 'IP web-02']
#     Returns True if all operations have been done correctly, else False
# Use this script to deploy it on your servers: xx-web-01, xx-web-02
