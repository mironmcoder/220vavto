$(document).ready(function(){
	//Скрыть и показать меню при нажатии
	$(".category-menu-mobile").hide();
	$("h3.dropdown").click(function(){
		$(".category-menu-mobile").slideToggle("slow");
	});

	//добавить кнопку для скрытия и отображения многоуровневого меню

	$("li.dropdown-mobile:has(ul)").addClass("parrent");

	$(".parrent>ul").addClass("child")

	$(".parrent").append('<a class="expand" href="#">+</a>');

	//$(".parrent>a").addClass("pr");

	//$(".pr").after('<a href="#"></a>');
	
	//скрыть подменю

	$(".child").hide();

	//функция выпадающего подменю

	$(".expand").click(function(e){
		e.preventDefault();
		$(this).prev('ul').slideToggle("slow");
	});
});
