$(document).ready(function() {
    $("#data_table").DataTable();
    $("#clientList").DataTable();
    $("#tbl_bills").DataTable({
        "columnDefs": [ {
            "targets": 6, //Targets would be the 0 based index of the column
             "data": 'IsTaxExempt',
             "render": function ( data, type, full, meta ){
                       return data ? '<input type="checkbox" disabled checked/>' : '<input type="checkbox" disabled/>'
                    }
       } ]
    });
    //$("#statusTable").DataTable();
});