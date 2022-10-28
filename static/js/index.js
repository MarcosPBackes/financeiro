$( document ).ready(function() {

    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var addBtn = $('#add-btn');

    $(addBtn).on('click', function('a_add'));

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

});