$(function() {
  $("#search").autocomplete({
    // source: "search/"
    source: function(request, response) {
      $.get("truecar/search/",
            {term: request.term},
            function(data) {
              response(data);
            });
    },
    select: function(event, ui){
      event.preventDefault();
      $("#search").val(ui.item.label);
      $("#details").empty()
      $.get("truecar/details/" + ui.item.value + "/",
           function (vehicle) {
             var flag;
             var default_image = "http://img.truecar.com/colorid_images/v1/None/175x90/f3q";

             if (vehicle.flag)
               flag = "Yes"
             else
               flag = "No"
             
             if (!vehicle.image)
               vehicle.image = default_image

             $("#details").append($("<dt>").append("Make")).append($("<dd>").append(vehicle.make))
             $("#details").append($("<dt>").append("Model")).append($("<dd>").append(vehicle.model))
             $("#details").append($("<dt>").append("Body")).append($("<dd>").append(vehicle.body))
             $("#details").append($("<dt>").append("Flag")).append($("<dd>").append(flag))
             $("#details").append($("<dt>").append("Year")).append($("<dd>").append(vehicle.year))
             $("#details").append($("<dt>").append("MSRP")).append($("<dd>").append(vehicle.MSRP))
             $("#details").append($("<dt>").append("Details")).append($("<dd>").append("See ").append($("<a />", {href: vehicle.details}).append("here")).append("."))
             $("#details").append($("<dt>").append("Image")).append($("<dd>").append($("<img />", {src: vehicle.image})))
           })
    }});
})
