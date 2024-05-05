// Copyright (c) 2024, me and contributors
// For license information, please see license.txt

frappe.ui.form.on("Program",{
    onload:function(frm){
     frm.set_query("instructor",()=>
    {   
        return {
        "filters":{
            "designation":"Instructor"
        }
    };
    });
    },
    after_save: function(frm) {
        frappe.call({
            method: "customapp.customapp.doctype.program.program.calculate_total_credits",
            args: {
                program_name: frm.doc.name // Pass program name as an argument
            },
            callback: function(r) {
                if (r.message !== undefined) {
                    // Update the total credits field with the new value
                    // frm.doc.total_credits = r.message;
                    frm.set_value("total_credits",r.message);
                    frm.refresh_field('total_credits');
                } else {
                    frappe.msgprint("Failed to update total credits. Please try again.");
                }
            }
        });
    }    
}); 
