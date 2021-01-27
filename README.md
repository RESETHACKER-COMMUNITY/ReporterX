<h1 align="center">
  <br>
  <a href="https://github.com/HACKE-RC/webdork"><img src="https://beeimg.com/images/f36886119494.png" alt="webdork" width="600" height="300"></a>
  <br>
  ReporterX v1.0 beta
  <br>
</h1>

<p align="center">Report writing made easy.</p>

# ReporterX
Python tool to automate report writing with templates!<br>
Suggestions and issues are welcome because I know codes can never be perfect.

## Compatibility
Check your Python version by typing in
```bash
$ python --version
```
If you get the following
```bash
Python 3.9.0
```
or any version greater than or equal to 3.9, this script has been tested and confirmed to be supported.

## Installation

### For termux
```bash
pkg install git -y 
pkg install python -y 
git clone https://github.com/RESETHACKER-COMMUNITY/ReporterX
cd ReporterX
python termux-setup.py
```

### For Debian-based GNU/Linux distributions
```bash
git clone https://github.com/RESETHACKER-COMMUNITY/ReporterX
cd ReporterX
sudo python3 setup.py
```

## Usage:
***This is a yaml template based tool(like nuclei is, but it makes reports, instead of finding vulns), The arguments depends upon the template you use.***
***You can use ```-h``` after selecting a template.***
#### Here is a example :
```
root@rc# ReporterX -t /root/RepoterX/templates/SQL-inection/SQLI-GET.yaml -h
usage: main.py [-h] -u URL -p Parameter -user Reporter username [-s Custom Steps to reproduce] [-imp Custom impact] [-rem Custom remediation] [-t Template path] [--silent] [-o]

Template based report generator tool.

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL where vulnerability exits(with path)
  -p Parameter, --param Parameter
                        Parameter to append with the URL(with value).
  -user Reporter username, --username Reporter username
                        Username of the reporter(e.g. @coder_rc).
  -s Custom Steps to reproduce, --steps Custom Steps to reproduce
                        File path to read steps to reproduce from.
  -imp Custom impact, --impact Custom impact
                        File path to read impact from.
  -rem Custom remediation, --remediation Custom remediation
                        File path to remediation from.
  -t Template path      Path of template you want to use.
  --silent              Don't print anything just silently save results.
  -o , --output         Filename to save results in.

```

**For every type of template there is a different usage procedure which is guided [here](/templates)**<br>
**For people who wants make templates they can read how to make them [here](/templates)**

## Arguments :
- Template path : -t 
- URL/Domain/Host(with path) : -u, --url
- Specify parameter to use(with payload) : -p, --param
- Specify organisation name : -on, --orgname
- Specify your username to use at the end of the report : -user, --username
- Specify custom Steps/Impact/Remediation to read from file and not from original template : -s, --steps, -imp, --impact, -rem, --remediation
- Directly save the results without printing anything : --silent

# How to use special characters in arguments
**Read [here](/templates#How-to-use-special-characters-in-arguments)**

## Shoutout
- [Rahul RC](https://twitter.com/coder_rc) (myself).
- [ResetHacker](https://github.com/RESETHACKER-COMMUNITY).
- [InfosecMecha](https://twitter.com/InfosecMecha).

**If you like my work consider contacting me on Twitter @coder_rc for donation related information.**

## Demonstrative Video:

- https://www.youtube.com/watch?v=FViMJC40V88

**Made with Python by [RC](https://twitter.com/coder_rc)**
