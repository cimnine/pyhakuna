from pyhakuna.hakuna.request import Request

ABSENCE_TYPES_PATH = "/api/v1/projects"


class AbsenceTypes:
  def __init__(self, h: Request):
    self._hakuna = h

  def list(self):
    return self._hakuna.get(ABSENCE_TYPES_PATH)
