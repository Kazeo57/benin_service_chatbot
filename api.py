from flask import Flask ,jsonify,request 
from main import chat

app=Flask(__name__)

@app.route('/',methods=['POST'])
def home():
    data=request.get_json()
    if data and "query" in data:
        query=data['query']
        return chat(query)
    return {"error":"Le paramètre 'query' est manquant"},400


@app.route('/health/',methods=['GET'])
def health():
    return "API works well"


if __name__=='__main__':
    app.run(debug=True)

