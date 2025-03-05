from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
#def home():
#	return "Flask server is up-to-date!"

def index():
	return render_template("index.html")

@app.route('/check', methods=['POST'])
def check_number():
	data = request.json
	if not isinstance(data.get("number"), (int, float)):
		return jsonify({"error": "Enter Number!"}), 400
	number = data["number"]

	if isinstance(number, float):
	   return jsonify({"message": "You've entered a fractional number!"})
	if number % 2 == 0:
	   return jsonify({"message": "Even number."})
	else:
	   return jsonify({"message": "Odd number."})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
