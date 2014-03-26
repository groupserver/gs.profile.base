# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2012, 2013, 2014 OnlineGroups.net and Contributors.
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
from zope.cachedescriptors.property import Lazy
from Products.CustomUserFolder.interfaces import IGSUserInfo
from gs.viewlet import SiteContentProvider


class ContentProvider(SiteContentProvider):
    def __init__(self, user, request, view):
        super(ContentProvider, self).__init__(user, request, view)
        self.user = user

    @Lazy
    def userInfo(self):
        retval = IGSUserInfo(self.user)
        return retval
