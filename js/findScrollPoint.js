function checkScroll(){
  var atContent = $(document).scrollTop() >= $('.content-grid').position().top;

  if(atContent){
    $('.nav-bar').addClass('scrolled');
    // Clear any inline color overrides — CSS classes handle link colors
    $('.nav-bar a').css('color', '');
    $('.nav-bar .active').css('border-bottom', '');
    $('.nav-bar').css({'background-color': '', 'border-bottom': ''});
    $('#bar1,#bar2,#bar3').css('background-color', '#2c1a0a');
  } else {
    $('.nav-bar').removeClass('scrolled');
    $('.nav-bar a').css('color', '');
    $('.nav-bar .active').css('border-bottom', '');
    $('.nav-bar').css({'background-color': '', 'border-bottom': ''});
    // Keep bars dark if the mobile overlay is open
    if($('#bool').attr('class') !== 'not'){
      $('#bar1,#bar2,#bar3').css('background-color', '');
    }
  }
}

$(document).ready(function(){ checkScroll(); });
$(document).on('scroll', function(){ checkScroll(); });
