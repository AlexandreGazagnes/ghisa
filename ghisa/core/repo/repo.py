class Repo:
    """ """

    def __init__(self, url) -> None:
        """Constructor of the class"""

        self.repo_url = ""
        self.repo_name = ""
        self.profile = ""
        self.branch = ""

        self.imports_list = []
        self.import_dict = {}

        # self.repo_list_url = ""
        # self.repo_list = []
        # self.repo = None

        self.branch = ""

    def _manage_repo(self):
        """ """

        pass

    def _clone_repo(self):
        """ """

        pass

    def _count_imports(self):
        """ """

        pass

    def as_dict(self):
        return self.__dict__
