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