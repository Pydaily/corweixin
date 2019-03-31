#!/usr/bin/env python
# -*- Coding:utf-8 -*-
from apis.contact.department.departmanage import DepartManage


class TestCreateDepartment:

    def test_create_new_department(self):
        department_manage = DepartManage()
        department_manage.creat_department()
        create_res = department_manage.get_create_department_res()
        assert create_res.get('errmsg')=='created'