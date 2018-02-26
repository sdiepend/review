#!/usr/bin/env python
import requests
import fire
import subprocess
import re
import os
import logging

 
def cmr(name, assignee=None, ds=False):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)

    gitlab_token = os.getenv('GITLAB_TOKEN')
    if gitlab_token is None:
        print("No Gitlab private token found in environment variables, please set one and try again")
        return
    subprocess.run(['git', 'branch', name])
    subprocess.run(['git', 'push', 'origin', name])
    headers = {'PRIVATE-TOKEN': gitlab_token}

    # remote_url = subprocess.check_output(['git', 'remote', '-v'])

    output = subprocess.check_output(['git', 'ls-remote', '--get-url', 'origin']).decode("utf-8")
    project_name = re.sub(r'^.+\:(.+)\.git', r'\1', output).strip()
    project_id_url = re.sub(r'/', r'%2F', project_name)
    
    hostname = re.sub(r'^.*[@:](.+\..+)[\:].+', r'\1', output).strip()
    
    logger.info('URL safe project name: ' + project_id_url)
    logger.info('Remote hostname: ' + hostname)
    project_id_int = int(requests.get("http://" + hostname + "/api/v4/projects/" + project_id_url, headers=headers).json()['id'])

    payload = {
            'id': project_id_int,
            'source_branch': name,
            'target_branch': 'master',
            'title': name
            }
    if assignee:
        assignee_id = _get_user_id(assignee, hostname)
        if assignee_id:
            assignee_id_int = int(assignee_id)
        else:
            print("Assignee not found")
            return

    payload['assignee_id'] = assignee_id_int

    if ds:
        payload['remove_source_branch'] = 'true'

    req = requests.post('http://' + hostname + '/api/v4/projects/' + project_id_url + '/merge_requests', headers=headers, data=payload)
    logger.info('Response Status: %d' % (req.status_code))
    response_json = req.json()
    print("Merge request successfully created with name {name}.\n Click here {url}".format(name=response_json['title'], url=response_json['']))


def _get_user_id(assignee, hostname):
    users = _get_users(hostname)
    for user in users:
        if user['name'] == assignee:
            return user['id']
    return None

def _get_users(hostname, url=None):
    gitlab_token = os.getenv('GITLAB_TOKEN')
    headers = {'PRIVATE-TOKEN': gitlab_token}
    if url:
        print("Ja!")
        response = requests.get(url, headers=headers)
    else:
        print("Eerste")
        response = requests.get("http://" + hostname + "/api/v4/users?per_page=80", headers=headers)
    users = response.json()
    if 'next' in response.links:
        print(response.links['next']['url'])
        return users + _get_users(hostname, response.links['next']['url'])
    else:
        return users

if __name__ == "__main__":
    fire.Fire(cmr)
