$( document ).ready(function() {

    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var addBtn = $('#adicionar-btn')

    $(addBtn).on('click', function())

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

});