$(document).ready(function () {

		$('.captcha').click(function () {
	    $.getJSON("/captcha/refresh/", function (result) {
	        $('.captcha').attr('src', result['image_url']);
	        $('#id_captcha_0').val(result['key'])
	    });
	});


	var form = $('.reviews-form-main');
	var url = form.attr("action");
	var product = form.attr("product");
	var data = {};
	var parent = 0;
	

	$('.rating__send').click(function(e){
		e.preventDefault();
		var getParent = $(this).attr('parent');
		var userName = $(this).attr('name');
		form.attr('parent', getParent)
		parent = form.attr("parent");
		$('#reply').text('Ответить пользователю: ' + userName + ' X');
		$('.reply-comment').css("display", "block");

		///scroll
		$('html, body').animate({
            scrollTop: $(".reviews-h").offset().top
        }, 500);
	});

	
	$('.reply-comment').click(function(e){
		e.preventDefault();
		$('.reply-comment').hide();
		form.attr("parent", "0")
	});


	$(form).submit(function(e) {
		e.preventDefault();
		data.csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
		data.username = $("input[name=username]").val();
		data.email = $("input[name=email]").val();
		data.comment = $("textarea[name=comment]").val();
		data.captcha_0 = $("input[name=captcha_0]").val();
		data.captcha_1 = $("input[name=captcha_1]").val();
		data.parent = parent;
		data.product = product;

	$("#modal-btn").click(function(e){
		e.preventDefault();
		$("#modal-msg").css("opacity","0").css("pointer-events","none");
	});

		$.ajax({
             url: url, 
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                console.log("OK");
                $("#modal-msg").css("opacity","1").css("pointer-events","auto");
                $(".modalwindow h3").text('Комментарий успешно отправлен!');
                $(".modalwindow p").text('Комментарий будет опубликован в ближайшее время')
             },
             error: function(){
                 console.log("error")
                $("#modal-msg").css("opacity","1").css("pointer-events","auto");
                $(".modalwindow h3").text('Возникла непредвиденная ошибка!');
                $(".modalwindow p").text('Проверьте введённые данные, или попробуйте снова')
             }
         })
	});

});