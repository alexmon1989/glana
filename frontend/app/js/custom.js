$(document).on('ready', function () {
    $.extend($.scrollTo.defaults, {
        axis: 'y',
        duration: 800
    });

    $(".scrollTo").click(function (e) {
        e.preventDefault();
        var href = $(this).attr('href');
        $.scrollTo($(href));
    })
});