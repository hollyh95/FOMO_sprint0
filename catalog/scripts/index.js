$(function(context) {
    return function() {
        var ajaxOutput = $('#products');
        ajaxOutput.load('/catalog/index.inner/' + context.catid + '/1/');
        $('#getLastPage').on('click', function() {
            if (parseInt($('#currentPage').html(), 10) > 1) {
                ajaxOutput.load('/catalog/index.inner/' + context.catid + '/' + (parseInt($('#currentPage').html(), 10) - 1));
                $('#currentPage').html(parseInt($('#currentPage').html(), 10) - 1); // decrement
            }
            else {
                console.log('unable');
            }
        });
        $('#getNextPage').on('click', function() {
            if (parseInt($('#currentPage').html(), 10) < parseInt($('#maxPages').html(), 10)) {
                ajaxOutput.load('/catalog/index.inner/' + context.catid + '/' + (parseInt($('#currentPage').html(), 10) + 1));
                $('#currentPage').html(parseInt($('#currentPage').html(), 10) + 1); // increment
            }
            else {
                console.log('unable');
            }
        });
    }
}(DMP_CONTEXT.get()))
