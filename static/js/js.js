$(function () {

      var loadForm = function () {
        var btn = $(this);
        console.log(btn.attr('data-url'));
        $.ajax({
          url: btn.attr('data-url'),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#divClient").modal("show");
          },
          success: function (data) {
            $("#divClient .modal-content").html(data.html_form);
          }
        });
      };
  
     var saveForm = function () {
          var form = $(this);
          console.log(form.attr("action"));
          $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
              if (data.form_is_valid) {
                console.log(data.client_list);
                $("#clientList tbody").html(data.client_list);
                $("#divClient").modal("hide");
              }
              else {
                $("#divClient .modal-content").html(data.html_form);
              }
            }
          });
          return false;
        };
    
     /* Binding */

  // Create client
  $(".js-create-client").click(loadForm);
  $("#divClient").on("submit", ".js-client-create-form", saveForm);

  // Update client
  $("#clientList").on("click", ".js-update-client", loadForm);
  $("#divClient").on("submit", ".js-client-update-form", saveForm);

  //Delete client
  $("#clientList").on("click", ".js-delete-client", loadForm);
  $("#divClient").on("submit", ".js-client-delete-form", saveForm);

  
  //ping client
  $("#monitorTable").on('click', '.js-ping-client', loadForm);


// Bills
var loadFormBill = function() {
  var btn = $(this);
  $.ajax({
    url: btn.attr('data-url'),
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#div_bills").modal("show");
    },
    success: function (data) {
      $("#div_bills .modal-content").html(data.html_form);
    }
  });
};

var saveFormBill = function() {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#tbl_bills tbody").html(data.bills_list);
          $("#div_bills").modal("hide");
        }
        else {
          $("#div_bills .modal-content").html(data.html_form);
        }
      }
    });
    return false;
};

// Create bill
$(".js-create-bills").click(loadFormBill);
$("#div_bills").on("submit", ".js-create-bill-form", saveFormBill);


  

$("#monitorTable").on('click', '.js-create-status', function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr('data-url'),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#newMonitor").modal("show");
        },
        success: function (data) {
          $("#newMonitor .modal-content").html(data.html_form);
        }
      });
    });

$("#newMonitor").on('submit', '.js-create-status-form', function () {
      var form = $(this);
        $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function (data) {
            if (data.form_is_valid) {
              //alert("Status created.")
              $('.alert').alert();
              $("#newMonitor").modal("hide");
            }
            else {
              $("#newMonitor .modal-content").html(data.html_form);
            }
          }
        });
        return false;
      });


      //create_status_1

  $(".js-create-status").click(function () {
        var btn = $(this);
        $.ajax({
          url: btn.attr('data-url'),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#newStatus").modal("show");
          },
          success: function (data) {
            $("#newStatus .modal-content").html(data.html_form);
          }
        });
      });
  
  $("#newStatus").on("submit", ".js-create-status-form-1", function () {
        var form = $(this);
        console.log(form.attr("action"));
        console.log(form.data);
          $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
              if (data.form_is_valid) {
                //alert("Status created.")
                $("#statusTable tbody").html(data.status_list)
                $("#newStatus").modal("hide");
              }
              else {
                $("#newStatus .modal-content").html(data.html_form);
              }
            }
          });
          return false;
        });

      $("#statusTable").on('click', '.js-update-status', function () {
        var btn = $(this);
        $.ajax({
          url: btn.attr('data-url'),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#newStatus").modal("show");
          },
          success: function (data) {
            $("#newStatus .modal-content").html(data.html_form);
          }
        });
      });

      $("#newStatus").on("submit", ".js-update-status-form", function () {
        var form = $(this);
          $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
              if (data.form_is_valid) {
                $("#statusTable tbody").html(data.status_list);
                $("#newStatus").modal("hide");
              }
              else {
                $("#newStatus .modal-content").html(data.html_form);
              }
            }
          });
          return false;
        });
  
        $("#statusTable").on('click', '.js-delete-status', function () {
          var btn = $(this);
          console.log(btn.attr('data-url'));
          $.ajax({
            url: btn.attr('data-url'),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
              $("#newStatus").modal("show");
            },
            success: function (data) {
              $("#newStatus .modal-content").html(data.html_form);
            }
          });
        });
  
        $("#newStatus").on("submit", ".js-status-delete-form", function () {
          var form = $(this);
            $.ajax({
              url: form.attr("action"),
              data: form.serialize(),
              type: form.attr("method"),
              dataType: 'json',
              success: function (data) {
                if (data.form_is_valid) {
                  $("#statusTable tbody").html(data.status_list);
                  $("#newStatus").modal("hide");
                }
                else {
                  $("#newStatus .modal-content").html(data.html_form);
                }
              }
            });
            return false;
          });

      $("#id_client").change(function(){
        this.form.submit();
      });
      
      $("#id_status_type").change(function(){
        this.form.submit();
      });
});