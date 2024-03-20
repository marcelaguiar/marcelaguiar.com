$(document).on('submit','#post-form', function(e) { 
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "subscribe/",
        data: {
            email: $('#subscriber_email').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data) {
            if(data.success) {
                alert("success");
            }
            else {
                alert("error");
            }
        },
        error: function(jqXHR, textStatus, errorThrown ) {
            alert(errorThrown)
        }
      });
})  