#!/usr/bin/python3
"""Deploy archive"""

from fabric.api import run, local, put, env
from datetime import datetime
import os

env.hosts = ["35.237.214.104", "34.73.23.247"]

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

def deploy():
    """Fully creates and distributes an archive to
    the web servers"""
    archive = do_pack()
    if archive:
        return do_deploy(archive)
    return False
