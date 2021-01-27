from os import system

try:
    import jinja2
    import yaml
except:
    system("pip3 install -r requirements.txt")
    system("cp main.py /data/data/com.termux/files/usr/bin/ReporterX && chmod 755 /data/data/com.termux/files/usr/bin/ReporterX")

print("[INF] The tool has been successfully installed! [INF}")
print("Now you can access this tool from anywhere by typing RepoterX.")
print("Start now by typing ReporterX -h")
