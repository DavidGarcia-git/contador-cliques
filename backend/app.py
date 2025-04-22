from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)
contador = 0

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Contador de Cliques</title>
  <style>
    body {
      text-align: center;
      font-size: 22px;
      margin-top: 50px;
      font-family: Arial, sans-serif;
    }
    button {
      font-size: 24px;
      padding: 10px 20px;
      margin-top: 15px;
    }
    #contador {
      font-size: 40px;
      margin: 20px;
    }
    #mario-box img {
      margin-top: 20px;
      width: 100px;
    }
  </style>
</head>
<body>
  <h1>API do contador está no ar! 👇</h1>
  <div id="contador">0</div>
  <button onclick="clicar()">Clique aqui!</button>
  <div id="mario-box">
    <img id="mario-gif" src="https://i.imgur.com/vyKc4XQ.gif" alt="Mario pulando" style="display: none;">
  </div>

  <script>
    async function clicar() {
      document.getElementById("mario-gif").style.display = "inline";
      setTimeout(() => {
        document.getElementById("mario-gif").style.display = "none";
      }, 1000);

      const res = await fetch('/clique', { method: 'POST' });
      const data = await res.json();
      document.getElementById("contador").innerText = data.contador;
    }

    // Atualiza o contador ao carregar
    fetch('/contador')
      .then(res => res.json())
      .then(data => {
        document.getElementById("contador").innerText = data.contador;
      });
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/clique", methods=["POST"])
def clique():
    global contador
    contador += 1
    return jsonify({"contador": contador})

@app.route("/contador")
def get_contador():
    return jsonify({"contador": contador})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
