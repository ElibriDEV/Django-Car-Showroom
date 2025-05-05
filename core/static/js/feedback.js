$(document).ready(function(){
    $("input, textarea, select").hover(
        function(){
        $(this).attr("style", "background-color: #FFDBDB !important; border: 1px solid #b62513 !important");
    },
        function(){
        $(this).removeAttr("style");
    }
    );
});