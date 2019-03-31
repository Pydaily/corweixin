#!/usr/bin/env python
# -*- Coding:utf-8 -*-
from apis.contact.department.departmanage import DepartManage


class TestUpdateDepartment:

    def test_update_department(self):
        department = DepartManage()
        department.update_department()
        update_res = department.get_update_department_res()
        assert update_res.get('errmsg') == 'updated'