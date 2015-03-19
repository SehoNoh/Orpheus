var count = 1;

$("#load").click(function() {
    $.get("./load?page=" + count, function(data) {
        $("#data").html("");
        var text = '';

        $.each(data, function(key, value) {
            text += '<div><span class="title">' + value['title'] + '</span> / <span class="key">' + key + '</span><div><img src="' + value['imgSrc'] + '" width=200 height=200/></div></div>'
        });

        $("#data").html(text)

        console.log(count);
        count += 1;
        $("#load").html = 'Load More';
    });
});


$("#player").bind("ended", function() {
    var nowPlayId = $("#player").attr("uniqueId");
    var index = playlist.indexOf(nowPlayId);

    if (index == (playlist.length - 1)) {
        alert("This is last song. The player will play music from first");

        var uniqueId = playlist[0];
        $.get("/video/" + uniqueId, function(data) {
            src = JSON.parse(data);
            console.log(src["src"]);
            $("#player").attr("src", src["src"]);
            $("#player").attr("uniqueId", uniqueId);
            // playlist.push(uniqueId);
            // alert(playlist);
        });
    } else {
        alert("The player will play next music");

        var uniqueId = playlist[index + 1];
        $.get("/video/" + uniqueId, function(data) {
            src = JSON.parse(data);
            console.log(src["src"]);
            $("#player").attr("src", src["src"]);
            $("#player").attr("uniqueId", uniqueId);
            // playlist.push(uniqueId);
            // alert(playlist);
        });
    }
});


$("#search").keypress(function(event) {
    // alert("Event : " + event.which);
    if (event.which == 13) {
        // alert("");
        event.preventDefault();
        $("#header").addClass('loading');

        var dom = '';
        var START_TAG = '<div class="music_card" id="';
        var CENTER_TAG = '""><img src="';
        var END_TAG = '"/></div>'

        $.get('/load?query=' + $(this).val(), function(data) {
            list = JSON.parse(JSON.stringify(data));

            $.each(list, function(key, value) {
                dom += START_TAG;
                dom += key;
                dom += CENTER_TAG
                dom += value.imgSrc;
                dom += END_TAG;

                console.log(key + ': ' + value.imgSrc + ', ' + value.title);
            });

            $("#container").html(dom);

            $(".music_card").click(function() {
                var uniqueId = $(this).attr("id");
                $.get("/video/" + uniqueId, function(data) {
                    src = JSON.parse(data);
                    console.log(src["src"]);
                    $("#player").attr("src", src["src"]);
                    $("#player").attr("uniqueId", uniqueId);
                    playlist.push(uniqueId);
                    alert(playlist);
                });
            });
        });
    }
});