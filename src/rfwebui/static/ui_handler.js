"use strict";

$( ".run" ).click(function(event) {
    var id = event.target.id;
    $("#" + id).attr("disabled", true);
    $("#" + id).html('Running ...');
    $("#" + id).toggleClass('btn-default btn-warning');
    $("#" + id + "-panel").addClass("panel-primary")
    $("#" + id + "-panel").removeClass("panel-success")
    $("#" + id + "-panel").removeClass("panel-danger")
    $("#" + id + "-panel").css("background", "rgba(238, 238, 238, 1)");

});

function runIsDone(data) {
    var obj = JSON.parse(data);
    var id = (obj.test_name).split(".")[0];
    var status_code = (obj.status_code);
    $("#" + id).attr("disabled", false);
    $("#" + id).html('Run');
    $("#" + id).toggleClass('btn-warning btn-default');
    
    $("#" + id + "-files").show();
    $("#" + id + "-report").attr("href", "/static/" + id + "/report.html");
    $("#" + id + "-log").attr("href", "/static/" + id + "/log.html");
    
    if (status_code == 0) {
        // panel-success
        $("#" + id + "-panel").removeClass("panel-primary")
        $("#" + id + "-panel").addClass("panel-success")
        $("#" + id + "-panel").css("background", "rgba(123, 239, 178, 1)");
    } 
    if (status_code == 1) {
        // panel-danger
        $("#" + id + "-panel").removeClass( "panel-primary" )
        $("#" + id + "-panel").addClass('panel-danger');
        $("#" + id + "-panel").css("background", "rgba(214, 69, 65, 1)");
    }
}

$( "#test_search" ).on('input',function(e){
    var input = $( this ).val();
    $( ".panel-heading" ).each(function() {
        var parent_id = $(this).parent().attr('id');
        var text = $( this ).text();
        if (text.indexOf(input) == -1) {
            $("#" + parent_id).hide();
        } else {
            $("#" + parent_id).show();
        }
    });
});

$( "#reset_search" ).click(function() {
    $( "#test_search" ).val("");
    $( ".panel-heading" ).each(function() {
        var parent_id = $(this).parent().attr('id');
        $("#" + parent_id).show();
    });
});
