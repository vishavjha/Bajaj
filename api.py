from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy operation code for GET request
operation_code = "ABC123"

@app.route('/api', methods=['POST', 'GET'])
def api():
    if request.method == 'POST':
        return handle_post_request(request)
    elif request.method == 'GET':
        return jsonify(operation_code=operation_code)

def handle_post_request(request):
    try:
        data = request.get_json()
        if data:
            user_id = data.get('user_id')
            college_email = data.get('college_email')
            college_roll_number = data.get('college_roll_number')
            numbers = data.get('numbers', [])
            alphabets = data.get('alphabets', [])

            if alphabets:
                highest_alphabet = max(alphabets, key=lambda x: ord(x))
            else:
                highest_alphabet = None

            response_data = {
                "status": "Success",
                "user_id": user_id,
                "college_email_id": college_email,
                "college_roll_number": college_roll_number,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet
            }

            return jsonify(response_data)
        else:
            return jsonify({"error": "Invalid JSON data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    if __name__ == '__main__':
    app.run(debug=True)

