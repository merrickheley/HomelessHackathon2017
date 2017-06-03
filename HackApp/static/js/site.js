var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644},
        zoom: 8
    });
}

// -------------------------------------------------------------------

$(document).on('click', 'a.smooth', function(event){
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
});

$(document).ready(function(){

    $('#home-search button').click(function(ev) {
        if ($(ev.target).hasClass('disabled')) return;

        $(ev.target).closest('.form-group').parent().find('.form-group.p1').addClass('hidden');
        $(ev.target).closest('.form-group').parent().find('.form-group.p2').removeClass('hidden');
    });

    $('#home-search select').on('input', function(ev){
        $(ev.target).closest('.form-group').next('.form-group').find('button').removeClass('disabled');
    });

    $('select.deselected').on('input', function(ev){
        $(ev.target).removeClass('deselected');
    });

    $('#home-form-submit').click(function(ev){
        ev.preventDefault();
        var geoSuccess = function(position) {
            $('#lat').val(position.coords.latitude);
            $('#lon').val(position.coords.longitude);
            $('#home-search-form').submit();
        };
        navigator.geolocation.getCurrentPosition(geoSuccess);
    });
    /*
    $('#home-search input').on('input', function(ev){
        $(ev.target).closest('.form-group').parent().find('.form-group').addClass('hidden');
        $(ev.target).closest('.form-group').next('.form-group').removeClass('hidden');

    });
    */
    //$(this).closest('.form-group').next('.form-group').removeClass('invisible');
});

//$("a[href='#bottom']").click(function() {
//  $("html, body").animate({ scrollTop: $(document).height() }, "slow");
//  return false;
//});