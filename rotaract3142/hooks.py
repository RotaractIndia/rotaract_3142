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

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
#app_include_css = "/assets/rotaract3142/css/rotaract.css"
# app_include_js = "/assets/rotaract3142/js/rotaract3142.js"

# include js, css files in header of web template
app_include_js = [
	"/assets/rotaract3142/js/conf.js"
	
]

web_include_css = [
	"/assets/rotaract3142/css/rotaract.css",
	"/assets/rotaract3142/css/et-line-font/et-line-font.css",
	"/assets/rotaract3142/css/menuzord.css",
	"/assets/rotaract3142/css/owl.css",
	"/assets/rotaract3142/css/style.css"
]
web_include_js = "/assets/rotaract3142/js/rotaractblog.js"

icons = [
	{
		"module": "Club Administration",
		"label": "Pay Dues Online",
		"icon": "octicon octicon-credit-card",
		"link": '/pay'
	}
]

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "rotaract3142.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rotaract3142.install.before_install"
# after_install = "rotaract3142.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rotaract3142.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rotaract3142.tasks.all"
# 	],
# 	"daily": [
# 		"rotaract3142.tasks.daily"
# 	],
# 	"hourly": [
# 		"rotaract3142.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rotaract3142.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rotaract3142.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rotaract3142.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rotaract3142.event.get_events"
# }
