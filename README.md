## Review

Commandline tool to create gitlab merge requests.

## Options

  --name, Required, create new merge request with title <name>
```shell
review.py --name=newmr
``` 

  --ds, Optional, delete source branch, true or false, defaults to false
```shell
review.py --name=newmr --ds=true
```

  --assignee,  Optional, assign a reviewer, expects the gitlab name of a gitlab user.
```shell
review.py --name=newmr --assignee=JOHNWICK
```




