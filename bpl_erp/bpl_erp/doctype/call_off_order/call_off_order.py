# -*- coding: utf-8 -*-
# Copyright (c) 2018, Jenslaw and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import money_in_words

class CallOffOrder(Document):
	
	def get_call_off_purchase_order(self):
		po = frappe.get_doc("Purchase Order",self.purchase_order)
		return po.as_dict()


	def get_po_amount_in_words(self):
		if self.purchase_order:
			po = frappe.get_doc("Purchase Order",self.purchase_order)
			return money_in_words(po.total)

	def get_service_agreement(self):
		if self.service_agreement:
			sa = frappe.get_doc('Service Agreement', self.service_agreement)
			return sa.as_dict()

	def validate(self):
		self.collect_po_details()
		

	def collect_po_details(self):
		# frappe.logger().debug(self.po_price_words)
		if self.purchase_order:
			po = frappe.get_doc("Purchase Order",self.purchase_order)
			self.purchase_order_price = po.total
			self.purchase_order_date = po.transaction_date
			self.po_price_words = self.get_po_amount_in_words()
