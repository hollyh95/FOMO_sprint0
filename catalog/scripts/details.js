$(document).ready(function() {
    $('.small-image-tile').on('mouseenter', function(){
        $('.main-image-img').attr('src', $(this).find('img').attr('src'));
    })
});

