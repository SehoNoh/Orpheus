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
        // alert("This is last song. The player will play music from first");

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
        // alert("The player will play next music");

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

        if ($(this).val() === '') {
                    ga('send', 'event', 'query', 'blank search');
      alert('Insert Search Query');
        } else {
   $("#header").addClass('loading');

        var dom = '';
        var START_TAG = '<div class="music_card" id="';
        var CENTER_TAG = '" title="';
        var CENTER_2_TAG = '" author="';
        var CENTER_3_TAG ='"><img src="';
        var CENTER_4_TAG = '"/><p class="music_card_content"><span class="music_title">'
        var CENTER_5_TAG = '</span><span class="music_length">'
        var CENTER_6_TAG = '</span><span class="music_uploader">'
        var END_TAG = '</span></p></div>'
        var query = $(this).val();

/*
<p class="music_card_content">
<span class="music_title">This is just title</span>
<span class="music_length">00:00:00</span>
<span class="music_uploader">I'm the uploader</span>
</p>
*/

        $.get('/load?query=' + query, function(data) {
            ga('send', 'event', 'query', 'search', query);
            list = JSON.parse(JSON.stringify(data));

            $.each(list, function(key, value) {
                var time = value.duration;
                var min = Math.floor(time / 60);
                var sec = Math.floor(time % 60);

                dom += START_TAG;
                dom += key;
                dom += CENTER_TAG;
                dom += value.title;
                dom += CENTER_2_TAG;
                dom += value.author;
                dom += CENTER_3_TAG;
                dom += value.imgSrc;
                dom += CENTER_4_TAG;
                dom += value.title;
                dom += CENTER_5_TAG;
                dom += (min + '분 '+ sec +'초 ');
                dom += CENTER_6_TAG;
                dom += value.author;
                dom += END_TAG;

                console.log(key + ': ' + value.imgSrc + ', ' + value.title);
            });

            console.log("DOM : " + dom);

            $("#container").html(dom);

            $(".music_card").click(function() {
                var uniqueId = $(this).attr("id");
                var imgSrc = "http://i.ytimg.com/vi/" + uniqueId + "/sddefault.jpg";
                var title = $(this).attr("title");
                var author = $(this).attr("author");
                $.get("/video/" + uniqueId, function(data) {
                    ga('send', 'event', 'player', 'play', ('TITLE : "' + title + '" / Unique ID : "' + uniqueId + '"'));
                    src = JSON.parse(data);
                    console.log(src["src"]);
                    $("#player").attr("src", src["src"]);
                    $("#player").attr("uniqueId", uniqueId);
                    $("#player").attr("title", title);

                    $("#playing_album_cover").attr("src", imgSrc);
                    $("#playing_title").text(title);
                    $("#playing_uploader").text(author);
                    playlist.push(uniqueId);
                    // alert(playlist);
                });
            });
        });           
        }
    }
});