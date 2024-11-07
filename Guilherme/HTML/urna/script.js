// Variáveis de controle
let numeroCandidato = '';
let candidatoNome = '';
let status = 'Aguardando Votação...';
let somConfirmacao = new Audio('confirma-urna.mp3');  // Caminho do som atualizado

// Função para adicionar números ao candidato
function adicionarNumero(numero) {
    if (numeroCandidato.length < 2) {
        numeroCandidato += numero;
        document.getElementById('tela-candidato').textContent = 'Número: ' + numeroCandidato;

        // A lógica a seguir poderia ser substituída por um banco de dados de candidatos reais
        if (numeroCandidato === '22') {
            candidatoNome = 'Candidato A';
        } else if (numeroCandidato === '13') {
            candidatoNome = 'Candidato B';
        } else if (numeroCandidato === '45') {
            candidatoNome = 'Candidato C';
        } else {
            candidatoNome = 'Candidato desconhecido';
        }

        document.getElementById('tela-nome').textContent = 'Candidato: ' + candidatoNome;
        document.getElementById('tela-status').textContent = status;
    }
}

// Função para confirmar a votação
function confirmarVotacao() {
    if (numeroCandidato !== '') {
        // Alterar o status de votação
        status = 'Votação Confirmada!';
        document.getElementById('tela-status').textContent = status;

        // Tocar o som de confirmação
        somConfirmacao.play();  // Reproduz o som

    } else {
        status = 'Número inválido, tente novamente.';
        document.getElementById('tela-status').textContent = status;
    }

    // Resetar a votação
    resetarVotacao();
}

// Função para votar em branco
function votoBranco() {
    status = 'Voto em Branco Confirmado!';
    document.getElementById('tela-status').textContent = status;

    // Tocar o som de confirmação
    somConfirmacao.play();  // Reproduz o som

    resetarVotacao();
}

// Função para corrigir a votação
function corrigirVotacao() {
    status = 'Corrigir voto!';
    document.getElementById('tela-status').textContent = status;
    numeroCandidato = '';
    candidatoNome = '';
    document.getElementById('tela-candidato').textContent = 'Número: 0';
    document.getElementById('tela-nome').textContent = 'Candidato: Nenhum';
}

// Função para resetar a votação
function resetarVotacao() {
    numeroCandidato = '';
    candidatoNome = '';
    document.getElementById('tela-candidato').textContent = 'Número: 0';
    document.getElementById('tela-nome').textContent = 'Candidato: Nenhum';
}
