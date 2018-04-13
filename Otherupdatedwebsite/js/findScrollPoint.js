$(document).on('scroll', function(){
  if($(this).scrollTop()>=$('.content-grid').position().top){
    $('.nav-bar').css('background-color', 'white');
    $('.nav-bar').css('border-bottom', '1px solid black');
    $('.nav-bar .active').css('border-bottom', '1px solid black');
    $('.nav-bar a').css('color', 'black');
    $('#bar1').css('background-color', 'black');
    $('#bar2').css('background-color', 'black');
    $('#bar3').css('background-color', 'black');
  }else{
    $('.nav-bar').css('background-color', 'rgba(0,0,0,0)');
    $('.nav-bar').css('border-bottom', 'none');
    $('.nav-bar .active').css('border-bottom', '3px solid white');
    $('.nav-bar a').css('color', 'white');
    $('#bar1').css('background-color', 'white');
    $('#bar2').css('background-color', 'white');
    $('#bar3').css('background-color', 'white');
  }
});
