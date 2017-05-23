jQuery(function() {
	$(document).ready(function() {
	    $('#alltweets').DataTable();
    });
    $('td').each(function(){
	   $(this).html( $(this).html().replace(/((http|https|ftp):\/\/[\w?=&.\/-;#~%-]+(?![\w\s?&.\/;#~%"=-]*>))/g, '<a href="$1">$1</a> ') );
	});
});