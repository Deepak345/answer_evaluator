$(document).ready(function () {
    console.log("script linked");
    $('#answerform').submit(function(e){
        e.preventDefault();
        console.log("clicked")
        var formdata = $('#answerform').serializeArray();
        console.log(formdata);
        $.post('http://127.0.0.1:8000/obtain', formdata, function (data, status) {
            console.log(data);
            $("#resultmodal").show();
            $("#resultpara").html("The obtained mark is:- <span style='color:blue;'>" + data.result + "</span>");
            // $("#resultpara").html("The obtained mark is:- <span style='color:blue;'>" + "50" + "</span>");
            
        })
        // .then(function(){$('textarea').val("");});
    perform = function(){
        document.getElementById('resultmodal').style.display='none';
        $('textarea').val("");
    }
    })
})