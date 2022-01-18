from pyhakuna.hakuna.request import Request

ABSENCES_PATH = "/api/v1/absences"


class Absences:
  def __init__(self, h: Request):
    self._hakuna = h

  def list(self, year: int):
    return self._hakuna.get(f"{ABSENCES_PATH}/{year}")
