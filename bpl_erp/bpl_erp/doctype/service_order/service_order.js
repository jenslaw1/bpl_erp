// Copyright (c) 2018, Jenslaw and contributors
// For license information, please see license.txt

frappe.ui.form.on('Service Order', {
	refresh: function(frm) {
		if(!frm.doc.service_order_date){
			frm.set_value("service_order_date", frappe.datetime.now_date());
		}
		frm.set_query("party_type","signatories", function(doc, cdt, cdn){
			return {
				filters:{
					name:["in",["Company","Supplier"]]
				}
			};
		});
	},
	company_rep:function(frm){
		frm.set_value("company_rep_email","");
		frm.set_value("company_rep_mobile","");
		setup_signatory(frm);
		if(frm.doc.company_rep){
			frappe.call({
			method:"frappe.contacts.doctype.contact.contact.get_contact_details",
			args:{"contact":frm.doc.company_rep},
			callback:function(r){
				if(r.message){
					frm.set_value("company_rep_email",r.message.contact_email);
					frm.set_value("company_rep_mobile",r.message.contact_phone);
				}
			}

		});
		}
	},
	contractor_rep:function(frm){
		frm.set_value("contractor_rep_email","");
		frm.set_value("contractor_rep_mobile_number","");
		setup_signatory(frm);
		if(frm.doc.contractor_rep){
			frappe.call({
			method:"frappe.contacts.doctype.contact.contact.get_contact_details",
			args:{"contact":frm.doc.contractor_rep},
			callback:function(r){
				if(r.message){
					frm.set_value("contractor_rep_email",r.message.contact_email);
					frm.set_value("contractor_rep_mobile_number",r.message.contact_phone);
				}
			}

		});
		}
	},
	contractor:function(frm){
		frm.set_value("contractor_rep","");
		frm.set_value("contractor_address","");
		setup_signatory(frm);
		frm.set_query("contractor_rep", function(doc) {
				return {
					filters: {
						link_doctype: "Supplier",
						link_name: doc.contractor
					}
				};
		});

		frm.set_query("contractor_address", function(doc) {
				return {
					filters: {
						link_doctype: "Supplier",
						link_name: doc.contractor
					}
				};
		});
	},

	agreement:function(frm){
		frappe.call({
				doc:frm.doc,
				method:"get_service_agreement",
				callback:function(r){
					if(r.message){
						frm.set_value("agreement_title",r.message.agreement_title);					
					}
				}
			});
	},
});


frappe.ui.form.on("Service Order Items",{ 
	number_of_days:function(frm, cdt, cdn){
		calculate_service_order_items_amount(frm, cdt, cdn);
	},
	quantity:function(frm, cdt, cdn){
		calculate_service_order_items_amount(frm, cdt, cdn);
	},
	rate:function(frm, cdt, cdn){
		calculate_service_order_items_amount(frm, cdt, cdn);
		
	},
	so_items_remove:function(frm){
		calculate_service_order_items_total_amount(frm);
	}
});

var calculate_service_order_items_amount = function(frm, cdt, cdn){
	var item = locals[cdt][cdn];
	var rate = item.rate == undefined?0:item.rate;
	var quantity = item.quantity == undefined?1:item.quantity;
	var number_of_days = item.number_of_days == undefined?1:item.number_of_days
	item.amount = rate * number_of_days * quantity;
	frm.refresh_field("so_items");
	calculate_service_order_items_total_amount(frm);
}

var calculate_service_order_items_total_amount = function(frm){
	var total_amount = 0.0;
	var all_rows = frm.get_field("so_items").grid.grid_rows;
	$.each(all_rows, function(i,val){
		var amount = val.doc.amount == undefined?0:val.doc.amount;
		total_amount += amount;
	});
	frm.set_value("grand_total", total_amount);
	frm.refresh_field("grand_total");
	get_amount_in_words(frm);
}

var get_amount_in_words = function(frm){
	frm.set_value("grand_total_in_words","");
	frappe.call({
		doc:frm.doc,
		method:"get_grand_total_amount_in_words",
		callback:function(r){
			if(r.message){
				frm.set_value("grand_total_in_words",r.message);
				frm.refresh_field("grand_total_in_words");					
			}
		}
	});
}

var setup_signatory = function(frm){
	// Clear rows first
	frm.set_value("signatories", []);
	set_contractor_on_signatory(frm);
	set_company_on_signatory(frm);
	frm.refresh_field('signatories');

}

var set_contractor_on_signatory = function(frm){
	var d = frappe.model.add_child(frm.doc, "Service Order Signatories", "signatories");
	d.party_type = "Supplier";
	d.party = frm.doc.contractor;
	d.name1 = frm.doc.contractor_rep;

}

var set_company_on_signatory = function(frm){
	var d = frappe.model.add_child(frm.doc, "Service Order Signatories", "signatories");
	d.party_type = "Company";
	d.party = frm.doc.company;
	d.name1 = frm.doc.company_rep;

}