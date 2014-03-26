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
from __future__ import absolute_import, unicode_literals
from logging import getLogger
log = getLogger('GSProfileContextMenuContentProvider')
from zope.app.publisher.browser.menu import getMenu
from zope.component import createObject
from zope.contentprovider.interfaces import UpdateNotCalled
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from AccessControl.security import newInteraction
from .contentprovider import ContentProvider


class GSProfileContextMenuContentProvider(ContentProvider):
    """GroupServer context-menu for the user profile area."""

    def __init__(self, user, request, view):
        super(GSProfileContextMenuContentProvider, self).__init__(user, request,
                                                                    view)
        self.__updated = False

        newInteraction()

    def update(self):
        self.__updated = True

        self.groupsInfo = createObject('groupserver.GroupsInfo',
          self.context)

        self.pages = getMenu('user_profile_menu', self.user, self.request)

        self.requestBase = self.request.URL.split('/')[-1]
        self.userId = self.context.getId()

    def render(self):
        if not self.__updated:
            raise UpdateNotCalled

        pageTemplate = PageTemplateFile(self.pageTemplateFileName)
        return pageTemplate(view=self)

    #########################################
    # Non standard methods below this point #
    #########################################

    def page_class(self, page):
        if page['selected']:
            retval = 'current'
        else:
            retval = 'not-current'
        assert retval
        return retval
