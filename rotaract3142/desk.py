# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rotaract3142"
app_title = "Rotaract 3142"
app_publisher = "Neil Lasrado"
app_description = "Pranali Customizations for District 3142"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "neil@rotarctsuncity.in"
app_license = "MIT"

import frappe
from frappe import _

@frappe.whitelist()
def desktop_icons():
	icons = [
			{
				"category": "Administration",
				"label": _('AARA Nomination'),
				"icon": "octicon octicon-gift",
				"type": 'doctype',
				"name": 'AARA Nomination',
				"link": '#List/AARA Nomination/List'
			}
		]
	return icons