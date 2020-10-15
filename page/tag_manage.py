from page.we_chat_work import WeChatWork


class TagManage(WeChatWork):
    tagSecret = 'xxx'

    def __init__(self):
        self.token = self.get_token(self.tagSecret)

    def get_tags(self):
        req = self.template_sub('../data/r_tag_manage.yml', {'token': self.token}, 'get')
        return self.send_api(req)

    def add_tag(self, group_name, tag_name):
        req = self.template_sub('../data/r_tag_manage.yml',
                                {'token': self.token, 'group_name': group_name, 'tag_name': tag_name}, 'add')
        return self.send_api(req)

    def add_tag_data(self, **data):
        data.update({'token': self.token})
        req = self.template_sub('../data/r_tag_manage.yml', data, 'add')
        return self.send_api(req)

    def update_tag(self, tag_id, tag_name):
        req = self.template_sub('../data/r_tag_manage.yml',
                                {'token': self.token, 'tag_id': tag_id, 'tag_name': tag_name}, 'update')
        return self.send_api(req)

    def update_tag_data(self, **data):
        data.update({'token': self.token})
        req = self.template_sub('../data/r_tag_manage.yml', data, 'update')
        return self.send_api(req)

    def delete_tag(self, tag_id):
        req = self.template_sub('../data/r_tag_manage.yml',
                                {'token': self.token, 'tag_id': tag_id}, 'delete')
        return self.send_api(req)

    def delete_tag_data(self, **data):
        data.update({'token': self.token})
        req = self.template_sub('../data/r_tag_manage.yml', data, 'delete')
        return self.send_api(req)
