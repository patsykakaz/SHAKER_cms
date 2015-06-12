$(window).load(function(){
    i = 1;
    $('.col-md-4').not('triple-item').not('half-item').each(function(){
        if(i % 5 == 0){
            $(this).addClass('item-dark');
        }
        i+=1;
    });

    $('.secondary-caption').each(function(){
        $(this).css('margin-top', ($(this).parent('.item-secondary-layer').outerHeight()-$(this).outerHeight())/2);
    });

    $('.layer-img').each(function(){
        img = $(this).children('img');
        if($(this).width() > $(this).height()){
            img.css('width', '100%').css('top', ($(this).height() - img.outerHeight())/3);
        }else{
            img.css('height', '100%').css('left', ($(this).width() - img.outerWidth())/2);
        }
    });

    $('#test').click(function(){
        $('#test-click').toggleClass('hide');
    });
});