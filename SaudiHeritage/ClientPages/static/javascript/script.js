
  $(document).ready(function() {
    var counted = false;
    $(window).scroll(function() {
      var oTop = $('.nums').offset().top - window.innerHeight;
      if (!counted && $(window).scrollTop() > oTop) {
        $('.num').each(function() {
          var $this = $(this),
              countTo = $this.attr('data-goal');
          $({ countNum: $this.text() }).animate({
            countNum: countTo
          },
          {
            duration: 2000,
            easing: 'swing',
            step: function() {
              $this.text(Math.floor(this.countNum));
            },
            complete: function() {
              $this.text(this.countNum);
            }
          });
        });
        counted = true;
      }
    });
  });
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
        }
    });
}, { threshold: 0.5 }); 

const elements = document.querySelectorAll('.animate-on-scroll'); 
elements.forEach(element => {
    observer.observe(element);
});



