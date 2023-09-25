function playAudio(event, title, artist) {
  event.preventDefault();

  var audio = document.getElementById('audio');

  if (audio.paused) {
    audio.play();
  } else {
    audio.pause();
  }
}

function showPopup(event, title, artist) {
  event.preventDefault();
  const popup = document.getElementById('popup');
  const popupTitle = document.getElementById('popup-title');
  const popupArtist = document.getElementById('popup-artist');

  popupTitle.textContent = `Título: ${title}`;
  popupArtist.textContent = `Artista: ${artist}`;
  popup.style.display = 'block';
}

function hidePopup() {
  const popup = document.getElementById('popup');
  popup.style.display = 'none';
}