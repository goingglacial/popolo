/*!
 * Start Bootstrap - Grayscale Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery to collapse the navbar on scroll
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});

// jQuery search widget
$(document).ready(function() {

      $('span.glyphicon').click(function() {
        $('#cities').val('');
        $('#results').fadeOut("slow");
    });
 
    $("#cities").autocomplete({ 
        delay: 0,
          select: function( event, ui ) {
            console.log(ui.item);
            $( "#cities" ).val( ui.item.label );
            $( "#results" ).html( ui.item.desc );
            $('#results').fadeIn("slow");
            return false;

          },
          focus: function( event, ui ) {
            $( "#results" ).html("");
            return false;
          },
          source: function(request, response) {
            var base = 'search/' + encodeURI($("#cities").val());
            //var base = 'search/'' + $("#cities").val()';
            console.log(base);

                $.ajax({
                    dataType: "json",
                    type : 'Get',
                    url: base,
                    success: function(data) {
                        // console.log(data);

                        response(data.map(function(d) {
                            return {label: (d.city + " - " + d.state), desc: d.city + "- " + d.pop};//(d.city + ', ' + d.state + ': ' + d.pop);
                        }));
                    },
                    error: function(data) {
                        console.log("ERROR");
                    }
                });
        }
    }).autocomplete( "instance" )._renderItem = function( ul, item ) {

    return $( "<li>" )
        .append( "<a>" + item.label + "<br>" + item.desc + "</a>" )
        .appendTo( ul );
    };
    });
  

//$(document).ready(function() {
//   $('html').click(function() {
//        $('#cities').val('');
//        $('#results').delay(4000).fadeToggle("slow");
//    });
// });