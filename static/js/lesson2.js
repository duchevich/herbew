$(document).ready(function() {
    
    /*---- WRAP ----*/
    $(function() {
        $('.img').click(function() {
            //var wrap = $(this).parent().css('transform');
            if($(this).parent().css('transform') == 'matrix(1, 0, 0, 1, 0, 0)') {
                  $(this).parent().css({'transform':'rotateY(180deg)'});
            } 
            else {
                  $(this).parent().css({'transform':'rotateY(0deg)'});
            }
        });
    });
          
   
      
    /*---- MASONRY ----*/
    
    var container = document.querySelector('#container');
          var msnry = new Masonry( container, {
          // Настройки
                columnWidth: '.item',
                itemSelector: '.item'
          });   
          
})