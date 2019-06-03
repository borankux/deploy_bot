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