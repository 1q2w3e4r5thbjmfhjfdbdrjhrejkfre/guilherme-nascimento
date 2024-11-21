// script.js
function atualizarPlacar(jogo) {
    const placarInput = document.getElementById(`placar-jogo${jogo}`);
    const placar = placarInput.value;
  
    // Verifica se o placar está no formato correto (ex: "2 - 1")
    if (placar.match(/^\d{1,2} - \d{1,2}$/)) {
      // Preencher os vencedores na próxima fase
      const vencedor = calcularVencedor(placar);
      alert(`Vencedor do Jogo ${jogo}: ${vencedor}`);
  
      // Atualiza os vencedores na fase seguinte
      if (jogo <= 4) {
        const fase2Jogo = jogo <= 2 ? 5 : 6;
        const vencedorSpan = document.querySelector(`#placar-jogo${fase2Jogo} ~ span`);
        vencedorSpan.textContent = `Vencedor Jogo ${jogo}`;
      }
  
      // Checa se a final já foi definida
      if (jogo === 7) {
        document.getElementById('vencedor').innerText = `Campeão: ${vencedor}`;
      }
    } else {
      alert('Insira o placar no formato correto: "X - Y"');
    }
  }
  
  function calcularVencedor(placar) {
    const [time1, time2] = placar.split(' - ').map(Number);
    return time1 > time2 ? 'Time 1' : 'Time 2';
  }
  