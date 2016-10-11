"use strict";

$( "#settings_btn" ).click(function() {
    $('.btn').button('reset');
    $( "#settings" ).show( "slow", function() {} );
});

$( "#settings_btn_close" ).click(function() {
    $( "#settings" ).hide( "slow", function() {} );
});

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
