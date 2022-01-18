from .hakuna.global_ import Global
from .hakuna.personal import Personal
from .hakuna.organization import Organization
from .hakuna.request import Request


class Hakuna:
  def __init__(self, instance_name: str, api_token: str):
    request = Request(instance_name, api_token)
    self._personal = Personal(request)
    self._global = Global(request)
    self._organization = Organization(request)

  def personal(self):
    return self._personal

  def global_(self):
    return self._global

  def organization(self):
    return self._organization
