$(document).ready(function() {
    //MD Bootstrap payment stepper
    $('.stepper').mdbStepper();

    /* If CA, add sales tax and ca grand total, if not remove */
    function caShipTax() {
        if ($('#id_ship_state').val() === "CA") {
            $('#taxes-label').removeClass("d-none");
            $('#taxes-amt').removeClass("d-none"); 
            $("#gtotal-amt-ca").removeClass("d-none");
            $("#gtotal-amt").addClass("d-none");
            document.cookie = "ca=true";
        } else {
            $('#taxes-label').addClass("d-none");
            $('#taxes-amt').addClass("d-none"); 
            $("#gtotal-amt-ca").addClass("d-none");
            $("#gtotal-amt").removeClass("d-none");
            document.cookie = "ca=false";
        }
    }

    /* Add gray to SelectState when page loads and change when selected */
    /* if statement handles preload */
    if ($('#id_ship_city').val() != '' ) {
        $('#id_ship_state').css('color', '#47646f');
    } else {
        $('#id_ship_state').css('color', '#c3ccd3');
    }

    /* If CA value preloaded as shipping addresss */
    caShipTax();

    /* When state input changes, change font color and check for CA value */
    $('#id_ship_state').on('change', function() {
        $('#id_ship_state').css('color', '#47646f');
        caShipTax();
    });

    $('#id_bill_state').css('color', '#c3ccd3');
    
    $('#id_bill_state').on('change', function() {
        $('#id_bill_state').css('color', '#47646f'); 
    });

    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        card.update({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
        const caTax = localStorage.getItem("ca");
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);
    
       var saveInfo = Boolean($('#id-save-info').prop('checked'));
       var marketingBox = Boolean($('#id_marketing').prop('checked'));
        // From using {% csrf_token %} in the form
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        var postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
            'marketing': marketingBox,
        };
        var url = '/checkout/cache_checkout_data/';
      
        $.post(url, postData).done(function () {
});

