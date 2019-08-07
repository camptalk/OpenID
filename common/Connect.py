import pymysql
from common.Riko import Riko, DictModel, ObjectModel, INSERT

"""
@module  : Connect.py
@author  : Rinne
@contact : yejunbin123@qq.com
@time    : 2019/08/03
"""


class user_information(DictModel):
    pk = ["uid"]
    fields = ["phone", "email", "username", "pwd", "appid", "clientId", "timestamp", "login_channel", "extra_payload",
              "user_payload"]


class login_information(DictModel):
    pk = ["id"]
    fields = ["uid", "username", "phone", "email", "login_success", "token", "request_id", "appid", "clientId",
              "timestamp", "login_channel", "user_ip", "remote_ip", "extra_payload", "user_payload"]


class DataBaseControl:

    @staticmethod
    def get_user_information_by_email(email):
        return user_information.get_one(email=email)

    @staticmethod
    def get_user_information_by_phone(phone):
        return user_information.get_one(phone=phone)

    @staticmethod
    def get_user_information_by_username(username):
        return user_information.get_one(username=username)

    @staticmethod
    def login_operating_information_update(**kwargs):
        login_information.new(**kwargs).insert()

    @staticmethod
    def sign_in_information(**kwargs):
        try:
            user_information.new(**kwargs).insert()
        except Exception as ex:
            print(ex)

    @staticmethod
    def update_information(uid, info_dict):
        new_info = user_information.get_one(uid=uid)
        for k, v in info_dict.items():
            new_info[k] = v
        new_info.update()


if __name__ == "__main__":
    Riko.db_config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "passwd": "123456",
        "db": "camptalk",
        "charset": "utf8",
        "autocommit": True,
        'cursorclass': pymysql.cursors.DictCursor
    }