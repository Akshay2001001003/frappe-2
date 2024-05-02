// Copyright (c) 2024, me and contributors
// For license information, please see license.txt
frappe.ui.form.on('Student', {
    refresh: function(frm) {
        frm.add_custom_button('Create User', function() {
            frappe.call({
                method: 'customapp.customapp.doctype.student.student.create_user_if_not_exists',
                args: {
                    email: frm.doc.email
                },
                callback: function(response) {
                    if (response.message) {
                        frappe.msgprint(response.message);
                    } else {
                        frappe.msgprint('Failed to create user.');
                    }
                }
            });
        });
    }
});
