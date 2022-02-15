window.addEventListener('DOMContentLoaded', function () { 
    $('div#add_item').click(function () {
        $('<li>Item</li>').appendTo('ul.my_list');
    });
    $('div#remove_item').click(function () {
        $('ul.my_list li').last().remove();
    });
    $('div#clear_list').click(function () {
        $('ul.my_list').empty();
    });
});
