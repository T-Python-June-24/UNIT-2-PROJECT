const swiperHome = new Swiper('.home__swiper', {
  loop: true,
  speed:800,
  parallax:true,
  effect:'fade',

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
    type: 'fraction',  
    formatFractionCurrent: number => '0' + number, 
    formatFractionTotal: number => '0' + number
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});