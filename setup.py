#!/usr/bin/env python3

try:
    from pip.req import parse_requirements  # pip 9.x
except ImportError:
    from pip._internal.req import parse_requirements  # pip 10.x
from distutils.core import setup

requirements = [str(r.req) for r in parse_requirements('requirements.txt', session=False)]

name = 'chss'
version = 1.0

setup(
  name=name,
  version=version,
  install_requires=requirements,
  console=['./chss.py'],
)
