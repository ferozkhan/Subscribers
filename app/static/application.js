$(document).ready(function() {
    window.onsubmit = function(){
        $.each($(".delete"), function(){
            $(this).attr("disabled", "disabled");
        });
    }
});