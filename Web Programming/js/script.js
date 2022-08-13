let menuToggle = document.querySelector ('.toggle');
let Navbar = document.querySelector ('.nav');
menuToggle.onclick = function() {
  Navbar.classList.toggle('active');
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

