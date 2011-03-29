# coding=utf-8
from zope.component import createObject
from AccessControl import getSecurityManager
from Products.CustomUserFolder.interfaces import IGSUserInfo

class ProfileContentProvider(object):
    def __init__(self, group, request, view):
        self.__parent__ = self.view = view
        self.__updated = False

        self.context = self.user = group
        self.request = request

        self.__siteInfo = None
        self.__userInfo = None

    @property
    def siteInfo(self):
        if self.__siteInfo == None:
            self.__siteInfo = \
                createObject('groupserver.SiteInfo', self.context)
        return self.__siteInfo
        
    @property
    def userInfo(self):
        if self.__userInfo == None:
            self.__userInfo = IGSUserInfo(self.user)
        return self.__userInfo

