### Custom made deploy tool
	You can define the site schema via yml format. 
### Steps:
	- Resolves domain in Aliyun, 
	- creates rds account and currosponding database, grants WR privilege.
	- Pulls code to specific directory, installs the required packages.
	- Creates nginx config files for persite
	- restarts the nginx server
	- Informs to the DingDing robot.

#### 安装

Clone the project, cd in to the folder, then run:

```shell
 make install
```

### Useage

```
 easy_deploy.py --schema ./schema.yml --step pull --scilence
```
### todo
- Alot


### Schema format
```yml
version: 0.1
base: /var/www/public_html/
title: easy_deploy_test_project
name: easy_deploy
password: '#$gWgsgwng90q93@#FWEgqt13G@Q'
domain: example.com
host: 127.0.0.1
sites:
  - name: front
    repo: git@github.com:borankux/front_end.git
    type: vue

  - name: backend
    repo: git@github.com:borankux/back_end.git
    type: laravel

  - name: official
    repo: git@github.com:borankux/official.git
    type: golang
 ```
