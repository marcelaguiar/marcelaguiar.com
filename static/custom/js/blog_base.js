function subscribe(token) {
    $("#post-form").submit();
}

$(document).on('submit','#post-form', function(e) { 
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: email_subscribe_url,
        data: {
            email: $('#subscriber_email').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data) {
            if(data.success) {
                // Success message
                let timeoutId = 0;
                toggleSubscribe();
                timeoutId = setTimeout(function() {
                    toggleSubscribe();
                    $('#subscriber_email').val("");
                }, 2000);
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


let subscribeButton = document.getElementById("subscribe-button");
let subscribeConfirmation = document.getElementById("subscription-confirmation");
let subContainer = document.getElementById("subscribe-container");

function toggleSubscribe() {
    if(subscribeButton.style.display == "none") {
        switchToSubscribeButton();
    }
    else {
        switchToSuccessIcon();
    }    
}

function switchToSubscribeButton() {
    subscribeConfirmation.style.display = "none";
    subscribeButton.style.display = "block";
}

function switchToSuccessIcon() {
    subscribeButton.style.display = "none";
    subscribeConfirmation.style.display = "block";
}