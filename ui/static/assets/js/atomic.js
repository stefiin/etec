/**
* Swaps between 2 pages in a single-page style.
* 'target' should be some browser address (e.g. 'services' to pull from '/services/')
* 'should_push' is true if we are navigating to a new page and a new history state should be pushed,
*  or false if we are navigating via browser forward/back and no new state should be pushed.
*/
function swapPage(target, should_push) {
	// just a silly spinner
	$("#single_page").append("<div class='sp-div'><div class='loader'></div></div>");
	// fetch contents of the new page that we are changing to.
	$.get("/load_single/?f=" + target, function(data) {
		// parse the document using DOMParser API
		var htmlDoc = (new DOMParser()).parseFromString(data, "text/html");
		// insert contents of the body of the pulled doc into #single_page
		$("#single_page").html(htmlDoc.getElementsByTagName("body")[0].innerHTML);
		// insert into history
		if (should_push) window.history.pushState({target: target}, document.title, "/" + target + "/");
		// fix navbar
		$("#navPanel").html($('#nav').html() + '<a href="#navPanel" class="close"></a>');
	});
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