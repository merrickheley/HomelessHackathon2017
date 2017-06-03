$(document).on('click', 'a.smooth', function(event){
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
});

//$("a[href='#bottom']").click(function() {
//  $("html, body").animate({ scrollTop: $(document).height() }, "slow");
//  return false;
//});