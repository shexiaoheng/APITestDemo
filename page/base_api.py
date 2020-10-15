import json
from string import Template

import requests
import yaml


class BaseAPI:
    def send_api(self, req):
        r = requests.request(**req)
        return r.json()

    @classmethod
    def load(cls, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    @classmethod
    def format_res(cls, res):
        return json.dumps(res, ensure_ascii=False, indent=4)

    @classmethod
    def template_sub(cls, path, data, sub=None):
        with open(path, 'r') as f:
            if sub is None:
                return yaml.safe_load(Template(f.read()).substitute(data))
            else:
                # yaml.safe_load(f)[sub] -> <class 'dict'>
                # yaml.dump(yaml.safe_load(f)[sub]) -> <class 'str'>
                return yaml.safe_load(Template(yaml.dump(yaml.safe_load(f)[sub])).substitute(data))
