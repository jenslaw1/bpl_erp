# -*- coding: utf-8 -*-
# Copyright (c) 2018, Jenslaw and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from .patches import add_call_off_order_print_format



def after_install():
	add_call_off_order_print_format.execute()
	add_print_format_for_service_order()




def add_print_format_for_service_order():
	print_format_name = "Service Order Print Format"
	json_data = r"""[{"fieldname": "print_heading_template", "fieldtype": "Custom HTML", "options": "<div style=\"border:1px solid black;background:#ffcccc;text-align:center;\">\n\t\t<h2 style=\"color:red\">SERVICE ORDER</h2>\n\t\t<h5>{{doc.name}}</h5>\n\t</div>"}, {"fieldtype": "Section Break", "label": ""}, {"fieldtype": "Column Break"}, {"print_hide": 0, "options": "<div style=\"border:1px solid black;padding:10px;\">\n<table style=\"width:100%;\">\n\t<tr>\n\t\t<td><strong>Company:</strong></td>\n\t\t<td>{{doc.company}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Contractor:</strong></td>\n\t\t<td>{{doc.contractor}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Contractor's Address</strong></td>\n\t\t<td>{{doc.contractor_address}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Agreement Number:</strong></td>\n\t\t<td>{{doc.agreement}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Agreement Title:</strong></td>\n\t\t<td>{{doc.agreement_title}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Service Order Number:</strong></td>\n\t\t<td>{{doc.service_order_number}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Service Order Date:</strong></td>\n\t\t<td>{{doc.service_order_date}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Company's Rep:</strong></td>\n\t\t<td>{{doc.company_rep}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Company\u2019s Rep Mobile No:</strong></td>\n\t\t<td>{{doc.company_rep_mobile}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Company\u2019s Rep Email:</strong></td>\n\t\t<td>{{doc.company_rep_email}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Contractor\u2019s Rep:</strong></td>\n\t\t<td>{{doc.contractor_rep}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Contractor\u2019s Rep Mobile No:</strong></td>\n\t\t<td>{{doc.contractor_rep_mobile_number}}</td>\n\t</tr>\n\t<tr>\n\t\t<td><strong>Contractor\u2019s Rep E-mail:</strong></td>\n\t\t<td>{{doc.contractor_rep_email}}</td>\n\t</tr>\n</table>\n</div>\n<style>\n</style>", "fieldname": "_custom_html", "fieldtype": "HTML", "label": "Custom HTML"}, {"fieldtype": "Section Break", "label": ""}, {"fieldtype": "Column Break"}, {"print_hide": 0, "options": "<div style=\"margin-top:10px;\">\n{% for i in doc.terms %}\n<p>{{i.idx}}. {{i.term}}</p><br>\n{% endfor %}\n</div>", "fieldname": "_custom_html", "fieldtype": "HTML", "label": "Custom HTML"}, {"fieldtype": "Section Break", "label": "Service"}, {"fieldtype": "Column Break"}, {"visible_columns": [{"print_hide": 0, "fieldname": "item", "print_width": ""}, {"print_hide": 0, "fieldname": "number_of_days", "print_width": "4px"}, {"print_hide": 0, "fieldname": "quantity", "print_width": ""}, {"print_hide": 0, "fieldname": "rate", "print_width": ""}, {"print_hide": 0, "fieldname": "amount", "print_width": ""}], "print_hide": 0, "fieldname": "so_items", "label": "Service Order Items"}, {"fieldtype": "Section Break", "label": ""}, {"fieldtype": "Column Break"}, {"print_hide": 0, "fieldname": "grand_total", "label": "Grand Total"}, {"print_hide": 0, "fieldname": "grand_total_in_words", "label": "Grand Total in Words"}, {"fieldtype": "Section Break", "label": ""}, {"fieldtype": "Column Break"}, {"visible_columns": [{"print_hide": 0, "fieldname": "party_type", "print_width": ""}, {"print_hide": 0, "fieldname": "party", "print_width": ""}, {"print_hide": 0, "fieldname": "name1", "print_width": ""}, {"print_hide": 0, "fieldname": "title", "print_width": ""}, {"print_hide": 0, "fieldname": "date", "print_width": ""}, {"print_hide": 0, "fieldname": "signature", "print_width": ""}], "print_hide": 0, "fieldname": "signatories", "label": "Signatories"}, {"fieldtype": "Section Break", "label": "Particular Conditions Of Service Order"}, {"fieldtype": "Column Break"}, {"print_hide": 0, "options": "<div style=\"margin-top:10px;\">\n{% for i in doc.service_order_conditions %}\n<p>{{i.idx}}. {{i.term}}</p><br>\n{% endfor %}\n</div>", "fieldname": "_custom_html", "fieldtype": "HTML", "label": "Custom HTML"}, {"fieldtype": "Section Break", "label": "Payment Terms And Taxes"}, {"fieldtype": "Column Break"}, {"print_hide": 0, "options": "<div style=\"margin-top:10px;\">\n{% for i in doc.service_order_payment_terms %}\n<p>{{i.idx}}. {{i.term}}</p><br>\n{% endfor %}\n</div>", "fieldname": "_custom_html", "fieldtype": "HTML", "label": "Custom HTML"}]"""
	if frappe.db.exists("Print Format", print_format_name):
		return
	print_format = frappe.new_doc("Print Format")
	print_format.name = print_format_name
	print_format.parent = "Service Order"
	print_format.line_breaks = 1
	print_format.font = "Default"
	print_format.show_section_headings = 1
	print_format.doc_type = "Service Order"
	print_format.module = "Bpl Erp"
	print_format.standard = "No"
	print_format.default_print_language = "en"
	print_format.format_data = json_data
	print_format.save(ignore_permissions=True)



