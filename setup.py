from setuptools import find_packages, setup

name = 'chs'
version = '1.3'

setup(
  name = name,
  version = version,
  license='MIT',
  description = 'Play chess against the Stockfish engine in your terminal.',
  author = 'Nick Zuber',
  author_email = 'zuber.nicholas@gmail.com',
  include_package_data = True,
  url = 'https://github.com/nickzuber/chs',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['chess', 'terminal', 'stockfish'],
  packages = find_packages(),
  install_requires=[
    'python-chess',
    'editdistance',
  ],
  entry_points={
    'console_scripts': ['{} = chs.__main__:run'.format(name)],
  }
)
