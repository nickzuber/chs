from distutils.core import setup

name = 'chs'

setup(
  name = name,
  packages = ['chs'],
  version = '1.0',
  license='MIT',
  description = 'Play chess against the Stockfish engine in your terminal.',
  author = 'Nick Zuber',
  author_email = 'zuber.nicholas@gmail.com',
  url = 'https://github.com/nickzuber/chs',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['chess', 'terminal', 'stockfish'],
  install_requires=[
    'python-chess',
    'editdistance',
  ],
  entry_points={
    'console_scripts': ['{} = chs.__main__:run'.format(name)],
  }
)
