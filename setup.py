from distutils.core import setup
setup(
  name = 'authgen',
  packages = ['authgen'],
  version = '0.4',
  license='MIT',
  description = 'Random string gen',
  author = 'Zakhar Preobrazhensky',
  author_email = 'cfym.gamer@gmail.com',
  url = 'https://github.com/DemonEclipSe/authgen',
  download_url = 'https://github.com/DemonEclipSe/authgen/tree/master/authgen',
  keywords = ['wrapper', 'api', 'random'],
  install_requires=['aiohttp', 'string', 'random'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
