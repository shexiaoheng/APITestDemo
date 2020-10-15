import pytest
from jsonpath import jsonpath

from page.base_api import BaseAPI
from page.tag_manage import TagManage


class TestTagManage:

    @classmethod
    def setup_class(cls):
        cls.tagM = TagManage()

    data = BaseAPI.load('../data/data_tag.yml')

    @pytest.mark.parametrize('group_name,add_name,update_name', data)
    def test_multi_tag(self, group_name, add_name, update_name):
        # query tags
        tags = self.tagM.get_tags()

        # remove already exists data
        for name in [add_name, update_name]:
            tag_id = jsonpath(tags, f'$..tag[?(@.name=="{name}")].id')
            if tag_id:
                self.tagM.delete_tag(tag_id[0])

        # add tag
        res_add = self.tagM.add_tag(group_name, add_name)
        assert res_add['errcode'] == 0
        new_tag_id = jsonpath(res_add, '$..id')

        # update
        res_update = self.tagM.update_tag(new_tag_id[0], update_name)
        assert res_update['errcode'] == 0

    def test_get_tags(self):
        res = self.tagM.get_tags()
        print(self.tagM.format_res(res))

    def test_add_tag(self):
        res = self.tagM.add_tag('TestGroup', 'add1')
        print(self.tagM.format_res(res))

    def test_add_tag_data(self):
        data = {
            'group_name': 'TestGroup',
            'tag_name': 'add2'
        }
        res = self.tagM.add_tag_data(**data)
        print(self.tagM.format_res(res))

    def test_update_tag(self):
        old_tag_name = 'add1'
        new_tag_name = 'update1'
        tag_id = jsonpath(self.tagM.get_tags(), f'$..tag[?(@.name=="{old_tag_name}")].id')[0]
        res = self.tagM.update_tag(tag_id, new_tag_name)
        print(self.tagM.format_res(res))

    def test_update_tag_data(self):
        old_tag_name = 'add2'
        new_tag_name = 'update2'
        tag_id = jsonpath(self.tagM.get_tags(), f'$..tag[?(@.name=="{old_tag_name}")].id')[0]
        data = {
            'tag_id': tag_id,
            'tag_name': new_tag_name
        }
        res = self.tagM.update_tag_data(**data)
        print(self.tagM.format_res(res))

    def test_delete_tag(self):
        target_tag_name = 'update1'
        tag_id = jsonpath(self.tagM.get_tags(), f'$..tag[?(@.name=="{target_tag_name}")].id')[0]
        res = self.tagM.delete_tag(tag_id)
        print(self.tagM.format_res(res))

    def test_delete_tag_data(self):
        target_tag_name = 'update2'
        tag_id = jsonpath(self.tagM.get_tags(), f'$..tag[?(@.name=="{target_tag_name}")].id')[0]
        res = self.tagM.delete_tag_data(tag_id=tag_id)
        print(self.tagM.format_res(res))
