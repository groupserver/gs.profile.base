# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.profile.base',
    version=version,
    description="Base code for profiles on GroupServer.",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='profile groupserver viewlet',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org/',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.profile'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'AccessControl',
        'zope.app.publisher',
        'zope.cachedescriptors',
        'zope.component',
        'zope.contentprovider',
        'zope.interface',
        'zope.pagetemplate',
        'zope.schema',
        'gs.content.base',
        'gs.content.form',
        'gs.viewlet',
        'Products.CustomUserFolder',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
