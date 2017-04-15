

$(document).ready( function() {
     loadAllShoplists();
});

function loadAllShoplists() {

    $('#lists_form > div.list-group > div.not:hidden').remove();

    $.ajax({
        type: "GET",
        dataType: "json",
        url: url_shoplist_list_all_json,
        success: function(data) {
            shoplistsDisplay(data);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            alert( textStatus + '\n' + errorThrown);
        }
    });
}

function shoplistsDisplay(jsonData) {
    jsonData.forEach(function(item, index) {
        $('#lists_form > div.list-group > div.hidden')
            .clone(true, true)
            .appendTo('#lists_form > div.list-group')
            .removeClass('hidden')
            .children('input[type="checkbox"]')
            .attr('value', item.pk)
            .siblings('span')
            .children('a')
            .attr('href', "" + item.pk + "/edit")
            .children('strong')
            .text(item.fields.name)
    });
}
