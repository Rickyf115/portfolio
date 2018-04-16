function openNav(){
  var x = $("#bool");
  if(x.attr('class') === "closed"){
    $('#head-nav').css('height','100%');
    $('#head-nav').css('background', 'white');
    $('#bar1').css('background','black');
    $('#bar2').css('background','black');
    $('#bar3').css('background','black');
    x.attr('class', 'not');
  }else{
    $('#head-nav').css('height','0%');
    $('#head-nav').css('background','rgba(255,255,255,0)');
    $('#bar1').css('background','white');
    $('#bar2').css('background','white');
    $('#bar3').css('background','white');
    x.attr('class', 'closed');
  }
}
