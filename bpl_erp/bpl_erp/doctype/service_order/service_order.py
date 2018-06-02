# -*- coding: utf-8 -*-
# Copyright (c) 2018, Jenslaw and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import money_in_words


class ServiceOrder(Document):
	
	def validate(self):
		self.validate_service_order_amount()

	def validate_service_order_amount(self):
		if self.so_items:
			for item in self.so_items:
				item.amount = item.rate * item.number_of_days * item.quantity


	def get_grand_total_amount_in_words(self):
		if self.grand_total:
			return money_in_words(self.grand_total)


	def get_service_agreement(self):
		if self.agreement:
			sa = frappe.get_doc('Service Agreement', self.agreement)
			return sa.as_dict()

