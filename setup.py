# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import codecs
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()
with codecs.open(os.path.join("docs", "HISTORY.rst"), encoding='utf-8') as f:
    long_description += '\n' + f.read()

setup(name='gs.profile.base',
    version=version,
    description="Base code for profiles on GroupServer.",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Zope Public License',
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='groupserver, viewlet, profile, form, page',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='https://source.iopen.net/groupserver/gs.profile.base/',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.profile'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'AccessControl',
        'zope.app.publisher',
        'zope.browsermenu',
        'zope.cachedescriptors',
        'zope.component',
        'zope.contentprovider',
        'zope.interface',
        'zope.pagetemplate',
        'zope.schema',
        'zope.tal',
        'zope.tales',
        'Zope2',
        'gs.content.base',
        'gs.content.form.base',
        'gs.viewlet',
        'Products.CustomUserFolder',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
