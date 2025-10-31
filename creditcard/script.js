// get a reference to the form. We can access all the named form inputs through the form element.
    const theForm = document.querySelector('#checkoutForm');

function displayError(msg) {
	// display error message
	document.querySelector('.errors').textContent = msg
}

function isCardNumberValid(number) {
	// normally we would contact a credit card service...but we don't know how to do that yet. So to keep things simple we will only accept one number
	return number === '1234123412341234'
}

function submitHandler(event) {
	event.preventDefault();
  let errorMsg = '';
	displayError('');

  let cardNumber = document.querySelector('#creditCardNumber');
  const cardNum = cardNumber.value.replace(/\s+/g, '').trim();

    
    if (!/^\d{16}$/.test(cardNum)) {
    errorMsg += 'Card number must be 16 digits\n';
    } else if (!isCardNumberValid(cardNum)) {
      errorMsg += 'Card number is not valid\n';
    }
    
  //check date
  const expYear = Number(document.querySelector('#year').value);   
  const expMonth = Number(document.querySelector('#month').value);
  const currentDate = new Date()

  if (2000 + expYear < currentDate.getFullYear() || (2000 + expYear === currentDate.getFullYear() && expMonth <= (currentDate.getMonth()))
  ) {
      errorMsg += 'Card is expired\n';
  }
  

    if (errorMsg !== '') {
		// there was an error. stop the form and display the errors.
		displayError(errorMsg)
		return;
    }
    // Success: show a confirmation message
    const formContainer = document.getElementById('checkoutForm');
    formContainer.innerHTML = '<h2>Thank you for your purchase.</h2>';
}

document.querySelector('#checkoutForm').addEventListener('submit', submitHandler)