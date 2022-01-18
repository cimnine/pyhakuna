from pyhakuna.hakuna.request import Request

TASKS_PATH = "/api/v1/tasks"


class Tasks:
  def __init__(self, h: Request):
    self._hakuna = h

  def list(self):
    return self._hakuna.get(TASKS_PATH)
