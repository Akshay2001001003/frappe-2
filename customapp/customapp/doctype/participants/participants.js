// Copyright (c) 2024, me and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Participants", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Participants', {
    refresh: function(frm) {
        // Add event listener to the "Preview" button
        frm.fields_dict['participants'].grid.wrapper.on('click', '.grid-row-open-preview', function(e) {
            var student = $(this).attr('data-name');
            if (student) {
                // Fetch the student document
                frappe.call({
                    method: "customapp.customapp.doctype.participant.participant.get_student_image",
                    args: {
                        student: student
                    },
                    callback: function(r) {
                        if (r.message && r.message.image) {
                            // Show the image in a dialog
                            var dialog = new frappe.ui.Dialog({
                                title: __('Student Image'),
                                fields: [
                                    {
                                        fieldtype: 'HTML',
                                        options: `<img src="${r.message.image}" style="max-width: 100%; max-height: 400px;">`
                                    }
                                ]
                            });
                            dialog.show();
                        } else {
                            frappe.msgprint(__('Image not available'));
                        }
                    }
                });
            }
        });
    }
});
