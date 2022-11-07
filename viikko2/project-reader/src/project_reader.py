from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_toml = toml.loads(content)

        name = parsed_toml['tool']['poetry']['name']
        description = parsed_toml['tool']['poetry']['description']
        dependencies = [key for key, item in parsed_toml['tool']['poetry']['dependencies'].items()]
        devdependencies = [key for key, item in parsed_toml['tool']['poetry']['dev-dependencies'].items()]

        return Project(name, description, dependencies, devdependencies)
