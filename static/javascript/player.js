// $(window).on('load', function() {
// 	var audioPlayer = document.getElementById('audioPlayer');
// 	audioPlayer.play();
// 	$('#play_button').removeClass('fa-stop').addClass('fa-play');
// });


$('#play_button').on('click', function() {

	if ($(this).hasClass('fa-play')) {
		var audioPlayer = document.getElementById('audioPlayer');
		audioPlayer.play();
		$(this).removeClass('fa-play').addClass('fa-stop');
		return
	}
	if ($(this).hasClass('fa-stop')) {
		var audioPlayer = document.getElementById('audioPlayer');
		audioPlayer.pause();
		$(this).removeClass('fa-stop').addClass('fa-play');
	}
});


var addSongInQueue = function() {
	var musicId = $('#currentSong').data('other');
	var csrfToken = $('#csrf_token').data('other')

	$.ajax({
		url : 'http://127.0.0.1:8000/add_song_in_queue',
		data: {
			'song_id' : musicId,
			'csrfmiddlewaretoken': csrfToken			
		},
		type: 'POST',
		success: function(result) {
			if (result.is_added) {
				$('#queue').append(
					'<div class="box">' +
					'<a href="{% url "song" song_id=' + result.music.id + '%}">' + result.music.title + '</a>' +
					'</div>'
				)
			}
		}
	});
};
