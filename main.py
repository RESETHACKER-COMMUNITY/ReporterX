#!/usr/bin/env python3

# Author : HACKE-RC commonly known as RC;
# Description : ReporterX by RC - Template based report writing tool.
# Developer contact: @coder_rc on twitter. You can request new feature by tagging me on any of your tweet.

import yaml
import argparse
import os
import sys
from jinja2 import Environment, FileSystemLoader
import requests
import html


def update():
    os.system("git checkout . && git pull && chmod +x *")

def checkupdate():
    current_version = open(f".version").read()
    version = requests.get("https://raw.githubusercontent.com/RESETHACKER-COMMUNITY/ReporterX/main/.version").text
    if current_version != version:
        print("An update is available.")
        que = input("Do you want to update the tool now? (y/n) : ")
        if que.startswith("y"):
            update()
        else:
            pass


try:
    checkupdate()
except:
    pass


try:
    requests.get("https://resethacker.com/")
    checkupdate()
except:
    pass

if not os.path.isdir(".temp"):
    os.mkdir(".temp")
else:
    try:
        os.remove(".temp/something.yaml")
    except:
        pass


class ReporterX:
    required = {
        "URL": False,
        "param": False,
        "reporter_username": False,
        "steps": False,
        "impact": False,
        "remediation": False,
        "org_name": False
    }

    main_dict = {
        "host": None,
        "param": None,
        "reporter_username": None,
        "org_name": None,
        "steps": None,
        "impact": None,
        "remediation": None
    }

    def __init__(self, file_name):
        self.filename = file_name
        try:
            self.file = open(file_name).read()
        except:
            pass

    @staticmethod
    def banner():
        print(r'''
 ____                       _          __  __
|  _ \ ___ _ __   ___  _ __| |_ ___ _ _\ \/ /
| |_) / _ \ '_ \ / _ \| '__| __/ _ \ '__\  /
|  _ <  __/ |_) | (_) | |  | ||  __/ |  /  \
|_| \_\___| .__/ \___/|_|   \__\___|_| /_/\_\
          |_|
''')
        print("\t\t\t\tv1.0 beta")
        print("------------ ReporterX by RC ------------")
        print("----- github.com/resetdeveloper/ReporterX -----")

    @staticmethod
    def showargs(missing: int):
        if missing:
            print("")
            print("Required arguments:")
            print("\t-t Template path\tPath of the template you want to use.")
        print("\nOther arguments will be shown according to the template you choose.")
        exit()

    @staticmethod
    def isfile(file_name: str):
        try:
            open(file_name).close()
        except FileNotFoundError:
            print(f"FileNotFound: Unable to open {file_name}. error the file you specified doesn\'t exits!")
            exit(-1)
        except KeyboardInterrupt:
            print("[Q] Quiting... [Q]")
            exit(0)

    @staticmethod
    def updatesteps(template: dict):
        template["report"]["steps"] = open(args.steps).read()
        return template

    @staticmethod
    def updateimpact(template: dict):
        template["report"]["impact"] = open(args.impact).read()
        return template

    @staticmethod
    def updateremediation(template: dict):
        template["report"]["remediation"] = open(args.remediation).read()
        return template


def updatetemplate(file_name: str):
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    env = Environment(loader=FileSystemLoader(DIR_PATH))
    template = env.get_template(file_name)
    c = template.render(host=args.url, param=html.escape(args.param), username=args.username.replace("@", ""), steps=args.steps,
                        impact=args.impact, remediation=args.remediation)
    return yaml.safe_load(c)


try:
    checkvariable = sys.argv[sys.argv[:].index("-t") + 1]
except:
    ReporterX.banner()
    ReporterX.showargs(1)

filename = sys.argv[sys.argv[:].index("-t") + 1]
ReporterX.isfile(filename)
template = ReporterX(filename)
template = yaml.safe_load(open(filename))

parser = argparse.ArgumentParser(description='Template based report generator tool.')

if "url" in template['info']['required']:
    ReporterX.required["url"] = True
    parser.add_argument("-u", "--url", type=str,
                        metavar="URL", help="URL where vulnerability exits(with path)",
                        required=True)

if 'param' in template['info']['required']:
    ReporterX.required["param"] = True
    parser.add_argument("-p", "--param", type=str,
                        metavar="Parameter", help="Parameter to append with the URL(with value).",
                        required=True, default=None)

