[Unit]
Description=My Test Service
after=multi-user.target

[Service]
User=ubuntu
Type=simple
Restart=always
ExecStart=sudo /usr/bin/python3 /home/ubuntu/wechatDev/main.py 80

[Install]
WantedBy=multi-user.target