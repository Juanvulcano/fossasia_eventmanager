$(document).ready(function() {

        $('#ticket').hide();

        $('#participants').click(function(){
    var eventid;
    eventid = $(this).attr("data-eventid");
    $.get('/events/participate/', {event_id: eventid}, function(data){
        $('#participants').hide();
        $('#participate_count').html(data);
        $('#ticket').show();
    });
});

});
