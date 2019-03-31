#!/usr/bin/env python
# -*- Coding:utf-8 -*-
import logging

from apis.baseapi import BaseAPI
from initialization.sysconfig import sys_cfg


class DepartManage(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("Init department manage API")
        self.secret_id = sys_cfg.get('contact_para', 'secret_id')
        self.create_deparment_url = sys_cfg.get('contact_para', 'create_department_url')
        self.update_deparment_url = sys_cfg.get('contact_para', 'update_department_url')
        self.my_token = {'access_token':self.get_token(self.secret_id)}


    def creat_department(self):
        new_department={
            "name": "测试开发组",
            "parentid": 1,
            "order": 1,
        }
        self.post_json(self.create_deparment_url, new_department, params=self.my_token)

    def get_create_department_res(self):
        return self.get_response()

    def update_department(self):
        update_deparment={
            "id": 2,
            "name": "测试开发组",
        }
        self.post_json(self.update_deparment_url, update_deparment, params=self.my_token)

    def get_update_department_res(self):
        return self.get_response()