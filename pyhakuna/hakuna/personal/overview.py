from pyhakuna.hakuna.request import Request

OVERVIEW_PATH = "/api/v1/overview"


class Overview:
  def __init__(self, h: Request):
    self._hakuna = h

  def get(self):
    return self._hakuna.get(OVERVIEW_PATH)
