from page.we_chat_work import WeChatWork


class MemberManage(WeChatWork):
    tagSecret = 'xxx'

    def __init__(self):
        self.token = self.get_token(self.tagSecret)

    def get_department_member(self, department_id):
        req = self.template_sub('../data/r_member_manage.yml', {'token': self.token, 'department_id': department_id},
                                'get_department')

        return self.send_api(req)

    def get_department_member_data(self, **data):
        data.update({'token': self.token})
        req = self.template_sub('../data/r_member_manage.yml', data, 'get_department')
        return self.send_api(req)

    def get_member(self, userid):
        req = self.template_sub('../data/r_member_manage.yml', {'token': self.token, 'userid': userid}, 'get')
        return self.send_api(req)

    def get_member_data(self, **data):
        data.update({'token': self.token})
        req = self.template_sub('../data/r_member_manage.yml', data, 'get')
        return self.send_api(req)

    def add_member(self, userid, name, mobile, department):
        req = self.template_sub('../data/r_member_manage.yml',
                                {'token': self.token, 'userid': userid, 'name': name, 'mobile': mobile,
                                 'department': department}, 'add')
        return self.send_api(req)

    def add_member_data(self, **data):
        data.update({'token': self.token})
        req = self.template_sub('../data/r_member_manage.yml', data, 'add')
        return self.send_api(req)

    def update_member(self, userid, name):
        req = self.template_sub('../data/r_member_manage.yml',
                                {'token': self.token, 'userid': userid, 'name': name}, 'update')
        return self.send_api(req)

    def update_member_data(self, **data):
        data.update({'token': self.token})
        req = self.template_sub('../data/r_member_manage.yml', data, 'update')
        return self.send_api(req)

    def delete_member(self, userid):
        req = self.template_sub('../data/r_member_manage.yml', {'token': self.token, 'userid': userid}, 'delete')
        return self.send_api(req)

    def delete_member_data(self, **data):
        data.update({'token': self.token})
        req = self.template_sub('../data/r_member_manage.yml', data, 'delete')
        return self.send_api(req)
