#!/usr/bin/python3
"""pack web pages for deployment"""
from fabric.api import env, run, put, local
from datetime import datetime
from os import mkdir, path
env.user = 'ubuntu'


def do_pack():
    """ function to pack web pages for deployment"""

    now = datetime.utcnow().strftime("%Y%d%m%H%M%S")
    file = "web_static_" + str(now) + ".tgz"
    print("Packing web_static to {}".format(file))

    if path.exists("versions") and path.isdir("versions"):
        if (local("tar -cvzf versions/{} {}".format(file, "web_static"))):
            return file
    else:
        try:
            mkdir("versions")
            if (local("tar -cvzf versions/{} {}".format(file, "web_static"))):
                return file
        except Exception as e:
            return None
    return None


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


def deploy():
    """ full deployment create archive and deploy to servers"""

    file_path = do_pack()
    if file_path is None:
        return False
    env.hosts = ['54.173.110.95', '34.207.156.58']
    for host in env.hosts:
        env.host_string = host
        if not do_deploy(file_path):
            return False
    return True
