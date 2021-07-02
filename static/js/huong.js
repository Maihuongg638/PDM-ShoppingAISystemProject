$(function () {
    $("#latest-product").owlCarousel({
       items: 1,
       nav: false,
       dots: true,
       loop: true,
       autoplay: true,
       autoplayTimeout: 5000
    });
 
 
 });
//  $(function () {
//     $(".owl-carousel").owlCarousel({
//         items: 1,
//         margin: 10,
//         loop: true,
//         nav: true,
//         navText: ["<i class='fa fa-user'></i>", "hello"],
//         dots: true,
//         autoplay: true,
//         autoplayTimeout: 5000,
//         autoplayHoverPause: true,
//         smartSpeed: 1000,
//     });
// });

$(function () {
   $(".owl-carousel").owlCarousel({
       items: 1,
       // margin: 10,
       loop: false,
       nav: false,
       // navText: [`<i class="fas fa-chevron-left"></i>`, `<i class="fas fa-chevron-right"></i>`],
       dots: true,
       // autoplay: true,
       autoplayTimeout: 5000,
       autoplayHoverPause: true,
       smartSpeed: 1000,
       // video: true,
       // videoHeight: true,
   });
   
});

$(function () {
   $(".owl-carousel.owl-carousel-2").owlCarousel({
       items: 1,
       // margin: 10,
       loop: true,
       nav: true,
       navText: [`<i class="fas fa-chevron-left"></i>`, `<i class="fas fa-chevron-right"></i>`],
       dots: false,
       autoplay: true,
       autoplayTimeout: 5000,
       autoplayHoverPause: true,
       smartSpeed: 1000,
   });
});

$(function () {
   $(".Button").click(function (e) { 
       e.preventDefault();
       $(".Button-drop").addClass("show");
   });
});