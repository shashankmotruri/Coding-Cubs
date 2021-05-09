$(document).ready(function () {

     $('.collapsed').on('click', function () {
         $('.collapsed').removeClass('active');
        $(this).addClass('active');
    });
     $('.sub-menu li').on('click', function () {
         $('.sub-menu .active').removeClass('active');
        $(this).addClass('active');
    });
});