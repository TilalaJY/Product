$(document).ready(function() {
    $('.dateinput').datepicker({ format: "yyyy-mm-dd" });
});

var product_table = $('.product_record').dataTable({
    stateSave: true,
    "processing": true,
    "serverSide": true,
    "ajax": "/product-list",
    "columnDefs": [
        {
            "targets": [0],
            "visible": false,
            "searchable": false
        },
        {
            targets: -1,
            title: 'Actions',
            orderable: false,
            render: function (data, type, row, meta) {
                if(row[row.length-1]){
                    return '<a href="/product-update/'+row[0]+'" class="btn btn-primary" title="Edit details">Edit</a><a href="/product-delete/'+row[0]+'" class="btn btn-danger" title="Delete">Delete</a>';
                }else{
                    return '<p>only admin can change</p>'
                }
            },

        },


    ],
    "order": [[0, "desc"]],

});


var category_table = $('.Category_record').dataTable({
    stateSave: true,
    "processing": true,
    "serverSide": true,
    "ajax": "/category-list",
    "columnDefs": [
        {
            "targets": [0],
            "visible": false,
            "searchable": false
        },
        {
            targets: -1,
            title: 'Actions',
            orderable: false,
            render: function (data, type, row, meta) {
                if(row[row.length-1]){
                    return '<a href="/category-update/'+row[0]+'" class="btn btn-primary" title="Edit details">Edit</a><a href="/category-delete/'+row[0]+'" class="btn btn-danger" title="Delete">Delete</a>';
                }else{
                    return '<p>only admin can change</p>'
                }
            },

        },

    ],
    "order": [[0, "desc"]],

});
