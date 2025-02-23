document.addEventListener("DOMContentLoaded", function () {
    const audioPlayer = document.getElementById("audioPlayer");
    const seekBar = document.getElementById("seekBar");
    const currentTimeDisplay = document.getElementById("currentTime");
    const durationDisplay = document.getElementById("duration");

    // Atualiza a barra de progresso conforme o áudio toca
    audioPlayer.addEventListener("timeupdate", function () {
        if (!isNaN(audioPlayer.duration)) {
            let progress = (audioPlayer.currentTime / audioPlayer.duration) * 100;
            seekBar.value = progress;
            currentTimeDisplay.textContent = formatTime(audioPlayer.currentTime);
        }
    });

    // Espera o áudio carregar completamente para exibir a duração
    audioPlayer.addEventListener("loadedmetadata", function () {
        if (!isNaN(audioPlayer.duration)) {
            durationDisplay.textContent = formatTime(audioPlayer.duration);
        } else {
            // Se a duração ainda não estiver disponível, tenta atualizar depois
            setTimeout(() => {
                durationDisplay.textContent = formatTime(audioPlayer.duration);
            }, 500);
        }
    });

    // Atualiza a posição do áudio quando o usuário mexe na barra
    seekBar.addEventListener("input", function () {
        let newTime = (seekBar.value / 100) * audioPlayer.duration;
        audioPlayer.currentTime = newTime;
    });

    // Funções para controlar o áudio
    window.playAudio = function () {
        audioPlayer.play();
    };

    window.pauseAudio = function () {
        audioPlayer.pause();
    };

    window.rewindAudio = function () {
        audioPlayer.currentTime -= 10;
    };

    window.forwardAudio = function () {
        audioPlayer.currentTime += 10;
    };

    // Função para formatar o tempo em mm:ss
    function formatTime(seconds) {
        if (isNaN(seconds) || seconds < 0) return "0:00";
        let minutes = Math.floor(seconds / 60);
        let secs = Math.floor(seconds % 60);
        return `${minutes}:${secs < 10 ? "0" : ""}${secs}`;
    }
});
document.addEventListener("DOMContentLoaded", function () {
    pauseBtn.style.display = "none"; // Garante que o botão pause está escondido ao iniciar a página
});

// Alterna os botões quando o áudio é tocado ou pausado
playBtn.addEventListener("click", function () {
    audioPlayer.play();
    playBtn.style.display = "none";
    pauseBtn.style.display = "inline-block";
});

pauseBtn.addEventListener("click", function () {
    audioPlayer.pause();
    pauseBtn.style.display = "none";
    playBtn.style.display = "inline-block";
});
// Função para mudar o episódio no player
function changePlayer(capa, titulo, descricao, audioUrl) {
    // Atualizar capa do episódio
    document.getElementById('episodeCapa').src = capa;
    
    // Atualizar título e descrição
    document.getElementById('episodeTitulo').textContent = titulo;
    document.getElementById('episodeDescricao').textContent = descricao;

    // Atualizar o áudio
    var audioPlayer = document.getElementById('audioPlayer');
    var source = audioPlayer.querySelector('source');
    source.src = audioUrl;
    audioPlayer.load();  // Recarrega o áudio com o novo arquivo

    // Iniciar o player automaticamente (opcional)
    audioPlayer.play();

    // Atualizar controles
    document.getElementById('playBtn').style.display = 'none';
    document.getElementById('pauseBtn').style.display = 'inline-block';
}

// Função para alternar entre play e pause
function togglePlay() {
    var audioPlayer = document.getElementById('audioPlayer');
    var playBtn = document.getElementById('playBtn');
    var pauseBtn = document.getElementById('pauseBtn');

    if (audioPlayer.paused) {
        audioPlayer.play();
        playBtn.style.display = 'none';
        pauseBtn.style.display = 'inline-block';
    } else {
        audioPlayer.pause();
        playBtn.style.display = 'inline-block';
        pauseBtn.style.display = 'none';
    }
}

// Funções de avançar e retroceder
function rewindAudio() {
    var audioPlayer = document.getElementById('audioPlayer');
    audioPlayer.currentTime -= 10;
}

function forwardAudio() {
    var audioPlayer = document.getElementById('audioPlayer');
    audioPlayer.currentTime += 10;
}

