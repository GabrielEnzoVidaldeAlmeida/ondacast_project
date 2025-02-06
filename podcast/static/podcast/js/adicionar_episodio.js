document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('episode-form').addEventListener('submit', async function(event) {
        event.preventDefault();

        let formData = new FormData(this);

        let response = await fetch('/api/episodes/', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            alert('Episódio enviado com sucesso!');
            window.location.reload();
        } else {
            alert('Erro ao enviar episódio.');
        }
    });
});
