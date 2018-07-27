$(window).scroll(function() {
  if($(this).scrollTop() > 40)  /*height in pixels when the navbar becomes non opaque*/
  {
      $('.opaque-navbar').addClass('opaque');
      $('.brand').addClass('opaque');
  } else {
      $('.opaque-navbar').removeClass('opaque');
      $('.brand').removeClass('opaque');
  }
});

$(".clickme").click(function() {
    $(".hideme").toggle();
    $(".showme").toggle();
});

$(".clickcomment").click(function() {
    $(".showcomment").toggle();
    $(".showme").toggle();
});
