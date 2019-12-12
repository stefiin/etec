/**
* Swaps between 2 pages in a single-page style.
* 'target' should be some browser address (e.g. 'services' to pull from '/services/')
* 'should_push' is true if we are navigating to a new page and a new history state should be pushed,
*  or false if we are navigating via browser forward/back and no new state should be pushed.
*/
function swapPage(target, should_push) {
	// just a silly spinner
	$("#single_page").append("<div class='sp-div'><div class='loader'></div></div>");
	// scroll to top of page
	$("html").scrollTop(0);
	if (target in window.cachedPages) {
		// insert contents of the body of the pulled doc into #single_page
		$("#single_page").html(window.cachedPages[target].getElementsByTagName("body")[0].innerHTML);
		// insert into history
		if (should_push) window.history.pushState({target: target}, document.title, "/" + target + "/");
		// fix navbar
		$("#navPanel").html($('#nav').html() + '<a href="#navPanel" class="close"></a>');
	} else {
		// fetch contents of the new page that we are changing to.
		$.get("/load_single/?f=" + target, function(data) {
			// parse the document using DOMParser API
			var htmlDoc = (new DOMParser()).parseFromString(data, "text/html");
			// insert into cache
			window.cachedPages[target] = htmlDoc;
			// insert contents of the body of the pulled doc into #single_page
			$("#single_page").html(htmlDoc.getElementsByTagName("body")[0].innerHTML);
			// insert into history
			if (should_push) window.history.pushState({target: target}, document.title, "/" + target + "/");
			// fix navbar
			$("#navPanel").html($('#nav').html() + '<a href="#navPanel" class="close"></a>');
		});
	}
}

function initSP(target) {
	swapPage(target, true);
}

window.addEventListener('popstate', function(event) {
	if (event.state == null) return;
	var target = event.state.target;
	if (target == null) return;
	swapPage(target, false);
});

window.cachedPages = {};


function contact_us() {
	// get variables
	var name = $("#name").val();
	var mail = $("#email").val();
	var message = $("#message").val();

	// confirm all fields are filled out
	if (name == "" || mail == "" || message == "") {
		$("#error_contact").html("<p>Please fill out all fields.</p>");
		return false;
	}

	// check if mail is a valid email address
	if (!validateEmail(mail)) {
		$("#error_contact").html("<p>E-mail address is in an incorrect format.</p>");
		return false;
	}

	// ajax call to send email
	$.post("/api/contact/", {name: name, mail: mail, message: message}, function(data) {
		$("#error_contact").html("<p>E-mail has been sent to E-TEC successfully.</p>");
	}).fail(function(jqXHR) {
		$("#error_contact").html("<p>Failed to send email to E-TEC.</p>");
		$("#error_contact").append("<p>" + jqXHR.responseJSON.error + "</p>");
	});

	return false;
}

function validateEmail(email) {
	var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return re.test(email);
}

function scrollToDiv(div) {
	$('html,body').animate({
		scrollTop: $(div).offset().top-10
	});
}