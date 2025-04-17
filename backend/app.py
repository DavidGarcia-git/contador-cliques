from flask import Flask, jsonify
app = Flask(__name__)
contador = {"cliques": 0}

@app.route('/')
def home():
    return "API está no ar! Acesse /clique para interagir."

    @app.route('/clique', methods=['POST'])
    def clicar():
        contador["cliques"] += 1
	    return jsonify(contador)

	    @app.route('/contador')
	    def ver():
	        return jsonify(contador)

		if __name__ == '__main__':
		    app.run(host='0.0.0.0', port=5000)

