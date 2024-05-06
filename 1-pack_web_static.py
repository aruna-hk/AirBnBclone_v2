#!/usr/bin/python3
"""pack web pages for deployment"""
from datetime import datetime
from fabric.api import local
from os import mkdir, path


def do_pack():
    """ function to pack web pages for deployment"""

    now = datetime.utcnow().strftime("%Y%d%m%H%M%S")
    file = "web_static_" + str(now)
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
