function getCsrfToken() {
    const csrfInput = document.querySelector("input[name='csrfmiddlewaretoken']");
    return csrfInput ? csrfInput.value : "";
}

function deletarEpisodio(episodioId) {
    if (!confirm("Tem certeza que deseja deletar este episódio?")) {
        return;
    }

    const csrfToken = getCsrfToken();

    if (!csrfToken) {
        console.error("CSRF token não encontrado!");
        alert("Erro: Token CSRF ausente.");
        return;
    }

    fetch(`/deletar_episodio/${episodioId}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Episódio deletado com sucesso!");
            location.reload();
        } else {
            alert("Erro ao deletar episódio: " + data.error);
        }
    })
    .catch(error => {
        console.error("Erro ao deletar episódio:", error);
        alert("Erro inesperado ao deletar episódio.");
    });
}
