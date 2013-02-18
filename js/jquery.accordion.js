$(document).ready(function() {
 
	//ACCORDION BUTTON ACTION	

	$('div.accordionButton').click(function() {
		if($(this).next().is(':visible')) {
			$('div.accordionContent').slideUp('normal');
		} else {
			$('div.accordionContent').slideUp('normal');	
			$(this).next().slideDown('normal');
		}
	});

	//HIDE THE DIVS ON PAGE LOAD	
	$("div.accordionContent").hide();

});

