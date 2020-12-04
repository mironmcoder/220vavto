jQuery(function ($) {

	$(".slide-thumb-item img").click(function(e){
		var slidethumb = $(this).attr('src');
		$("#slide-main").attr('src', slidethumb);
		alert(v);
	});
});