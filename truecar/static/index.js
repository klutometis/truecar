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
    select: function(event, ui){
      event.preventDefault();
      $("#search").val(ui.item.label);
      $("#details").empty()
      $("#details").append($("<dt>").append("harro")).append($("<dd>").append("thar"))
    }});
})
