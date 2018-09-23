# -*- coding: utf-8 -*-
# Copyright (c) 2018, Neil Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, cint

class NextTickets(Document):
	def validate(self):
		ticket_cost = 200
		if self.workshop_pass:
			ticket_cost = 250
		self.amount = flt(cint(self.qty) * ticket_cost)

	def on_payment_authorized(self, status_changed_to=None):
		self.paid = 1
		self.save(ignore_permissions=True)