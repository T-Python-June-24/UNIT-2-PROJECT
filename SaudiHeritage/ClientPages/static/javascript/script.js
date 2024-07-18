$(document).ready(function () {
  var counted = false;
  $(window).scroll(function () {
    var oTop = $(".nums").offset().top - window.innerHeight;
    if (!counted && $(window).scrollTop() > oTop) {
      $(".num").each(function () {
        var $this = $(this),
          countTo = $this.attr("data-goal");
        $({ countNum: $this.text() }).animate(
          {
            countNum: countTo,
          },
          {
            duration: 2000,
            easing: "swing",
            step: function () {
              $this.text(Math.floor(this.countNum));
            },
            complete: function () {
              $this.text(this.countNum);
            },
          }
        );
      });
      counted = true;
    }
  });
});
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("animate");
      }
    });
  },
  { threshold: 0.5 }
);

const elements = document.querySelectorAll(".animate-on-scroll");
elements.forEach((element) => {
  observer.observe(element);
});
$(function () {
  $(document).scroll(function () {
    var $nav = $(".fixed-top, .nav-link, .color , .navbar-dark");
    var scrollTop = $(this).scrollTop();
    $nav.toggleClass('scrolled font-color', scrollTop > $nav.height());
    if (scrollTop > $nav.height()) {
      document.getElementById('logo').src = "/static/images/logo-black.png";
    } else {
      document.getElementById('logo').src = "/static/images/logo-white.png";
    }
    var svgIcon = document.querySelector('.navbar-toggler-icon');
    if (scrollTop > $nav.height()) {
      svgIcon.style.backgroundImage = "url(\"data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3e%3cpath stroke='rgba(0, 0, 0, 0.5)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e\")";
    } else {
      svgIcon.style.backgroundImage = "url(\"data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3e%3cpath stroke='rgba(255, 255, 255, 0.5)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e\")";
    }
  });
});



let next = document.querySelector('.next')
let prev = document.querySelector('.prev')

next.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    document.querySelector('.slide').appendChild(items[0])
})

prev.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    document.querySelector('.slide').prepend(items[items.length - 1]) 
})