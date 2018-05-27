# -*- coding: utf-8 -*-
# Copyright (c) 2018, Jenslaw and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe




def execute():
	print_format_name = "Call Off Order Print Format"
	json_data = r"""[{"fieldname": "print_heading_template", "fieldtype": "Custom HTML", "options": "<div style=\"border:1px solid black;background:#ffcccc;text-align:center;\">\n\t\t<h2 style=\"color:red\">CALL OFF ORDER</h2>\n\t\t<h5>{{doc.name}}</h5>\n\t</div>"}, {"fieldtype": "Section Break", "label": ""}, {"fieldtype": "Column Break"}, {"fieldname": "_custom_html", "label": "Custom HTML", "print_hide": 0, "fieldtype": "HTML", "options": "<div style=\"border:1px solid black;padding:10px;\">\n<table style=\"width:100%;\">\n\t<tr>\n\t\t<td><strong>Purchaser:</strong></td>\n\t\t<td>{{doc.purchaser}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Supplier:</strong></td>\n\t\t<td>{{doc.supplier}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Supplier's Address</strong></td>\n\t\t<td>{{doc.supplier_address}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Service Agreement Number:</strong></td>\n\t\t<td>{{doc.service_agreement}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Service Agreement Title:</strong></td>\n\t\t<td>{{doc.service_agreement_title}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Purchase Order Number:</strong></td>\n\t\t<td>{{doc.purchase_order}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Purchase Order Date:</strong></td>\n\t\t<td>{{doc.purchase_order_date}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Purchaser's Rep:</strong></td>\n\t\t<td>{{doc.purchase_rep}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Purchaser\u2019s Rep Mobile No:</strong></td>\n\t\t<td>{{doc.purchase_rep_mobile_number}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Purchaser\u2019s Rep Email:</strong></td>\n\t\t<td>{{doc.purchase_rep_email}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Supplier\u2019s Rep:</strong></td>\n\t\t<td>{{doc.supplier_rep}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Supplier\u2019s Rep Mobile No:</strong></td>\n\t\t<td>{{doc.supplier_rep_mobile_number}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Supplier\u2019s Rep E-mail:</strong></td>\n\t\t<td>{{doc.supplier_rep_email}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Delivery Date:</strong></td>\n\t\t<td>{{doc.delivery_date}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Delivery Location:</strong></td>\n\t\t<td>{{doc.delivery_location}}</td>\n\t</tr>\n</table>\n</div>\n<style>\n</style>"}, {"fieldtype": "Section Break", "label": ""}, {"fieldtype": "Column Break"}, {"fieldname": "_custom_html", "label": "Custom HTML", "print_hide": 0, "fieldtype": "HTML", "options": "<div style=\"margin-top:10px;\">\n{% for i in doc.agreement_terms %}\n<p>{{i.idx}}. {{i.term}}</p><br>\n{% endfor %}\n</div>"}, {"fieldtype": "Section Break", "label": "Scope Of Supply"}, {"fieldtype": "Column Break"}, {"fieldname": "po_items", "label": "PO Items", "visible_columns": [{"fieldname": "item_code", "print_hide": 0, "print_width": ""}, {"fieldname": "qty", "print_hide": 0, "print_width": ""}, {"fieldname": "uom", "print_hide": 0, "print_width": ""}, {"fieldname": "unit_price", "print_hide": 0, "print_width": ""}, {"fieldname": "total_price", "print_hide": 0, "print_width": ""}, {"fieldname": "part_number", "print_hide": 0, "print_width": ""}, {"fieldname": "description", "print_hide": 0, "print_width": ""}], "print_hide": 0}, {"fieldtype": "Section Break", "label": ""}, {"fieldtype": "Column Break"}, {"fieldname": "purchase_order_price", "label": "Purchase Order Price", "print_hide": 0}, {"fieldname": "po_price_words", "label": "Purchase Order Price In Words", "print_hide": 0}, {"fieldtype": "Section Break", "label": ""}, {"fieldtype": "Column Break"}, {"fieldname": "signatories", "label": "Call Off Order Signatories", "visible_columns": [{"fieldname": "party", "print_hide": 0, "print_width": ""}, {"fieldname": "name1", "print_hide": 0, "print_width": ""}, {"fieldname": "signature", "print_hide": 0, "print_width": ""}, {"fieldname": "title", "print_hide": 0, "print_width": ""}, {"fieldname": "date", "print_hide": 0, "print_width": ""}], "print_hide": 0}, {"fieldtype": "Section Break", "label": "Payment Terms"}, {"fieldtype": "Column Break"}, {"fieldname": "_custom_html", "label": "Custom HTML", "print_hide": 0, "fieldtype": "HTML", "options": "<div style=\"margin-top:10px;\">\n<p>Invoices to be paid within 60 days from the end of the month of receipt of undisputed invoice(s) with supported documentation.</p>\n{% for i in doc.payment_terms %}\n<p>{{i.idx}}. {{i.term}}</p><br>\n{% endfor %}\n</div>"}, {"fieldtype": "Section Break", "label": "Delivery Terms And Documentation"}, {"fieldtype": "Column Break"}, {"fieldname": "_custom_html", "label": "Custom HTML", "print_hide": 0, "fieldtype": "HTML", "options": "<div style=\"margin-top:10px;\">\n{% for i in doc.delivery_terms %}\n<p>{{i.idx}}. {{i.term}}</p><br>\n{% endfor %}\n</div>"}, {"fieldtype": "Section Break", "label": "Particular Conditions of the Purchase Order:"}, {"fieldtype": "Column Break"}, {"fieldname": "_custom_html", "label": "Custom HTML", "print_hide": 0, "fieldtype": "HTML", "options": "<div style=\"margin-top:10px;\">\n{% for i in doc.purchase_order_terms %}\n<p>{{i.idx}}.<strong>{{i.title}}</strong> - {{i.term}}</p><br>\n{% endfor %}\n</div>"}]"""
	if frappe.db.exists("Print Format", print_format_name):
		return
	print_format = frappe.new_doc("Print Format")
	print_format.name = print_format_name
	print_format.parent = "Call Off Order"
	print_format.line_breaks = 1
	print_format.font = "Default"
	print_format.show_section_headings = 1
	print_format.doc_type = "Call Off Order"
	print_format.module = "Bpl Erp"
	print_format.standard = "No"
	print_format.default_print_language = "en"
	print_format.format_data = json_data
	print_format.save(ignore_permissions=True)

