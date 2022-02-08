# pyhakuna

![PyPI Version](https://img.shields.io/pypi/v/pyhakuna?style=flat-square)
![PyPI License](https://img.shields.io/pypi/l/pyhakuna?style=flat-square)
![PyPI Status](https://img.shields.io/pypi/status/pyhakuna?style=flat-square)

`pyhakuna` is a client to access the API of the time keeping service [hakuna.ch][hakuna].
[The Hakuna API][hakuna-api] is – unfortunately – personal and currently does not allow to access company-wide data. 

## Requirements

This tool requires [Python 3][python].

## Installation

```bash
pip3 install -U pyhakuna
```

Use the same command to update to a new version.

## Usage

```python
from pyhakuna import Hakuna

h = Hakuna("instance-name", "api-token")
u = h.personal().users().me()
```

The API tries to follow the structure of the [Hakuna API documentation][hakuna-api].

## Development

```bash
python3 -m venv .venv
source .venv/bin/active
python3 -m pip install -U pip setuptools wheel
python3 -m pip install -r requirements.txt
python3 -m pip install -e .
```

## Release

See https://packaging.python.org/tutorials/packaging-projects/.

tl;dr:

```bash
rm -rf dist *.egg-info
python3 -m pip install -U build twine
python3 -m build
python3 -m twine upload dist/*
# Username: __token__
```

## Licensing and Copyright

This code is copyrighted.
But it can be used under the terms of the [MIT license](./LICENSE) for your own purposes.
It builds upon the following third party modules:

- [requests][requests], a simple HTTP client for Python, which is made available under the terms of the [Apache Software License][requests-license].

Open source software rocks 🎸!

[hakuna]: https://hakuna.ch
[hakuna-api]: https://www.hakuna.ch/docs
[python]: https://www.python.org
[requests]: https://docs.python-requests.org/en/latest/
[requests-license]: https://github.com/psf/requests/blob/24dfbfde552bb8ce48eec415714cbe793cfa95bd/LICENSE
