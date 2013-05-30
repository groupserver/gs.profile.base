===================
``gs.profile.base``
===================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Base code for GroupServer site members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-05-29
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

The product provides the core code for displaying pages, and parts of pages
to do with profiles. It defines the page_ code, the `content provider`_
abstract base class, and the concrete viewlet_. It also defines a menu_.

Page
====

The ``gs.profile.base.ProfilePage`` is based on the ``SitePage``
[#sitePage]_, but it defines the ``userInfo`` attribute, that returns a
object that implements ``IGSUserInfo`` interface.

Content Provider
================

The ``gs.profile.base.ProfileContentProvider`` is a content provider that
extends the site content provider by providing a ``userInfo`` attribute.

Viewlet
-------

The ``gs.profile.base.ProfileViewlet`` is a subclass of the content
provider.

Menu
====

I (`Michael JasonSmith`_) know little about the menu, other than it
works. Despite having written the code.

This product defines the menu ``user_profile_menu``. To add an item to a
menu use something like the following ZCML::

  <browser:menuItems
    menu="user_profile_menu"
    for="Products.CustomUserFolder.interfaces.ICustomUser">
    <browser:menuItem 
      action="password.html"
      title="Change Password"
      description="Change the password you use to log in"
      order="5"
      permission="zope2.ManageProperties"/>
  </browser:menuItems>

It registers the action (the URL, ``password.html`` above) with the
title. If it looks awfully like a viewlet there is a reason for that.

The menu itself is produced by the content provider
``groupserver.ProfileContextMenu``.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.profile.base/
- Questions and comments to http://groupserver.org/groups/development/
- Report bugs at https://redmine.iopen.net/projects/groupserver/

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/

.. [#sitePage] See <https://source.iopen.net/groupserver/gs.content.base/>
