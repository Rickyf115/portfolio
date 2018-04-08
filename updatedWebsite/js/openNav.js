function openNav(){
  var x = document.getElementById("head-nav");
  if(x.className === "nav-bar"){
    x.className += " responsive";
  }else{
    x.className = "nav-bar";
  }
}
