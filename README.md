## Review

Commandline tool to create gitlab merge requests.
## Setup

```shell
$ pip install reviewer
```

```shell
$ export GITLAB_TOKEN=<token>
```
## Options

  **--name**, Required, create new merge request with title <name>
```shell
review --name=newmr
``` 

  **--ds**, Optional, delete source branch, true or false, defaults to false
```shell
review --name=newmr --ds=true
```

  **--assignee**,  Optional, assign a reviewer, expects the gitlab name of a gitlab user.
```shell
review --name=newmr --assignee=JOHNWICK
```




