// Copyright (c) 2018, Jenslaw and contributors
// For license information, please see license.txt

frappe.ui.form.on('Call Off Order', {
	refresh: function(frm) {
		frm.set_query("party_type","signatories", function(doc, cdt, cdn){
			return {
				filters:{
					name:["in",["Company","Supplier"]]
				}
			};
		});
	},


	purchase_rep:function(frm){
		frm.set_value("purchase_rep_email","");
		frm.set_value("purchase_rep_mobile_number","");
		if(frm.doc.purchase_rep){
			frappe.call({
			method:"frappe.contacts.doctype.contact.contact.get_contact_details",
			args:{"contact":frm.doc.purchase_rep},
			callback:function(r){
				if(r.message){
					frm.set_value("purchase_rep_email",r.message.contact_email);
					frm.set_value("purchase_rep_mobile_number",r.message.contact_phone);
				}
			}

		});
		}
	},
	supplier:function(frm){
		frm.set_value("supplier_rep","");
		frm.set_value("supplier_address","");
		frm.set_value("purchase_order","");
		frm.set_query("supplier_rep", function(doc) {
				return {
					filters: {
						link_doctype: "Supplier",
						link_name: doc.supplier
					}
				};
		});

		frm.set_query("supplier_address", function(doc) {
				return {
					filters: {
						link_doctype: "Supplier",
						link_name: doc.supplier
					}
				};
		});
		frm.set_query("purchase_order", function(doc) {
				return {
					filters: {
						supplier: doc.supplier,
						docstatus:1
					}
				};
		});
	},

	supplier_rep:function(frm){
		frm.set_value("supplier_rep_email","");
		frm.set_value("supplier_rep_mobile_number","");
		if(frm.doc.supplier_rep){
			frappe.call({
			method:"frappe.contacts.doctype.contact.contact.get_contact_details",
			args:{"contact":frm.doc.supplier_rep},
			callback:function(r){
				if(r.message){
					frm.set_value("supplier_rep_email",r.message.contact_email);
					frm.set_value("supplier_rep_mobile_number",r.message.contact_phone);
				}
			}

		});
		}
	},

	purchase_order:function(frm){
		frm.set_value("purchase_order_date",undefined);
		frm.set_value("purchase_order_price","");
		frm.set_value("po_price_words","");
		frm.clear_table("po_items");
		frm.refresh_field("po_items");
		if(frm.doc.purchase_order){
			frm.set_value("purchase_order_date","");
			frappe.call({
				doc:frm.doc,
				method:"get_call_off_purchase_order",
				callback:function(r){
					if(r.message){
						frm.set_value("purchase_order_date",r.message.transaction_date);
						frm.set_value("purchase_order_price",r.message.total);
					}
				}
			});

			frappe.call({
				doc:frm.doc,
				method:"get_po_amount_in_words",
				callback:function(r){
					if(r.message){
						frm.set_value("po_price_words",r.message);					
					}
				}
			});
			setup_po_items(frm);
		}		
	},

	service_agreement:function(frm){
		frappe.call({
				doc:frm.doc,
				method:"get_service_agreement",
				callback:function(r){
					if(r.message){
						frm.set_value("service_agreement_title",r.message.agreement_title);					
					}
				}
			});
	}

	
});


var setup_po_items = function(frm){
	frm.fields_dict.po_items.grid.df.read_only = 1;
	frappe.call({
			doc:frm.doc,
			method:"get_po_items",
			callback:function(r){
				if(r.message){
					
					$.each(r.message, function(i, val){
						var d = frappe.model.add_child(frm.doc, "Purchase Order Item", "po_items");
						d.item_code = val.item_code;
						d.qty = val.qty;
						d.uom = val.uom;
						d.unit_price = val.rate;
						d.total_price = val.amount;
						d.part_number = val.supplier_part_no;
						d.description = val.description;							
					});	
					frm.refresh_field("po_items");			
				}
			}
		});
	}

var update_signatories_items = function(frm){
	
}



