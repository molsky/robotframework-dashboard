"use strict";

$( ".run" ).click(function(event) {
    var id = event.target.id;
    $("#" + id).attr("disabled", true);
    $("#" + id).html('Running ...');
    $("#" + id).toggleClass('btn-default btn-warning');
});

function runIsDone(data) {
    var obj = JSON.parse(data);
    var id = (obj.test_name).split(".")[0];
    var status_code = (obj.status_code);
    $("#" + id).attr("disabled", false);
    $("#" + id).html('Run');
    $("#" + id).toggleClass('btn-warning btn-default');
    if (status_code == 0) {
        $("#" + id + "-files").show();
        $("#" + id + "-report").attr("href", "/results/" + id + "/report.html");
        $("#" + id + "-log").attr("href", "/results/" + id + "/log.html");
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
