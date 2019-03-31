#!/usr/bin/env python
# -*- Coding:utf-8 -*-
import logging
import requests
from initialization.sysconfig import sys_cfg


class BaseAPI:

    def __init__(self):
        logging.info("init base api interface")
        self.cop_id=sys_cfg.get('corp_para', 'cop_id')
        self.token_url=sys_cfg.get('corp_para', 'token_url')
        self.res = ''

    def get_token(self,secret_id):  # 获取运行时所需的access_token
        myparams = {
            'corpid': self.cop_id,
            'corpsecret': secret_id
        }
        token_res = requests.get(self.token_url,params=myparams)
        return token_res.json().get('access_token')

    def post_json(self, url, json_obj, params=None):
        if params:
            self.res = requests.post(url, json=json_obj, params=params)
        else:
            self.res = requests.post(url, json=json_obj)

    def get_response(self):
        return self.res.json()