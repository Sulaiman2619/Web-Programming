function Toggle() {
  var x = document.getElementById("nav");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

let list = document.querySelectorAll('.nav-link');
for (let i=0; i<list.length; i++){
  list[i].onclick = function() {
    let j = 0;
    while(j < list.length){
      list[j++].className = 'nav-link';
    }
    list[i].className = 'nav-link active';
  }
}

