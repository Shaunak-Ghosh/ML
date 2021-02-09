Cloning into '.'...
Warning: Permanently added the RSA host key for IP address '140.82.112.4' to the list of known hosts.
Reset branch 'master'
Your branch is up-to-date with 'origin/master'.
Dockerfile not found at ./Dockerfile

Cloning into '.'...
Warning: Permanently added the RSA host key for IP address '140.82.112.4' to the list of known hosts.
Reset branch 'master'
Your branch is up-to-date with 'origin/master'.
Dockerfile not found at ./Dockerfile

Cloning into '.'...
Warning: Permanently added the RSA host key for IP address '140.82.113.4' to the list of known hosts.
Switched to a new branch 'Dockerfile'
KernelVersion: 4.4.0-1060-aws
Components: [{u'Version': u'19.03.8', u'Name': u'Engine', u'Details': {u'KernelVersion': u'4.4.0-1060-aws', u'Os': u'linux', u'BuildTime': u'2020-03-11T01:24:30.000000000+00:00', u'ApiVersion': u'1.40', u'MinAPIVersion': u'1.12', u'GitCommit': u'afacb8b7f0', u'Arch': u'amd64', u'Experimental': u'false', u'GoVersion': u'go1.12.17'}}, {u'Version': u'1.2.13', u'Name': u'containerd', u'Details': {u'GitCommit': u'7ad184331fa3e55e52b890ea95e65ba581ae3429'}}, {u'Version': u'1.0.0-rc10', u'Name': u'runc', u'Details': {u'GitCommit': u'dc9208a3303feef5b3839f4323d9beb36df0a9dd'}}, {u'Version': u'0.18.0', u'Name': u'docker-init', u'Details': {u'GitCommit': u'fec3683'}}]
Arch: amd64
BuildTime: 2020-03-11T01:24:30.000000000+00:00
ApiVersion: 1.40
Platform: {u'Name': u'Docker Engine - Community'}
Version: 19.03.8
MinAPIVersion: 1.12
GitCommit: afacb8b7f0
Os: linux
GoVersion: go1.12.17
Starting build of index.docker.io/shaunakghosh123/machine-learning:this...
Unexpected error
Encountered error: 400 Client Error: Bad Request ("failed to parse Dockerfile: file with no instructions.")
Traceback (most recent call last):
File "/stage/builder/runner.py", line 297, in _run
self.build()
File "/stage/builder/runner.py", line 221, in build
self._build()
File "/stage/builder/runner.py", line 209, in _build
cache_repo)
File "/stage/builder/build.py", line 43, in build_image
for line in stream:
File "/usr/local/lib/python2.7/dist-packages/docker/api/client.py", line 305, in _stream_helper
yield self._result(response, json=decode)
File "/usr/local/lib/python2.7/dist-packages/docker/api/client.py", line 220, in _result
self._raise_for_status(response)
File "/usr/local/lib/python2.7/dist-packages/docker/api/client.py", line 216, in _raise_for_status
raise create_api_error_from_http_exception(e)
File "/usr/local/lib/python2.7/dist-packages/docker/errors.py", line 30, in create_api_error_from_http_exception
raise cls(e, response=response, explanation=explanation)
APIError: 400 Client Error: Bad Request ("failed to parse Dockerfile: file with no instructions.")

# INSTRUCTIONS FOR BUILD (PENDING)
Git clone
git status
run with exit 0
require Dockerfile

exit status 1

build failed
