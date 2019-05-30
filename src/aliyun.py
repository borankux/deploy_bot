import env
from aliyunsdkrds.request.v20140815.CreateAccountRequest import CreateAccountRequest
from aliyunsdkcore.client import AcsClient
from aliyunsdkrds.request.v20140815.CreateDatabaseRequest import CreateDatabaseRequest
from aliyunsdkrds.request.v20140815.GrantAccountPrivilegeRequest import GrantAccountPrivilegeRequest


client = AcsClient(ak=env.get('ALI_AK_ID'), secret=env.get('ALI_AK_SECRET'), region_id='cn-hangzhou')


def create_account(dbi, name, password, description='new_account'):
    request = CreateAccountRequest()
    request.set_accept_format('json')
    request.set_AccountType("Normal")

    request.set_DBInstanceId(dbi)
    request.set_AccountName(name)
    request.set_AccountPassword(password)
    request.set_AccountDescription(description)
    response = client.do_action_with_exception(request)
    return response


def create_db(dbi, name, description='new_db',  charset='utf8mb4'):
    request = CreateDatabaseRequest()
    request.set_accept_format('json')

    request.set_DBName(name)
    request.set_CharacterSetName(charset)
    request.set_DBDescription(description)
    request.set_DBInstanceId(dbi)
    response = client.do_action_with_exception(request)
    return response


def grant_db(dbi, account, db_name, privilege='ReadWrite'):
    request = GrantAccountPrivilegeRequest()
    request.set_accept_format('json')

    request.set_AccountPrivilege(privilege)
    request.set_DBName(db_name)
    request.set_AccountName(account)
    request.set_DBInstanceId(dbi)

    response = client.do_action_with_exception(request)
    return response

