from flask import Flask,request,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
import json
app=Flask(__name__)

@app.route('/signup',methods=['POST'])
def signup():
    new_data = request.get_json()
    username = new_data.get('username')
    password = new_data.get('password')
    hash_password = generate_password_hash(password)
    try:
        with open('first.json','r') as f:
            data = json.load(f)
    except:
        data =[]

    new_user = {
        "id":len(data)+1,
        "username":username,
        "password":hash_password
    }

    data.append(new_user)

    with open('first.json','w') as f:
        json.dump(data,f,indent=4)

    return jsonify({"massege":"Data stored in First.json"})
@app.route('/login',methods=['POST'])
def login():
    new_data = request.get_json()
    username = new_data.get('username')
    password = new_data.get('password')
    with open('first.json','r') as f:
        data = json.load(f)
    for i in data:
        if i['username'] == username:
            user = i
            break
    if check_password_hash(user['password'],password):
        return jsonify({"massege":"login ho gaya bhaisahab",
                        "user":i
                        })
    else:
        return jsonify({"massege":"invalid user"})
@app.route('/',methods=['GET'])
def get_data():
    with open('first.json','r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/delete/<int:id>',methods=['DELETE'])
def dele(id):
    with open('first.json','r') as f:
        data = json.load(f)
    for i in data:
        if i["id"] == id:
            data.remove(i)
            return jsonify({"massege":"user Deleted"})
    return jsonify({"massege":"user Not Found"})

@app.route('/search',methods=['GET'])
def search():
    new_data = request.get_json()
    username = new_data.get('username')
    with open('first.json','r') as f:
        data = json.load(f)

    for i in data:
        if i['username'].lower() == username.lower():
            return jsonify(i)
        else:
            return jsonify({"massege":"usern not found"})
# @app.route('/update/<int:id>',methods=['PUT'])
# def update(id):
#     data = request.get_json()
#     username = data.get('username') 
if __name__ == '__main__':
    app.run(debug=True)