import json
from datetime import datetime

from api.base_api import BaseAPI
from models.project_model import ProjectModel
from repository.project_repository import ProjectRepository
from transformer.json import JSONTransformer


class ProjectAPI(BaseAPI):

    def __init__(self):
        super().__init__(ProjectRepository(), ProjectModel())

    def add(self, data):
        self.model(**data)
        self.model.validate()
        if self.model.is_valid:
            data['date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.repository.insert(data)
            self.repository.save()
            return JSONTransformer.resultToJSON(self.repository.find_last_inserted(), self.repository.get_headers())
        else:
            return json.dumps(self.model.get_errors())
