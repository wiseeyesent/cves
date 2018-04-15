# cvesearch
Just gimme the list &amp; I'll do the work for you. None of us are happy about this though.

![uml](https://github.com/wiseeyesent/cves/raw/master/UMLDraft.png)

![architecture](https://github.com/wiseeyesent/cves/raw/master/CVESArchitecture.png)

```bash
[root@josh9580-cvesearch ~]# time cve-save.py >/dev/null

real	0m0.164s
user	0m0.129s
sys	0m0.035s
[root@josh9580-cvesearch ~]# time cve-check.py CVE-2017-0861 >/dev/null

real	0m3.098s
user	0m2.049s
sys	0m0.051s
[root@josh9580-cvesearch ~]# time cve-check.py CVE-2018-1050 >/dev/null

real	0m16.101s
user	0m2.720s
sys	0m0.107s
```

References
----------
- *Notifications*
* * https://access.redhat.com/security/security-updates/#/cve
* * * https://access.redhat.com/security/cve/cve-2018-1327
* * https://usn.ubuntu.com/
* * * https://usn.ubuntu.com/3607-1/
* * http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1327
* * https://nvd.nist.gov/vuln/detail/CVE-2018-1327
- *Documentation*
* * https://www.lucidchart.com/pages/uml-class-diagram
* * https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
* * http://lxml.de/xpathxslt.html
* * http://docs.python-guide.org/en/latest/scenarios/scrape/
* * https://pythonhosted.org/feedparser/index.html 
* * https://docs.python.org/2.7/library/configparser.html
* * https://docs.python.org/2/library/json.html
* * https://martin-thoma.com/configuration-files-in-python/
