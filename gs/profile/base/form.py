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
from zope.cachedescriptors.property import Lazy
from gs.content.form import SiteForm
from Products.CustomUserFolder.interfaces import IGSUserInfo


class ProfileForm(SiteForm):

    def __init__(self, user, request):
        super(ProfileForm, self).__init__(user, request)
        self.user = user

    @Lazy
    def userInfo(self):
        retval = IGSUserInfo(self.user)
        assert retval
        assert not(retval.anonymous)
        return retval
