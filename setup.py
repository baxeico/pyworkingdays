from distutils.core import setup

setup(
    name = 'pyworkingdays',
    version = '0.1',
    packages = ['workingdays'],
    author = 'Augusto Destrero',
    author_email = 'a.destrero@gmail.com',
    description = 'Utility functions to deal with working days in date operations. With builtin localization support.',
    url = 'https://github.com/baxeico/pyworkingdays',
    download_url = 'https://github.com/baxeico/pyworkingdays/archive/0.1.tar.gz',
    install_requires = ['python-dateutil'],
    keywords = ['date', 'business', 'working']
)
