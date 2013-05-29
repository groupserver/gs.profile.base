# -*- coding: utf-8 -*-
from contentprovider import ContentProvider


class Viewlet(ContentProvider):
    def __init__(self, user, request, view, manager):
        super(Viewlet, self).__init__(user, request, view)
        self.manager = manager
