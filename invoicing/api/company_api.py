import random

from api.base_api import BaseAPI
from models.company_model import CompanyModel
from repository.company_repository import CompanyRepository


class CompanyAPI(BaseAPI):

    def __init__(self):
        super().__init__(CompanyRepository(), CompanyModel())


if __name__ == '__main__':
    api = CompanyAPI()
    print(api.show_all())
    print(api.show_by_id(1))
    names = ['A. Corp', 'Widget Co.', 'Name Ltd.', 'Someone & Sons']
    print(api.update_by_id(1, '{"name": "%s"}' % random.choice(names)))
    print(api.add('{"name": "%s", "address": "A Street"}' % random.choice(names)))
    print(api.add('{"name": 1, "address": 2}'))
    print(api.add('{"name": "%s", "address": 2}' % random.choice(names)))
    print(api.add('{"name": "%s"}' % random.choice(names)))
    last = api.repository.find_last_inserted()
    print(api.delete(last['id']))
