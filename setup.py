# Copyright (c) by it's authors. 
# Some rights reserved. See LICENSE, AUTHORS.

from setuptools import setup, find_packages

setup(name='wallaby-base',
      version='0.1.56',
      url='https://github.com/FreshXOpenSource/wallaby-base',
      author='FreshX GbR',
      author_email='wallaby@freshx.de',
      license='BSD',
      description='Core package for wallaby.',
      long_description=open('README.md').read(),
      package_data={'': ['LICENSE', 'AUTHORS', 'README.md']},
      classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Twisted',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
      ],
      packages=find_packages('.'),
      # dependencies to couchdb and elasticsearch are for test-cases only. 
      install_requires=['wallaby-plugin-couchdb', 'wallaby-plugin-elasticsearch', 'setuptools-git']
  )
