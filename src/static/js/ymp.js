var count = 1;

$("#load").click(function () {
	$.get("./load?page="+count, function (data) {
		$("#data").html("");
		var text = '';

		$.each(data, function (key, value) {
			text += '<div><span class="title">' + value['title'] + '</span> / <span class="key">' + key + '</span><div><img src="' + value['imgSrc'] + '" width=200 height=200/></div></div>'
		});

		$("#data").html(text)

		console.log(count);
		count += 1;
		$("#load").html = 'Load More';
	});
});

$("#search").keypress(function (event) {
  if (event.which == 13) {
  	event.preventDefault();
	$("#header").addClass('loading');

	var dom = '';
	var START_TAG = '<div class="music_card" id="';
	var CENTER_TAG = '""><img src="';
	var END_TAG = '"/></div>'

  	$.get('/load?query=' + $(this).val(), function (data) {
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



	$(".music_card").click(function () {
		var uniqueId = $(this).attr("id");
		$.get("/video/"+uniqueId, function (data) {
				src = JSON.parse(data);
				console.log(src["src"]);
				$("#player").attr("src", src["src"]);
		});
	});
  		// for (var i = 0; i < list.length; i++) {
  		// 	video = list[i];
  		// };

  		// console.log();
  	});
  }

  /*
{
    "title": "2014 SBS 가요대전 B.I & BOBBY \"BORN HATER\" (초고화질)",
    "unique_id": "GWFMkOr2sps",
    "cover_image_url": "http://i.ytimg.com/vi/GWFMkOr2sps/default.jpg",
    "length": 240,
    "src": "http://r8---sn-oguesnle.googlevideo.com/videoplayback?id=19614c90eaf6b29b&itag=141&source=youtube&ms=au&mv=m&pl=21&nh=IgpwcjAxLm5ydDE5KgkxMjcuMC4wLjE&mm=31&ratebypass=yes&mime=audio/mp4&gir=yes&clen=7621628&lmt=1419404632461641&dur=239.026&fexp=900720,901454,907263,919158,927622,931362,9407103,9407463,9407891,9407913,948124,951511,951703,952302,952612,952901,955301,957201,959701,960612,961404,963201&mt=1426652713&signature=47E1C417005B9D9A1736A7323C3F04DA34B38A86.193B4FB4A93F783EAE1B73934A7E221727CE65CB&sver=3&upn=3OEdsTPPQM0&key=dg_yt0&ip=124.66.184.4&ipbits=0&expire=1426674403&sparams=ip,ipbits,expire,id,itag,source,ms,mv,pl,nh,mm,ratebypass,mime,gir,clen,lmt,dur"
}
  */
});