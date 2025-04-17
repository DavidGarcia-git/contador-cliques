from flask import Flask, jsonify, request

app = Flask(__name__)
contador = {"cliques": 0}

@app.route("/")
def home():
    return "API do contador está no ar! Use /clique para contar."

    @app.route("/clique", methods=["POST"])
    def clicar():
        contador["cliques"] += 1
        return jsonify(contador)

	    @app.route("/contador", methods=["GET"])
	    def ver_contador():
	        return jsonify(contador)

		if __name__ == "__main__":
		    app.run(host="0.0.0.0", port=5000)

