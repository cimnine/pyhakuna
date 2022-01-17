from pyhakuna.hakuna.global_ import Global
from pyhakuna.hakuna.personal import Personal
from pyhakuna.hakuna.request import Request


class Hakuna:
  def __init__(self, instance_name: str, api_token: str):
    request = Request(instance_name, api_token)
    self._personal = Personal(request)
    self._global = Global(request)

  def personal(self):
    return self._personal

  def global_(self):
    return self._global
