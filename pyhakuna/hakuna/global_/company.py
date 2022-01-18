from pyhakuna.hakuna.request import Request

COMPANY_PATH = "/api/v1/company"


class Company:
  def __init__(self, h: Request):
    self._hakuna = h

  def get(self):
    return self._hakuna.get(COMPANY_PATH)