if 'org_name' in template['info']['required']:
    ReporterX.required["org_name"] = True
    parser.add_argument("-on", "--orgname", type=str,
                        metavar="Company name", help="Name of the affected organisation/company.",
                        required=True)

if 'reporter_username' in template['info']['required']:
    ReporterX.required["reporter_username"] = True
    parser.add_argument("-user", "--username", type=str,
                        metavar="Reporter username", help="Username of the reporter(e.g. @coder_rc).",
                        required=True)

if 'steps' in template['info']['required']:
    ReporterX.required["steps"] = True
    parser.add_argument("-s", "--steps", type=str,
                        metavar="Custom Steps to reproduce", help="File path to read steps to reproduce from.",
                        required=False, default=False)

if 'impact' in template['info']['required']:
    ReporterX.required["impact"] = True
    parser.add_argument("-imp", "--impact", type=str,
                        metavar="Custom impact", help="File path to read impact from.",
                        required=False, default=False)

if "remediation" in template['info']['required']:
    ReporterX.required["remediation"] = True
    parser.add_argument("-rem", "--remediation", type=str,
                        metavar="Custom remediation", help="File path to remediation from.",
                        required=False, default=False)

parser.add_argument("-t", metavar="Template path", type=str,
                    help='Path of template you want to use.', required=False)

parser.add_argument("--silent", action="store_true", help="Don\'t print anything just silently save results.")

parser.add_argument("-o", '--output', type=str, metavar="", help="Filename to save results in.", default="report.txt")

args = parser.parse_args()

if not ReporterX.required["param"]:
    args.param = None  # To ignore future errors

if not ReporterX.required["url"]:
    args.url = None  # To ignore future errors

if not ReporterX.required["org_name"]:
    args.orgname = None  # To ignore future errors

if not ReporterX.required["org_name"]:
    args.orgname = None  # To ignore future errors

if not ReporterX.required["steps"]:
    args.steps = None  # To ignore future errors

if not ReporterX.required["remediation"]:
    args.remediation = None  # To ignore future errors

if args.steps:
    ReporterX.isfile(args.steps)
    _template = template
    template = ReporterX.updatesteps(_template)

if args.impact:
    ReporterX.isfile(args.impact)
    template = ReporterX.updateimpact(_template)

if args.remediation:
    ReporterX.isfile(args.remediation)
    template = ReporterX.updateremediation(_template)

with open(".temp/something.yaml", "w") as f:
    yaml.dump(template, f)

template = updatetemplate(".temp/something.yaml")

if not args.silent:
    print(f"[INF] Using {template['id']} by {template['info']['author']} [INF]\n")
    print(f"Vulnerability name : {template['info']['name']}")
    print(f"Severity : {template['info']['severity']}")
    print(f"Language : {template['info']['language']}")
    print(f"Category : {template['info']['category']}\n")
    print("-" * 70 + "\n")

# If you're seeing this, follow me on twitter @coder_rc!


def printescape(s):
    print(html.unescape(s))


if not args.silent:
    printescape(template["report"]["summary"] + "\n")

if ReporterX.required["steps"]:
    if not args.silent:
        printescape(template["report"]["steps"] + "\n")

if ReporterX.required["impact"]:
    if not args.silent:
        printescape(template["report"]["impact"] + "\n")

if ReporterX.required["remediation"]:
    if not args.silent:
        printescape(template["report"]["remediation"] + "\n")

if not args.silent:
    printescape(template["report"]["end"] + "\n")

outputfile = open(args.output, "w")
outputfile.write(template["report"]["summary"] + "\n" + "\n")
if ReporterX.required["steps"]:
    outputfile.write(html.unescape(template["report"]["steps"] + "\n" + "\n"))

if ReporterX.required["impact"]:
    outputfile.write(html.unescape(template["report"]["impact"] + "\n" + "\n"))

if ReporterX.required["remediation"]:
    outputfile.write(html.unescape(template["report"]["remediation"] + "\n" + "\n"))

outputfile.write(html.unescape(template["report"]["end"] + "\n" + "\n"))
outputfile.close()

del filename
del outputfile
del template
del args
del parser
del ReporterX.main_dict
del ReporterX.required
