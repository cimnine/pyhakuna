from typing import Optional
from urllib.parse import urljoin

import requests

from pyhakuna.hakuna.auth import HakunaAuth


class Request:
  def __init__(self, instance_name: str, api_token: str):
    self.instance_name = instance_name
    self._auth = HakunaAuth(api_token)

  def _url(self, path: str):
    return urljoin(f"https://{self.instance_name}.hakuna.ch/", path)

  def get(self, path: str, params: Optional[dict]):
    return requests.get(self._url(path), params=params, auth=self._auth).json()

  def post(self, path: str, data: dict):
    return requests.post(self._url(path), data, auth=self._auth).json()

  def put(self, path: str, data: dict):
    return requests.put(self._url(path), data, auth=self._auth).json()

  def patch(self, path: str, data: dict):
    return requests.patch(self._url(path), data, auth=self._auth).json()

  def delete(self, path: str):
    return requests.delete(self._url(path), auth=self._auth)
