from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple dictionary to simulate chatbot responses
responses = {
    "hello": "Hello! How can I help you?",
    "tourism": "Saudi Arabia is known for its rich history and cultural heritage. You can visit places like Riyadh, Jeddah, and historical sites like Diriyah and Al-Ula.",
    "greetings": "Greetings! How can I assist you today?",
    "default": "I'm sorry, I don't understand that. Can you please ask another question?"
}

# Endpoint to handle user queries
@app.route('/api/chatbot/', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_message = data['message'].lower()  # Convert message to lowercase for easier matching

    # Simple logic to determine bot response based on user message
    if 'hello' in user_message:
        bot_response = responses['hello']
    elif 'tourism' in user_message or 'visit' in user_message:
        bot_response = responses['tourism']
    elif 'hi' in user_message or 'hey' in user_message:
        bot_response = responses['greetings']
    else:
        bot_response = responses['default']

    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
