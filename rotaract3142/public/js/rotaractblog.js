$( document ).ready(function() {
    $( '.col-xs-12 p:nth-child(2)' ).on( "click", function() {
      window.open(jQuery(".col-xs-12 p:nth-child(2)").parent(".col-xs-12").find("h1 > a").attr("href"), '_self');
    });
});
