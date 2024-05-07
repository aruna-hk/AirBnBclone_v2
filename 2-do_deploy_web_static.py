#!/usr/bin/python3
""" deploy arhchive to the servers"""
from os import path
from fabric.api import env, run, put
env.hosts = ['54.173.110.95', '34.207.156.58']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ deploy arhhcive file to servers /tmp"""

    if path.exists(archive_path) is False:
        return False

    if (put(archive_path, "/tmp").failed):
        return False
    else:
        version = archive_path.split('/')[-1].split(".")[0]
        f_loc = '/tmp/' + version + '.tgz'
        f_dest = '/data/web_static/releases/{}/'.format(version)
        if (run("mkdir -p {}".format(f_dest)).failed):
            return False
        run("tar -xzf {} -C {}".format(f_loc, f_dest))
        run("rm {}".format(f_loc))
        run("mv {}web_static/* {}".format(f_dest, f_dest))
        run("rm -rf {}web_static".format(f_dest))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_dest))
        print("New version deployed!")
    return True
