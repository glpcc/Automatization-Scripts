#!/usr/bin/python3
# Copy github file version in python
import sys
import requests
import os

def create_dir_or_file(git_obj: dict, path = ''):
    if git_obj['type'] == 'dir':
        dir_data = requests.get(git_obj['url']).json()
        new_path = path + '/' + git_obj['name']
        if not os.path.exists(new_path):
            os.mkdir(new_path)   
        for g_obj in dir_data:
            create_dir_or_file(g_obj, new_path)
    elif git_obj['type'] == 'file':
        if path != '':
            file = open(path + '/' + git_obj['name'], 'wb')
        else:
            file = open(git_obj['name'], 'wb')
        file_content = requests.get(git_obj['download_url']).content
        file.write(file_content)
        file.close()

def main():
    num_args: int = len(sys.argv)
    if num_args < 2:
        print('You Have to pass a url to the github file')
    else:
        requested_url: str = sys.argv[1]
        splited_url: list[str] = requested_url.split('/')
        user = splited_url[3]
        repo_name = splited_url[4]
        try:
            path = '/'.join(splited_url[7:])
        except IndexError:
            path = ''
        github_api = f'https://api.github.com/repos/{user}/{repo_name}/contents/{path}'
        # Get the files data from the api
        data = requests.get(github_api).json()
        if type(data) == list:
            print('hola')
            # if data is a list means that the requested url was a folder
            if num_args < 3:
                dirname: str = splited_url[-1]
            else:
                dirname: str = sys.argv[2]
            # create the folder 
            if not os.path.exists(dirname):
                os.mkdir(dirname)
            # Create all subdirectories and subfiles
            for git_obj in data:
                create_dir_or_file(git_obj, dirname)
        elif type(data) == dict:
            create_dir_or_file(data)


if __name__ == '__main__':
    main()