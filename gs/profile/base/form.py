# -*- coding: utf-8 -*-
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
