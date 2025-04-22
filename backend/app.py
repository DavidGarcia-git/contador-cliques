html = """
<!DOCTYPE html>
<html>
  <head>
    <title>Contador do Mario</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        font-size: 20px;
        text-align: center;
        margin-top: 40px;
      }
      button {
        padding: 15px 30px;
        font-size: 18px;
        cursor: pointer;
      }
      #mario-box {
        display: none;
        margin-top: 20px;
      }
    </style>
    <script>
      async function clicar() {
        await fetch('/clique', { method: 'POST' });
        atualizarContador();
        mostrarAnimacao();
      }

      async function atualizarContador() {
        const resposta = await fetch('/contador');
        const dados = await resposta.json();
        document.getElementById('valor').innerText = dados.contador;
      }

      function mostrarAnimacao() {
        const animacao = document.getElementById('mario-box');
        animacao.style.display = 'block';
        setTimeout(() => {
          animacao.style.display = 'none';
        }, 1000);
      }

      window.onload = atualizarContador;
    </script>
  </head>
  <body>
    <h2>Contador de Cliques do Mario</h2>
    <p>Clique no bloco surpresa!</p>
    <button onclick="clicar()">🎮 PULAR!</button>
    <p>Moedas coletadas: <span id="valor">0</span></p>

    <div id="mario-box">
      <img src="https://media.tenor.com/fM9e7V-YpX8AAAAi/mario-jump.gif" alt="Mario pulando">
    </div>
  </body>
</html>
"""
