# -*- coding: utf-8 -*-
from zope.schema import TextLine
from zope.interface import Interface


class IProfileMenu(Interface):
    pageTemplateFileName = TextLine(title=u"Page Template File Name",
                                description=u'The name of the ZPT file that '
                                    u'is used to render the menu.',
                                required=False,
                                default=u"browser/templates/menu.pt")
