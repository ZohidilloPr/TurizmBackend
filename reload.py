import os

os.system("sudo systemctl daemon-reload")
os.system("sudo systemctl restart turizm")
os.system("sudo systemctl restart nginx")
os.system("sudo nginx -t")
print("final!")