document.addEventListener("DOMContentLoaded", function () {
    const audioPlayer = document.getElementById("audioPlayer");
    const playPauseBtn = document.getElementById("btn-playPause");
    const playPauseIcon = document.getElementById("playPauseIcon");
    const btnVoltar = document.getElementById("btn-voltar");
    const btnAvancar = document.getElementById("btn-avancar");
    const progressBar = document.getElementById("progressBar");
    const progress = document.getElementById("progress");
    const tempoAtual = document.getElementById("tempoAtual");
    const tempoTotal = document.getElementById("tempoTotal");
    const controleVolume = document.getElementById("controleVolume");

    // Formatar tempo em minutos e segundos
    function formatarTempo(segundos) {
        const min = Math.floor(segundos / 60);
        const sec = Math.floor(segundos % 60);
        return `${min}:${sec < 10 ? "0" + sec : sec}`;
    }

    // Atualizar barra de progresso
    function atualizarProgresso() {
        const porcentagem = (audioPlayer.currentTime / audioPlayer.duration) * 100;
        progress.style.width = `${porcentagem}%`;
        tempoAtual.textContent = formatarTempo(audioPlayer.currentTime);
    }

    // Definir duração total quando o áudio carregar
    audioPlayer.addEventListener("loadedmetadata", function () {
        tempoTotal.textContent = formatarTempo(audioPlayer.duration);
    });

    // Atualizar progresso enquanto o áudio toca
    audioPlayer.addEventListener("timeupdate", atualizarProgresso);

    // Permitir clique na barra de progresso
    progressBar.addEventListener("click", function (e) {
        const largura = this.clientWidth;
        const cliqueX = e.offsetX;
        const novaPosicao = (cliqueX / largura) * audioPlayer.duration;
        audioPlayer.currentTime = novaPosicao;
    });

    // Reproduzir ou pausar áudio
    playPauseBtn.addEventListener("click", function () {
        if (audioPlayer.paused) {
            audioPlayer.play();
            playPauseIcon.src = "/static/user/svg/pause.svg";
        } else {
            audioPlayer.pause();
            playPauseIcon.src = "/static/user/svg/play.svg";
        }
    });

    // Retroceder 10 segundos
    btnVoltar.addEventListener("click", function () {
        audioPlayer.currentTime = Math.max(0, audioPlayer.currentTime - 10);
    });

    // Avançar 10 segundos
    btnAvancar.addEventListener("click", function () {
        audioPlayer.currentTime = Math.min(audioPlayer.duration, audioPlayer.currentTime + 10);
    });

    // Ajustar volume
    controleVolume.addEventListener("input", function () {
        audioPlayer.volume = this.value;
    });

    // Atualizar ícone de play/pause ao terminar a música
    audioPlayer.addEventListener("ended", function () {
        playPauseIcon.src = "/static/user/svg/play.svg";
    });
});
