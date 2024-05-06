#!/usr/bin/env bash
#script to install and setup nginx
apt update -y
apt install nginx -y

#setup root directory
mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
#fake content
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

rm -rf /data/web_static/current
#nginx setup
echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;
	add_header X-Served-By \$hostname;	
        location /hbnb_static/ {
                alias /data/web_static/current/;
        }

}
" > /etc/nginx/sites-available/default

ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data
service nginx restart
