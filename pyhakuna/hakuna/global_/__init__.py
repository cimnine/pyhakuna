from pyhakuna.hakuna.request import Request
from .absence_types import AbsenceTypes
from .company import Company
from .projects import Projects
from .tasks import Tasks


class Global:
  def __init__(self, h: Request):
    self._absence_types = AbsenceTypes(h)
    self._company = Company(h)
    self._projects = Projects(h)
    self._tasks = Tasks(h)

  def absence_types(self):
    return self._absence_types

  def company(self):
    return self._company

  def projects(self):
    return self._projects

  def tasks(self):
    return self._tasks
