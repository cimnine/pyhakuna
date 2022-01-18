from typing import Optional

from pyhakuna.hakuna.request import Request

TIMER_PATH = "/api/v1/timer"


class Timer:
  def __init__(self, h: Request):
    self._hakuna = h

  def current(self):
    return self._hakuna.get(TIMER_PATH)

  def start(self,
            task_id: int,
            project_id: Optional[str] = None,
            note: Optional[str] = None,
            start_time: Optional[str] = None):
    data = {'task_id': task_id}
    if project_id:
      data['project_id'] = project_id
    if note:
      data['note'] = note
    if start_time:
      data['start_time'] = start_time

    return self._hakuna.post(TIMER_PATH, data)

  def stop(self, end_time: Optional[str]):
    data = {}
    if end_time:
      data['end_time'] = end_time

    return self._hakuna.put(TIMER_PATH, data)

  def cancel(self):
    return self._hakuna.delete(TIMER_PATH)
