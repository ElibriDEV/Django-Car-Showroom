$(document).ready(function(){
    $(".btn").hover(
        function(){
        $(this).attr("style", "background-color: white !important; color: #b62513 !important; border: 1px solid #b62513 !important");
    },
        function(){
        $(this).removeAttr("style");
    }
    );
});
