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

	def get_po_items(self, update=False):
		if self.purchase_order:
			po = frappe.get_doc("Purchase Order",self.purchase_order)
			if not update:
				return po.items
			self.set("po_items",[])
			for item in po.items:
				d = frappe.new_doc("COO Purchase Order Items")
				d.parent = self.name
				d.parenttype = "Call Off Order"
				d.parentfield = "po_items"
				d.item_code = item.item_code;
				d.qty = item.qty;
				d.uom = item.uom;
				d.unit_price = item.rate;
				d.total_price = item.amount;
				d.part_number = item.supplier_part_no;
				d.description = item.description;
				self.po_items.append(d)



	def validate(self):
		self.collect_po_details()
		self.get_po_items(update=True)
		self.set_signature_placeholder()
		

	def collect_po_details(self):
		if self.purchase_order:
			po = frappe.get_doc("Purchase Order",self.purchase_order)
			self.purchase_order_price = po.total
			self.purchase_order_date = po.transaction_date
			self.po_price_words = self.get_po_amount_in_words()

	def set_signature_placeholder(self):
		for i in self.signatories:
			i.signature = "."
