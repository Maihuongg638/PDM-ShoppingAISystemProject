$(function () {
    $(".Show-model").click(function (e) { 
        e.preventDefault();
        $(".dropdown-Click").fadeIn();
        console.log("hiihi")
    });
    $(".dropdown-Click").click(function (e) { 
        e.preventDefault();
        $(".dropdown-Click").fadeOut(); //display:block + opacity
    });

    $(".Show-option").click(function (e) { 
        e.preventDefault();
        $(".select-option").fadeIn();
        console.log("hiihi")
    });
    $(".select-option").click(function (e) { 
        e.preventDefault();
        $(".select-option").fadeOut(); //display:block + opacity
    });
     // bat su kien scroll
     $(window).scroll(function () { 
        const position = $(window).scrollTop()
        if(position > 300){
            $(".header-navigation").addClass("fixed")
        }else{
            $(".header-navigation").removeClass("fixed")
        }
    });
});
