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
