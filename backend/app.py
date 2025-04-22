from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)
contador = 0

@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Contador em tempo real</title>
        <script>
          async function clicar() {
            await fetch('/clique', { method: 'POST' });
            atualizarContador();
          }

          async function atualizarContador() {
            const resposta = await fetch('/contador');
            const dados = await resposta.json();
            document.getElementById('valor').innerText = dados.contador;
          }

          window.onload = atualizarContador;
        </script>
      </head>
      <body>
        <h2>Contador de Cliques</h2>
        <p>Clique no botão abaixo:</p>
        <button onclick="clicar()">Clique aqui</button>
        <p>Contador atual: <span id="valor">0</span></p>
      </body>
    </html>
    """
    return render_template_string(html)

@app.route("/clique", methods=["POST"])
def clicar():
    global contador
    contador += 1
    return jsonify({"mensagem": "Clique registrado!", "contador": contador})

@app.route("/contador")
def ver_contador():
    return jsonify({"contador": contador})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
