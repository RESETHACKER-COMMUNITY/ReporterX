# A introduction to yaml templates for RepoterX
***This page contains the information about how these templates can be used and how can you make [own templates](#How-to-make-own-templates).***
**Templates can be used according to vulnerability.**

Vulnerability | How to
--- | ---
[Broken link hijacking](https://github.com/RESETHACKER-COMMUNITY/ReporterX/tree/main/templates/Broken-link-hijacking) | Host will be used as the page where the broken link is found.<br> Parameter will be used as the broken link that is found.
[XSS - Relected](https://github.com/RESETHACKER-COMMUNITY/ReporterX/tree/main/templates/Cross-site-scripting/Reflected) | Host will be the url with path of the vulnerable page.<br> Parameter will be the vulnerable parameter with payload.
[No rate-limiting](https://github.com/RESETHACKER-COMMUNITY/ReporterX/tree/main/templates/No-rate-limiting) | Host will be the url with path of the vulnerable page.<br> Parameter can be used as the placeholder for the parameter<br> to select in intruder.
[Open redirects](https://github.com/RESETHACKER-COMMUNITY/ReporterX/tree/main/templates/Open-redirects) | Host will be the url and parameter will be the vulnerable parameter<br> with payload.
[SQLI - GET Based](https://github.com/RESETHACKER-COMMUNITY/ReporterX/tree/main/templates/SQL-inection) | Host will be the url and parameter will be the vulnerable parameter<br> with payload.
[SSRF - GET Based](https://github.com/RESETHACKER-COMMUNITY/ReporterX/tree/main/templates/Server-side-request-forgery) | Host will be the url and parameter will be the vulnerable parameter<br>with payload.


<p>If you create any new vulnerability's template update it in this table.</p>

-----

# How to make own templates
**Here is how can you create own templates :**

The templates are made in yaml, to read more yaml you can read [this](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html).

