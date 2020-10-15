import pytest

from page.base_api import BaseAPI
from page.member_manage import MemberManage


class TestMemberManage:

    @classmethod
    def setup_class(cls):
        cls.memberM = MemberManage()

    data_get = BaseAPI.load('../data/data_member_get.yml')
    data_add = BaseAPI.load('../data/data_member_add.yml')
    data_update = BaseAPI.load('../data/data_member_update.yml')

    def test_get_department_member(self):
        department_id = [1]
        res_get = self.memberM.get_department_member(department_id)
        print(self.memberM.format_res(res_get))

    @pytest.mark.parametrize('user', data_get)
    def test_get_member(self, user):
        res_get = self.memberM.get_member_data(**user)
        print(self.memberM.format_res(res_get))

    @pytest.mark.parametrize('user', data_add)
    def test_add_member_data(self, user):
        res_add = self.memberM.add_member_data(**user)
        print(self.memberM.format_res(res_add))

    @pytest.mark.parametrize('user', data_update)
    def test_update_member_data(self, user):
        res_update = self.memberM.update_member(**user)
        print(self.memberM.format_res(res_update))

    @pytest.mark.parametrize('user', data_get)
    def test_delete_member(self, user):
        res_delete = self.memberM.delete_member(**user)
        print(self.memberM.format_res(res_delete))
