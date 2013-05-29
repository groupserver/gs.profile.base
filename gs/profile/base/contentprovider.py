# -*- coding: utf-8 -*-
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
