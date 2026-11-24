async function enviarMensagem() {
    let mensagem = document.getElementById('mensagem').value;
    if (!mensagem) {
        return;
    }
    adicionarMensagem('Você', mensagem);
    document.getElementById('mensagem').value = '';
    let resposta = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            mensagem: mensagem,
            usuario_id: 1
        })
    });
    let dados = await resposta.json();
    adicionarMensagem('Bot', dados.resposta);
}

function adicionarMensagem(usuario, texto) {
    let chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `
        <div class="mensagem-item">
            <strong>${usuario}:</strong>
            ${texto}
        </div>
    `;
    chatBox.scrollTop = chatBox.scrollHeight;
}
