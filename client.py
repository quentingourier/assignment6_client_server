import requests
import json
import os

files = os.listdir(os.getcwd())
# print(files)

# url = "http://localhost:5000/hello"
# r = requests.get(url)
# print(r.text)

def welcome():
    username = input("\nWhat's your name : ")
    url = "http://localhost:5000/name"
    payload = {'data': username}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("\n  |", response.text, "\n  | status code = ", response.status_code)

def get_filename():
    print("\n Here is the list of available test files : \n")
    for f in files:
        if '.png' in f:
            print('- ',f)
    filename = input("\nEnter filename you'd want to test (ex: paper1) : ")
    url = "http://localhost:5000/filename"
    payload = {'data': filename}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("\n  |", response.text, "\n  | status code = ", response.status_code)
    return filename

def prediction_file():
    url = "http://localhost:5000/predict"
    payload = {'data': filename}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("\n  |", response.text, "\n  | status code = ", response.status_code)

welcome()
filename = get_filename()
prediction_file()













# import requests
# import json

# def hello():
#     url = "http://localhost:5000/hello"
#     r = requests.get(url)
#     print(r.text)

# def ask_name():
#     username = input("what's your name : ")
#     url = 'http://localhost:5000/message'
#     payload = {'data': username }
#     headers = {
#             'Content-Type': 'application/json'
#         }
#     response = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(response.text , response.status_code)


# def file_pick():
#     filename = input('which file would you like to test (enter filename) : ')
#     url = "http://localhost:5000/filename"

#     image= filename+'.png'
#     payload = {'data': image }
#     headers = {
#             'Content-Type': 'application/json'
#         }
#     response = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(response.text , response.status_code)



# hello()
# ask_name()



# import socket
# import pickle

# headersize = 10

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(), 1235))

# while True:
#     full_msg = b''
#     new_msg = True
#     while True:
#         msg = s.recv(16) #buffer = 8 i.e how much we want to receive at once
#         if new_msg:
#             print('new message length :', msg[:headersize])
#             msglen = int(msg[:headersize])
#             new_msg = False

#         full_msg += msg

#         if len(full_msg) - headersize == msglen:
#             print('full msg recvd')
#             print(full_msg[headersize:])

#             d = pickle.loads(full_msg[headersize:])
#             print(d)

#             new_msg = True
#             full_msg = 'b'
#     print(full_msg)
























