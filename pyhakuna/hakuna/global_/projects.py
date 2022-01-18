from pyhakuna.hakuna.request import Request

PROJECTS_PATH = "/api/v1/projects"


class Projects:
  def __init__(self, h: Request):
    self._hakuna = h

  def list(self):
    return self._hakuna.get(PROJECTS_PATH)
