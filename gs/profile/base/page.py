# coding=utf-8
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from gs.content.base.page import SitePage
from Products.CustomUserFolder.interfaces import IGSUserInfo

class ProfilePage(SitePage):
    def __init__(self, user, request):
        SitePage.__init__(self, user, request)
        self.user = user

    @Lazy
    def userInfo(self):
      retval = IGSUserInfo(self.user)
      assert retval
      assert not(retval.anonymous)
      return retval
