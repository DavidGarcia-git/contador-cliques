from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
contador = 0

@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Contador de Cliques</title>
      </head>
      <body>
        <h2>API do contador está no ar!</h2>
        <form action="/clique" method="post">
          <button type="submit">Clique para contar</button>
        </form>
        <p><a href="/contador">Ver valor atual</a></p>
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
