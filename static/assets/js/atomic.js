/**
* Swaps between 2 pages in a single-page style.
* 'target' should be some browser address (e.g. 'services' to pull from '/services/')
* 'should_push' is true if we are navigating to a new page and a new history state should be pushed,
*  or false if we are navigating via browser forward/back and no new state should be pushed.
*/
function swapPage(target, should_push) {
	$("#single_page").append("<div class='sp-div'><div class='loader'></div></div>");
	// fetch contents of the new page that we are changing to.
	$.get("/" + target + "/", function(data) {
		// parse the document using DOMParser API
		var htmlDoc = (new DOMParser()).parseFromString(data, "text/html");
		// insert contents of #single_page into body
		$("#single_page").html(htmlDoc.getElementById("single_page").innerHTML);
		// get title of loaded document
		var new_title = htmlDoc.getElementsByTagName("title")[0].innerText;
		// push history state and update URL
		if (should_push) window.history.pushState({target: target}, new_title, "/" + target + "/");
	});
}

/**
* Handles backward/forward navigation.
*/
function historyChange(event) {
	if (event.state == undefined || event.state == null) return true;
	// get the location we want to swap page to
	var target = event.state.target;
	// if it's undefined we can just let the browser handle this
	if (target === undefined) return true;
	// else, we handle the page swap
	swapPage(target, false);
}

// setup. we need to put some data into the current state.
window.history.replaceState({target: window.location.pathname.replace(/\//g, '')}, document.title, window.location.pathname);
// bind event listener for state changes
window.addEventListener('popstate', historyChange);