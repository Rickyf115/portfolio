function openNav(){
  var x = $("#bool");
  if(x.attr('class') === "closed"){
    $('#head-nav').addClass('open');
    $('#bar1').css('background-color', '#1a1a2e');
    $('#bar2').css('background-color', '#1a1a2e');
    $('#bar3').css('background-color', '#1a1a2e');
    x.attr('class', 'not');
  } else {
    $('#head-nav').removeClass('open');
    // Only reset to white if the nav bar is not scrolled
    if(!$('.nav-bar').hasClass('scrolled')){
      $('#bar1').css('background-color', '');
      $('#bar2').css('background-color', '');
      $('#bar3').css('background-color', '');
    }
    x.attr('class', 'closed');
  }
}
