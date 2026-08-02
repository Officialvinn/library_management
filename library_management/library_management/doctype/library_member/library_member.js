// Copyright (c) 2026, Alvin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Member", {
    refresh(frm) {
    },

    first_name: function (frm) {
        setfullname(frm); 
    },
    last_name: function(frm){
        setfullname(frm);
    },
    after_save(frm) {
        frappe.msgprint(`hey ${frm.doc.full_name}!`);
    }
});

function setfullname(frm){
    first_name = frm.doc.first_name || "";
    last_name = frm.doc.last_name || "";
    full_name = `${first_name} ${last_name}`;
    frm.set_value("full_name", full_name);

}

