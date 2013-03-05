$(function() {
  $("#search").autocomplete({
    // source: "search/"
    source: function(request, response) {
      $.get("search/",
            {term: request.term},
            function(data) {
              response(data);
            });
    },
})
