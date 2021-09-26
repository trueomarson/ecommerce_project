var stripe = Stripe('pk_test_51JVF0JK6v6fVXC6SvxxNN2e3DXaENVRTRErsqH3BKXXq5ENSIXJbl6WXQkKHRm4zpTHexYZjB6qT74N1jXu1xLdr00MDH3BtAC');

var elem = document.getAnimations.ElementyById('submit');
clientsecret = elem.getAttribute('data-secret');

var elements = stripe.elements()
var style = {
    base: {
        color: "#000",
        lineHeight: '2.4',
        fontSize: '16px',
    }
};
var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on('change', function(event) {
    var displayError = document.getElementById('card-errors')
    if (event.error) {
      displayError.textContent = event.error.message;
      $('#card-errors').addClass('alert alert-info');
    } else {
      displayError.textContent = '';
      $('#card-errors').removeClass('alert alert-info');
    }
    });

