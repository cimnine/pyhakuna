from pyhakuna.hakuna.request import Request

USERS_PATH = "/api/v1/users"


class Users:
  def __init__(self, h: Request):
    self._hakuna = h

  def list(self):
    return self._hakuna.get(USERS_PATH)

  def me(self):
    return self._hakuna.get(f"{USERS_PATH}/me")
