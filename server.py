
from flask import Flask, jsonify, request
import rps_algorithme

# initialize our Flask application
app= Flask(__name__)
@app.route("/name", methods=["POST"])
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        char_chain = "You are in Assignment 6 by @quentin, welcome "
        return jsonify(char_chain + str(data))

@app.route("/filename", methods=["POST"])
def setFile():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        char_chain = "Successfully found the following file : "
        return jsonify(char_chain + str(data)+'.png')

@app.route("/predict", methods=["POST"])
def setPredict():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        classes = rps_algorithme.prediction(data)
        if classes[0][0] == 1.0:
            result = 'The image you have submitted is classified as a PAPER'
        elif classes[0][1] == 1.0:
            result = 'The image you have submitted is classified as a ROCK'
        else:
            result = 'The image you have submitted is classified as a SCISSORS'

        return jsonify(result)

# @app.route("/hello", methods=["GET"])
# def hello():
#     return "<HTTML> <BODY> <STRONG> Hello </STRONG> World! </BODY> </HTML>"

#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)












# from flask import Flask, jsonify, request

# # initialize our Flask application
# app= Flask(__name__)
# @app.route("/filename", methods=["POST"])
# def setName():
#     if request.method=='POST':
#         posted_data = request.get_json()
#         data = posted_data['data']
#         print(jsonify(str("Successfully found  " + str(data))))
        

# @app.route("/message", methods=["GET"])
# def message():
#     posted_data = request.get_json()
#     name = posted_data['name']
#     return jsonify(" Hope you are having a good time " +  name + "!!!")

# @app.route("/hello", methods=["GET"])
# def hello():
#     return "Welcome to quentin's server"

# #  main thread of execution to start the server
# if __name__=='__main__':
#     app.run(debug=True)


# import socket
# import pickle


# headersize = 10

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 1235))  # Demande à l’OS d’associer la socket à une ip/port
# s.listen(5)   # transforme la socket en socket de connexion

# while True:
#   print(" waiting client… ")
#   clientsocket, address = s.accept()
#   print("connection established with ", {address})

#   d = {1: 'hey', 2: 'there'}
#   msg = pickle.dumps(d)



#   msg = bytes(f'{len(msg):<{headersize}}', 'utf-8') + msg

#   clientsocket.send(msg)















