from pyhakuna.hakuna.request import Request

ORGANIZATION_PATH = "/api/v1/organization"


class Organization:
  def __init__(self, h: Request):
    self._hakuna = h

  def status(self):
    return self._hakuna.get(f"{ORGANIZATION_PATH}/status")
